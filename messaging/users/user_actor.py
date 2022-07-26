import ray
import logging
from ray.util.metrics import Counter
from messaging.internal_types import CombinedMessage
from messaging.utils import utils
from messaging.mailclient import MailClient
from .models import Device, User
from messaging.proto.MessageDataPB_pb2 import EMAIL as EMAIL_PROTOCOL
from messaging.settings.settings import Settings


# Seperate out the logic from the actor implementation so we can sub-class
# since you can not directly sub-class actors.


class UserActorBase():
    """
    Base client class for talking to the swarm.space APIs.
    Note: this actor is not async because django's ORM is not happy with
    async.
    """

    def __init__(self, settings: Settings, idx: int, poolsize: int):
        self.settings = settings
        self.idx = idx
        self.poolsize = poolsize
        self.satellite_pool = utils.LazyNamedPool("satellite", poolsize)
        self.mail_client = MailClient(self.settings)
        self.messages_forwarded = Counter(
            "messages_forwarded",
            description="Messages forwarded",
            tag_keys=("idx",),
        )
        self.messages_forwarded.set_default_tags(
            {"idx": str(idx)})
        self.messages_rejected = Counter(
            "messages_rejected",
            description="Rejected messages",
            tag_keys=("idx",),
        )
        self.messages_rejected.set_default_tags(
            {"idx": str(idx)})
        logging.info(f"Starting user actor {idx}")

    def _fetch_user(self, msg: CombinedMessage) -> User:
        """
        Find the user associated with the message.
        """
        if (msg.from_device):
            device = Device.objects.get(serial_number=msg.msg_from)
            return device.user
        else:
            # TODO: handle e-mail
            username = msg.to
            try:
                return User.objects.get(username=username)
            except Exception as e:
                print(f"Failed to get user: {username}?")
                raise e

    def prepare_for_shutdown(self):
        """
        Prepare for shutdown (not needed for sync DB connection)
        """
        pass

    def handle_message(self, input_msg: CombinedMessage):
        """
        Handle messages.
        """
        user = self._fetch_user(input_msg)
        self.messages_forwarded.inc()
        if (input_msg.from_device):
            msg = {
                "data": input_msg.text,
                "msg_from": f"{user.username}@spacebeaver.com",
                "msg_to": input_msg.to
            }
            # Underneath this calls a ray.remote method.
            self.mail_client.send_message(**msg)
        else:
            msg = {
                "protocol": EMAIL_PROTOCOL,
                "msg_from": input_msg.msg_from,
                "msg_to": user.device.serial_number,
                "data": input_msg.text
            }
            self.satellite_pool.get_pool().submit(
                lambda actor, msg: actor.send_message(**msg),
                msg)


@ray.remote(max_restarts=-1)
class UserActor(UserActorBase):
    """
    Routes messages and checks the user account info.
    """
