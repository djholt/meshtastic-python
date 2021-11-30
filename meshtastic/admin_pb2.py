# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: admin.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mesh_pb2 as mesh__pb2
from . import radioconfig_pb2 as radioconfig__pb2
from . import channel_pb2 as channel__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='admin.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n\023com.geeksville.meshB\013AdminProtosH\003Z!github.com/meshtastic/gomeshproto',
  serialized_pb=b'\n\x0b\x61\x64min.proto\x1a\nmesh.proto\x1a\x11radioconfig.proto\x1a\rchannel.proto\"\xfb\x02\n\x0c\x41\x64minMessage\x12!\n\tset_radio\x18\x01 \x01(\x0b\x32\x0c.RadioConfigH\x00\x12\x1a\n\tset_owner\x18\x02 \x01(\x0b\x32\x05.UserH\x00\x12\x1f\n\x0bset_channel\x18\x03 \x01(\x0b\x32\x08.ChannelH\x00\x12\x1b\n\x11get_radio_request\x18\x04 \x01(\x08H\x00\x12*\n\x12get_radio_response\x18\x05 \x01(\x0b\x32\x0c.RadioConfigH\x00\x12\x1d\n\x13get_channel_request\x18\x06 \x01(\rH\x00\x12(\n\x14get_channel_response\x18\x07 \x01(\x0b\x32\x08.ChannelH\x00\x12\x1d\n\x13\x63onfirm_set_channel\x18  \x01(\x08H\x00\x12\x1b\n\x11\x63onfirm_set_radio\x18! \x01(\x08H\x00\x12\x18\n\x0e\x65xit_simulator\x18\" \x01(\x08H\x00\x12\x18\n\x0ereboot_seconds\x18# \x01(\x05H\x00\x42\t\n\x07variantBG\n\x13\x63om.geeksville.meshB\x0b\x41\x64minProtosH\x03Z!github.com/meshtastic/gomeshprotob\x06proto3'
  ,
  dependencies=[mesh__pb2.DESCRIPTOR,radioconfig__pb2.DESCRIPTOR,channel__pb2.DESCRIPTOR,])




_ADMINMESSAGE = _descriptor.Descriptor(
  name='AdminMessage',
  full_name='AdminMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='set_radio', full_name='AdminMessage.set_radio', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='set_owner', full_name='AdminMessage.set_owner', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='set_channel', full_name='AdminMessage.set_channel', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_radio_request', full_name='AdminMessage.get_radio_request', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_radio_response', full_name='AdminMessage.get_radio_response', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_channel_request', full_name='AdminMessage.get_channel_request', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_channel_response', full_name='AdminMessage.get_channel_response', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confirm_set_channel', full_name='AdminMessage.confirm_set_channel', index=7,
      number=32, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confirm_set_radio', full_name='AdminMessage.confirm_set_radio', index=8,
      number=33, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exit_simulator', full_name='AdminMessage.exit_simulator', index=9,
      number=34, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reboot_seconds', full_name='AdminMessage.reboot_seconds', index=10,
      number=35, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='variant', full_name='AdminMessage.variant',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=62,
  serialized_end=441,
)

_ADMINMESSAGE.fields_by_name['set_radio'].message_type = radioconfig__pb2._RADIOCONFIG
_ADMINMESSAGE.fields_by_name['set_owner'].message_type = mesh__pb2._USER
_ADMINMESSAGE.fields_by_name['set_channel'].message_type = channel__pb2._CHANNEL
_ADMINMESSAGE.fields_by_name['get_radio_response'].message_type = radioconfig__pb2._RADIOCONFIG
_ADMINMESSAGE.fields_by_name['get_channel_response'].message_type = channel__pb2._CHANNEL
_ADMINMESSAGE.oneofs_by_name['variant'].fields.append(
  _ADMINMESSAGE.fields_by_name['set_radio'])
_ADMINMESSAGE.fields_by_name['set_radio'].containing_oneof = _ADMINMESSAGE.oneofs_by_name['variant']
_ADMINMESSAGE.oneofs_by_name['variant'].fields.append(
  _ADMINMESSAGE.fields_by_name['set_owner'])
_ADMINMESSAGE.fields_by_name['set_owner'].containing_oneof = _ADMINMESSAGE.oneofs_by_name['variant']
_ADMINMESSAGE.oneofs_by_name['variant'].fields.append(
  _ADMINMESSAGE.fields_by_name['set_channel'])
_ADMINMESSAGE.fields_by_name['set_channel'].containing_oneof = _ADMINMESSAGE.oneofs_by_name['variant']
_ADMINMESSAGE.oneofs_by_name['variant'].fields.append(
  _ADMINMESSAGE.fields_by_name['get_radio_request'])
_ADMINMESSAGE.fields_by_name['get_radio_request'].containing_oneof = _ADMINMESSAGE.oneofs_by_name['variant']
_ADMINMESSAGE.oneofs_by_name['variant'].fields.append(
  _ADMINMESSAGE.fields_by_name['get_radio_response'])
_ADMINMESSAGE.fields_by_name['get_radio_response'].containing_oneof = _ADMINMESSAGE.oneofs_by_name['variant']
_ADMINMESSAGE.oneofs_by_name['variant'].fields.append(
  _ADMINMESSAGE.fields_by_name['get_channel_request'])
_ADMINMESSAGE.fields_by_name['get_channel_request'].containing_oneof = _ADMINMESSAGE.oneofs_by_name['variant']
_ADMINMESSAGE.oneofs_by_name['variant'].fields.append(
  _ADMINMESSAGE.fields_by_name['get_channel_response'])
_ADMINMESSAGE.fields_by_name['get_channel_response'].containing_oneof = _ADMINMESSAGE.oneofs_by_name['variant']
_ADMINMESSAGE.oneofs_by_name['variant'].fields.append(
  _ADMINMESSAGE.fields_by_name['confirm_set_channel'])
_ADMINMESSAGE.fields_by_name['confirm_set_channel'].containing_oneof = _ADMINMESSAGE.oneofs_by_name['variant']
_ADMINMESSAGE.oneofs_by_name['variant'].fields.append(
  _ADMINMESSAGE.fields_by_name['confirm_set_radio'])
_ADMINMESSAGE.fields_by_name['confirm_set_radio'].containing_oneof = _ADMINMESSAGE.oneofs_by_name['variant']
_ADMINMESSAGE.oneofs_by_name['variant'].fields.append(
  _ADMINMESSAGE.fields_by_name['exit_simulator'])
_ADMINMESSAGE.fields_by_name['exit_simulator'].containing_oneof = _ADMINMESSAGE.oneofs_by_name['variant']
_ADMINMESSAGE.oneofs_by_name['variant'].fields.append(
  _ADMINMESSAGE.fields_by_name['reboot_seconds'])
_ADMINMESSAGE.fields_by_name['reboot_seconds'].containing_oneof = _ADMINMESSAGE.oneofs_by_name['variant']
DESCRIPTOR.message_types_by_name['AdminMessage'] = _ADMINMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdminMessage = _reflection.GeneratedProtocolMessageType('AdminMessage', (_message.Message,), {
  'DESCRIPTOR' : _ADMINMESSAGE,
  '__module__' : 'admin_pb2'
  # @@protoc_insertion_point(class_scope:AdminMessage)
  })
_sym_db.RegisterMessage(AdminMessage)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
