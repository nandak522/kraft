# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/entities/order.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dprotobuf/entities/order.proto\x12\x11protobuf.entities\"7\n\tOrderItem\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08quantity\x18\x03 \x01(\r\"\xb8\x01\n\x05Order\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0f\n\x07user_id\x18\x02 \x01(\x04\x12.\n\x06status\x18\x03 \x01(\x0e\x32\x1e.protobuf.entities.OrderStatus\x12\x0c\n\x04\x63ost\x18\x04 \x01(\x02\x12\x12\n\ncreated_on\x18\x05 \x01(\x04\x12\x13\n\x0bmodified_on\x18\x06 \x01(\x04\x12+\n\x05items\x18\x07 \x03(\x0b\x32\x1c.protobuf.entities.OrderItem*H\n\x0bOrderStatus\x12\x0b\n\x07\x43REATED\x10\x00\x12\x0e\n\nINPROGRESS\x10\x01\x12\r\n\tDELIVERED\x10\x02\x12\r\n\tCANCELLED\x10\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protobuf.entities.order_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_ORDERSTATUS']._serialized_start=296
  _globals['_ORDERSTATUS']._serialized_end=368
  _globals['_ORDERITEM']._serialized_start=52
  _globals['_ORDERITEM']._serialized_end=107
  _globals['_ORDER']._serialized_start=110
  _globals['_ORDER']._serialized_end=294
# @@protoc_insertion_point(module_scope)
