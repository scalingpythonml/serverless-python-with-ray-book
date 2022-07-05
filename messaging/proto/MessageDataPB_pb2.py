# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MessageDataPB.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='MessageDataPB.proto',
  package='ca.pigscanfly.proto',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13MessageDataPB.proto\x12\x13\x63\x61.pigscanfly.proto\"d\n\rMessageDataPB\x12\x0f\n\x07version\x18\x01 \x02(\r\x12-\n\x07message\x18\x02 \x03(\x0b\x32\x1c.ca.pigscanfly.proto.Message\x12\x13\n\x0b\x66rom_device\x18\x03 \x02(\x08\"T\n\x07Message\x12\x0c\n\x04text\x18\x01 \x02(\t\x12\n\n\x02to\x18\x03 \x02(\t\x12/\n\x08protocol\x18\x05 \x02(\x0e\x32\x1d.ca.pigscanfly.proto.Protocol*8\n\x08Protocol\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05\x45MAIL\x10\x01\x12\x07\n\x03SMS\x10\x02\x12\x0b\n\x07TWITTER\x10\x03'
)

_PROTOCOL = _descriptor.EnumDescriptor(
  name='Protocol',
  full_name='ca.pigscanfly.proto.Protocol',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EMAIL', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SMS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TWITTER', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=232,
  serialized_end=288,
)
_sym_db.RegisterEnumDescriptor(_PROTOCOL)

Protocol = enum_type_wrapper.EnumTypeWrapper(_PROTOCOL)
UNKNOWN = 0
EMAIL = 1
SMS = 2
TWITTER = 3



_MESSAGEDATAPB = _descriptor.Descriptor(
  name='MessageDataPB',
  full_name='ca.pigscanfly.proto.MessageDataPB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='ca.pigscanfly.proto.MessageDataPB.version', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='ca.pigscanfly.proto.MessageDataPB.message', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='from_device', full_name='ca.pigscanfly.proto.MessageDataPB.from_device', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=144,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='ca.pigscanfly.proto.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='ca.pigscanfly.proto.Message.text', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to', full_name='ca.pigscanfly.proto.Message.to', index=1,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='protocol', full_name='ca.pigscanfly.proto.Message.protocol', index=2,
      number=5, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=146,
  serialized_end=230,
)

_MESSAGEDATAPB.fields_by_name['message'].message_type = _MESSAGE
_MESSAGE.fields_by_name['protocol'].enum_type = _PROTOCOL
DESCRIPTOR.message_types_by_name['MessageDataPB'] = _MESSAGEDATAPB
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.enum_types_by_name['Protocol'] = _PROTOCOL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MessageDataPB = _reflection.GeneratedProtocolMessageType('MessageDataPB', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEDATAPB,
  '__module__' : 'MessageDataPB_pb2'
  # @@protoc_insertion_point(class_scope:ca.pigscanfly.proto.MessageDataPB)
  })
_sym_db.RegisterMessage(MessageDataPB)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'MessageDataPB_pb2'
  # @@protoc_insertion_point(class_scope:ca.pigscanfly.proto.Message)
  })
_sym_db.RegisterMessage(Message)


# @@protoc_insertion_point(module_scope)
