# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: default.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\rdefault.proto\x12\x1e\x61\x65\x61.eightballer.default.v0_1_0\"\xce\x06\n\x0e\x44\x65\x66\x61ultMessage\x12R\n\x05\x62ytes\x18\x05 \x01(\x0b\x32\x41.aea.eightballer.default.v0_1_0.DefaultMessage.Bytes_PerformativeH\x00\x12N\n\x03\x65nd\x18\x06 \x01(\x0b\x32?.aea.eightballer.default.v0_1_0.DefaultMessage.End_PerformativeH\x00\x12R\n\x05\x65rror\x18\x07 \x01(\x0b\x32\x41.aea.eightballer.default.v0_1_0.DefaultMessage.Error_PerformativeH\x00\x1a\xe8\x01\n\tErrorCode\x12Z\n\nerror_code\x18\x01 \x01(\x0e\x32\x46.aea.eightballer.default.v0_1_0.DefaultMessage.ErrorCode.ErrorCodeEnum\"\x7f\n\rErrorCodeEnum\x12\x18\n\x14UNSUPPORTED_PROTOCOL\x10\x00\x12\x12\n\x0e\x44\x45\x43ODING_ERROR\x10\x01\x12\x13\n\x0fINVALID_MESSAGE\x10\x02\x12\x15\n\x11UNSUPPORTED_SKILL\x10\x03\x12\x14\n\x10INVALID_DIALOGUE\x10\x04\x1a%\n\x12\x42ytes_Performative\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\x1a\x8d\x02\n\x12\x45rror_Performative\x12L\n\nerror_code\x18\x01 \x01(\x0b\x32\x38.aea.eightballer.default.v0_1_0.DefaultMessage.ErrorCode\x12\x11\n\terror_msg\x18\x02 \x01(\t\x12\x64\n\nerror_data\x18\x03 \x03(\x0b\x32P.aea.eightballer.default.v0_1_0.DefaultMessage.Error_Performative.ErrorDataEntry\x1a\x30\n\x0e\x45rrorDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\x1a\x12\n\x10\x45nd_PerformativeB\x0e\n\x0cperformativeb\x06proto3'
)


