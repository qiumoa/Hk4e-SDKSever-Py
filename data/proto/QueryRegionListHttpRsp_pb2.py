# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: QueryRegionListHttpRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import data.proto.RegionSimpleInfo_pb2 as RegionSimpleInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cQueryRegionListHttpRsp.proto\x1a\x16RegionSimpleInfo.proto\"\xad\x01\n\x16QueryRegionListHttpRsp\x12\x0f\n\x07retcode\x18\x01 \x01(\x05\x12&\n\x0bregion_list\x18\x02 \x03(\x0b\x32\x11.RegionSimpleInfo\x12\x19\n\x11\x63lient_secret_key\x18\x05 \x01(\x0c\x12&\n\x1e\x63lient_custom_config_encrypted\x18\x06 \x01(\x0c\x12\x17\n\x0f\x65nable_login_pc\x18\x07 \x01(\x08\x42\x16\n\x14org.sorapointa.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'QueryRegionListHttpRsp_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _globals['_QUERYREGIONLISTHTTPRSP']._serialized_start=57
  _globals['_QUERYREGIONLISTHTTPRSP']._serialized_end=230
# @@protoc_insertion_point(module_scope)