_DEFAULTMESSAGE = DESCRIPTOR.message_types_by_name['DefaultMessage']
_DEFAULTMESSAGE_ERRORCODE = _DEFAULTMESSAGE.nested_types_by_name['ErrorCode']
_DEFAULTMESSAGE_BYTES_PERFORMATIVE = _DEFAULTMESSAGE.nested_types_by_name['Bytes_Performative']
_DEFAULTMESSAGE_ERROR_PERFORMATIVE = _DEFAULTMESSAGE.nested_types_by_name['Error_Performative']
_DEFAULTMESSAGE_ERROR_PERFORMATIVE_ERRORDATAENTRY = _DEFAULTMESSAGE_ERROR_PERFORMATIVE.nested_types_by_name[
    'ErrorDataEntry'
]
_DEFAULTMESSAGE_END_PERFORMATIVE = _DEFAULTMESSAGE.nested_types_by_name['End_Performative']
_DEFAULTMESSAGE_ERRORCODE_ERRORCODEENUM = _DEFAULTMESSAGE_ERRORCODE.enum_types_by_name['ErrorCodeEnum']
DefaultMessage = _reflection.GeneratedProtocolMessageType(
    'DefaultMessage',
    (_message.Message,),
    {
        'ErrorCode': _reflection.GeneratedProtocolMessageType(
            'ErrorCode',
            (_message.Message,),
            {
                'DESCRIPTOR': _DEFAULTMESSAGE_ERRORCODE,
                '__module__': 'default_pb2'
                # @@protoc_insertion_point(class_scope:aea.eightballer.default.v0_1_0.DefaultMessage.ErrorCode)
            },
        ),
        'Bytes_Performative': _reflection.GeneratedProtocolMessageType(
            'Bytes_Performative',
            (_message.Message,),
            {
                'DESCRIPTOR': _DEFAULTMESSAGE_BYTES_PERFORMATIVE,
                '__module__': 'default_pb2'
                # @@protoc_insertion_point(class_scope:aea.eightballer.default.v0_1_0.DefaultMessage.Bytes_Performative)
            },
        ),
        'Error_Performative': _reflection.GeneratedProtocolMessageType(
            'Error_Performative',
            (_message.Message,),
            {
                'ErrorDataEntry': _reflection.GeneratedProtocolMessageType(
                    'ErrorDataEntry',
                    (_message.Message,),
                    {
                        'DESCRIPTOR': _DEFAULTMESSAGE_ERROR_PERFORMATIVE_ERRORDATAENTRY,
                        '__module__': 'default_pb2'
                        # @@protoc_insertion_point(class_scope:aea.eightballer.default.v0_1_0.DefaultMessage.Error_Performative.ErrorDataEntry)
                    },
                ),
                'DESCRIPTOR': _DEFAULTMESSAGE_ERROR_PERFORMATIVE,
                '__module__': 'default_pb2'
                # @@protoc_insertion_point(class_scope:aea.eightballer.default.v0_1_0.DefaultMessage.Error_Performative)
            },
        ),
        'End_Performative': _reflection.GeneratedProtocolMessageType(
            'End_Performative',
            (_message.Message,),
            {
                'DESCRIPTOR': _DEFAULTMESSAGE_END_PERFORMATIVE,
                '__module__': 'default_pb2'
                # @@protoc_insertion_point(class_scope:aea.eightballer.default.v0_1_0.DefaultMessage.End_Performative)
            },
        ),
        'DESCRIPTOR': _DEFAULTMESSAGE,
        '__module__': 'default_pb2'
        # @@protoc_insertion_point(class_scope:aea.eightballer.default.v0_1_0.DefaultMessage)
    },
)
_sym_db.RegisterMessage(DefaultMessage)
_sym_db.RegisterMessage(DefaultMessage.ErrorCode)
_sym_db.RegisterMessage(DefaultMessage.Bytes_Performative)
_sym_db.RegisterMessage(DefaultMessage.Error_Performative)
_sym_db.RegisterMessage(DefaultMessage.Error_Performative.ErrorDataEntry)
_sym_db.RegisterMessage(DefaultMessage.End_Performative)

if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _DEFAULTMESSAGE_ERROR_PERFORMATIVE_ERRORDATAENTRY._options = None
    _DEFAULTMESSAGE_ERROR_PERFORMATIVE_ERRORDATAENTRY._serialized_options = b'8\001'
    _DEFAULTMESSAGE._serialized_start = 50
    _DEFAULTMESSAGE._serialized_end = 896
    _DEFAULTMESSAGE_ERRORCODE._serialized_start = 317
    _DEFAULTMESSAGE_ERRORCODE._serialized_end = 549
    _DEFAULTMESSAGE_ERRORCODE_ERRORCODEENUM._serialized_start = 422
    _DEFAULTMESSAGE_ERRORCODE_ERRORCODEENUM._serialized_end = 549
    _DEFAULTMESSAGE_BYTES_PERFORMATIVE._serialized_start = 551
    _DEFAULTMESSAGE_BYTES_PERFORMATIVE._serialized_end = 588
    _DEFAULTMESSAGE_ERROR_PERFORMATIVE._serialized_start = 591
    _DEFAULTMESSAGE_ERROR_PERFORMATIVE._serialized_end = 860
    _DEFAULTMESSAGE_ERROR_PERFORMATIVE_ERRORDATAENTRY._serialized_start = 812
    _DEFAULTMESSAGE_ERROR_PERFORMATIVE_ERRORDATAENTRY._serialized_end = 860
    _DEFAULTMESSAGE_END_PERFORMATIVE._serialized_start = 862
    _DEFAULTMESSAGE_END_PERFORMATIVE._serialized_end = 880
# @@protoc_insertion_point(module_scope)
