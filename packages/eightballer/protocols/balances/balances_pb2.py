# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: balances.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0e\x62\x61lances.proto\x12\x1f\x61\x65\x61.eightballer.balances.v0_1_0\"\xfc\x0c\n\x0f\x42\x61lancesMessage\x12\x62\n\x0c\x61ll_balances\x18\x05 \x01(\x0b\x32J.aea.eightballer.balances.v0_1_0.BalancesMessage.All_Balances_PerformativeH\x00\x12X\n\x07\x62\x61lance\x18\x06 \x01(\x0b\x32\x45.aea.eightballer.balances.v0_1_0.BalancesMessage.Balance_PerformativeH\x00\x12T\n\x05\x65rror\x18\x07 \x01(\x0b\x32\x43.aea.eightballer.balances.v0_1_0.BalancesMessage.Error_PerformativeH\x00\x12j\n\x10get_all_balances\x18\x08 \x01(\x0b\x32N.aea.eightballer.balances.v0_1_0.BalancesMessage.Get_All_Balances_PerformativeH\x00\x12`\n\x0bget_balance\x18\t \x01(\x0b\x32I.aea.eightballer.balances.v0_1_0.BalancesMessage.Get_Balance_PerformativeH\x00\x1aQ\n\x07\x42\x61lance\x1a\x46\n\x07\x42\x61lance\x12\x10\n\x08\x61sset_id\x18\x01 \x01(\t\x12\x0c\n\x04\x66ree\x18\x02 \x01(\x02\x12\x0c\n\x04used\x18\x03 \x01(\x02\x12\r\n\x05total\x18\x04 \x01(\x02\x1a\x62\n\x08\x42\x61lances\x1aV\n\x08\x42\x61lances\x12J\n\x08\x62\x61lances\x18\x01 \x03(\x0b\x32\x38.aea.eightballer.balances.v0_1_0.BalancesMessage.Balance\x1a\xb2\x01\n\tErrorCode\x12\\\n\nerror_code\x18\x01 \x01(\x0e\x32H.aea.eightballer.balances.v0_1_0.BalancesMessage.ErrorCode.ErrorCodeEnum\"G\n\rErrorCodeEnum\x12\x14\n\x10UNKNOWN_EXCHANGE\x10\x00\x12\x11\n\rUNKNOWN_ASSET\x10\x01\x12\r\n\tAPI_ERROR\x10\x02\x1a\xe6\x01\n\x1dGet_All_Balances_Performative\x12\x13\n\x0b\x65xchange_id\x18\x01 \x01(\t\x12j\n\x06params\x18\x02 \x03(\x0b\x32Z.aea.eightballer.balances.v0_1_0.BalancesMessage.Get_All_Balances_Performative.ParamsEntry\x12\x15\n\rparams_is_set\x18\x03 \x01(\x08\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\x1a\x41\n\x18Get_Balance_Performative\x12\x10\n\x08\x61sset_id\x18\x01 \x01(\t\x12\x13\n\x0b\x65xchange_id\x18\x02 \x01(\t\x1ah\n\x19\x41ll_Balances_Performative\x12K\n\x08\x62\x61lances\x18\x01 \x01(\x0b\x32\x39.aea.eightballer.balances.v0_1_0.BalancesMessage.Balances\x1a\x61\n\x14\x42\x61lance_Performative\x12I\n\x07\x62\x61lance\x18\x01 \x01(\x0b\x32\x38.aea.eightballer.balances.v0_1_0.BalancesMessage.Balance\x1a\x91\x02\n\x12\x45rror_Performative\x12N\n\nerror_code\x18\x01 \x01(\x0b\x32:.aea.eightballer.balances.v0_1_0.BalancesMessage.ErrorCode\x12\x11\n\terror_msg\x18\x02 \x01(\t\x12\x66\n\nerror_data\x18\x03 \x03(\x0b\x32R.aea.eightballer.balances.v0_1_0.BalancesMessage.Error_Performative.ErrorDataEntry\x1a\x30\n\x0e\x45rrorDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\x42\x0e\n\x0cperformativeb\x06proto3'
)


_BALANCESMESSAGE = DESCRIPTOR.message_types_by_name['BalancesMessage']
_BALANCESMESSAGE_BALANCE = _BALANCESMESSAGE.nested_types_by_name['Balance']
_BALANCESMESSAGE_BALANCE_BALANCE = _BALANCESMESSAGE_BALANCE.nested_types_by_name['Balance']
_BALANCESMESSAGE_BALANCES = _BALANCESMESSAGE.nested_types_by_name['Balances']
_BALANCESMESSAGE_BALANCES_BALANCES = _BALANCESMESSAGE_BALANCES.nested_types_by_name['Balances']
_BALANCESMESSAGE_ERRORCODE = _BALANCESMESSAGE.nested_types_by_name['ErrorCode']
_BALANCESMESSAGE_GET_ALL_BALANCES_PERFORMATIVE = _BALANCESMESSAGE.nested_types_by_name['Get_All_Balances_Performative']
_BALANCESMESSAGE_GET_ALL_BALANCES_PERFORMATIVE_PARAMSENTRY = (
    _BALANCESMESSAGE_GET_ALL_BALANCES_PERFORMATIVE.nested_types_by_name['ParamsEntry']
)
_BALANCESMESSAGE_GET_BALANCE_PERFORMATIVE = _BALANCESMESSAGE.nested_types_by_name['Get_Balance_Performative']
_BALANCESMESSAGE_ALL_BALANCES_PERFORMATIVE = _BALANCESMESSAGE.nested_types_by_name['All_Balances_Performative']
_BALANCESMESSAGE_BALANCE_PERFORMATIVE = _BALANCESMESSAGE.nested_types_by_name['Balance_Performative']
_BALANCESMESSAGE_ERROR_PERFORMATIVE = _BALANCESMESSAGE.nested_types_by_name['Error_Performative']
_BALANCESMESSAGE_ERROR_PERFORMATIVE_ERRORDATAENTRY = _BALANCESMESSAGE_ERROR_PERFORMATIVE.nested_types_by_name[
    'ErrorDataEntry'
]
_BALANCESMESSAGE_ERRORCODE_ERRORCODEENUM = _BALANCESMESSAGE_ERRORCODE.enum_types_by_name['ErrorCodeEnum']
BalancesMessage = _reflection.GeneratedProtocolMessageType(
    'BalancesMessage',
    (_message.Message,),
    {
        'Balance': _reflection.GeneratedProtocolMessageType(
            'Balance',
            (_message.Message,),
            {
                'Balance': _reflection.GeneratedProtocolMessageType(
                    'Balance',
                    (_message.Message,),
                    {
                        'DESCRIPTOR': _BALANCESMESSAGE_BALANCE_BALANCE,
                        '__module__': 'balances_pb2'
                        # @@protoc_insertion_point(class_scope:aea.eightballer.balances.v0_1_0.BalancesMessage.Balance.Balance)
                    },
                ),
                'DESCRIPTOR': _BALANCESMESSAGE_BALANCE,
                '__module__': 'balances_pb2'
                # @@protoc_insertion_point(class_scope:aea.eightballer.balances.v0_1_0.BalancesMessage.Balance)
            },
        ),
        'Balances': _reflection.GeneratedProtocolMessageType(
            'Balances',
            (_message.Message,),
            {
                'Balances': _reflection.GeneratedProtocolMessageType(
                    'Balances',
                    (_message.Message,),
                    {
                        'DESCRIPTOR': _BALANCESMESSAGE_BALANCES_BALANCES,
                        '__module__': 'balances_pb2'
                        # @@protoc_insertion_point(class_scope:aea.eightballer.balances.v0_1_0.BalancesMessage.Balances.Balances)
                    },
                ),
                'DESCRIPTOR': _BALANCESMESSAGE_BALANCES,
                '__module__': 'balances_pb2'
                # @@protoc_insertion_point(class_scope:aea.eightballer.balances.v0_1_0.BalancesMessage.Balances)
            },
        ),
        'ErrorCode': _reflection.GeneratedProtocolMessageType(
            'ErrorCode',
            (_message.Message,),
            {
                'DESCRIPTOR': _BALANCESMESSAGE_ERRORCODE,
                '__module__': 'balances_pb2'
                # @@protoc_insertion_point(class_scope:aea.eightballer.balances.v0_1_0.BalancesMessage.ErrorCode)
            },
        ),
        'Get_All_Balances_Performative': _reflection.GeneratedProtocolMessageType(
            'Get_All_Balances_Performative',
            (_message.Message,),
            {
                'ParamsEntry': _reflection.GeneratedProtocolMessageType(
                    'ParamsEntry',
                    (_message.Message,),
                    {
                        'DESCRIPTOR': _BALANCESMESSAGE_GET_ALL_BALANCES_PERFORMATIVE_PARAMSENTRY,
                        '__module__': 'balances_pb2'
                        # @@protoc_insertion_point(class_scope:aea.eightballer.balances.v0_1_0.BalancesMessage.Get_All_Balances_Performative.ParamsEntry)
                    },
                ),
                'DESCRIPTOR': _BALANCESMESSAGE_GET_ALL_BALANCES_PERFORMATIVE,
                '__module__': 'balances_pb2'
                # @@protoc_insertion_point(class_scope:aea.eightballer.balances.v0_1_0.BalancesMessage.Get_All_Balances_Performative)
            },
        ),
        'Get_Balance_Performative': _reflection.GeneratedProtocolMessageType(
            'Get_Balance_Performative',
            (_message.Message,),
            {
                'DESCRIPTOR': _BALANCESMESSAGE_GET_BALANCE_PERFORMATIVE,
                '__module__': 'balances_pb2'
                # @@protoc_insertion_point(class_scope:aea.eightballer.balances.v0_1_0.BalancesMessage.Get_Balance_Performative)
            },
        ),
        'All_Balances_Performative': _reflection.GeneratedProtocolMessageType(
            'All_Balances_Performative',
            (_message.Message,),
            {
                'DESCRIPTOR': _BALANCESMESSAGE_ALL_BALANCES_PERFORMATIVE,
                '__module__': 'balances_pb2'
                # @@protoc_insertion_point(class_scope:aea.eightballer.balances.v0_1_0.BalancesMessage.All_Balances_Performative)
            },
        ),
        'Balance_Performative': _reflection.GeneratedProtocolMessageType(
            'Balance_Performative',
            (_message.Message,),
            {
                'DESCRIPTOR': _BALANCESMESSAGE_BALANCE_PERFORMATIVE,
                '__module__': 'balances_pb2'
                # @@protoc_insertion_point(class_scope:aea.eightballer.balances.v0_1_0.BalancesMessage.Balance_Performative)
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
                        'DESCRIPTOR': _BALANCESMESSAGE_ERROR_PERFORMATIVE_ERRORDATAENTRY,
                        '__module__': 'balances_pb2'
                        # @@protoc_insertion_point(class_scope:aea.eightballer.balances.v0_1_0.BalancesMessage.Error_Performative.ErrorDataEntry)
                    },
                ),
                'DESCRIPTOR': _BALANCESMESSAGE_ERROR_PERFORMATIVE,
                '__module__': 'balances_pb2'
                # @@protoc_insertion_point(class_scope:aea.eightballer.balances.v0_1_0.BalancesMessage.Error_Performative)
            },
        ),
        'DESCRIPTOR': _BALANCESMESSAGE,
        '__module__': 'balances_pb2'
        # @@protoc_insertion_point(class_scope:aea.eightballer.balances.v0_1_0.BalancesMessage)
    },
)
_sym_db.RegisterMessage(BalancesMessage)
_sym_db.RegisterMessage(BalancesMessage.Balance)
_sym_db.RegisterMessage(BalancesMessage.Balance.Balance)
_sym_db.RegisterMessage(BalancesMessage.Balances)
_sym_db.RegisterMessage(BalancesMessage.Balances.Balances)
_sym_db.RegisterMessage(BalancesMessage.ErrorCode)
_sym_db.RegisterMessage(BalancesMessage.Get_All_Balances_Performative)
_sym_db.RegisterMessage(BalancesMessage.Get_All_Balances_Performative.ParamsEntry)
_sym_db.RegisterMessage(BalancesMessage.Get_Balance_Performative)
_sym_db.RegisterMessage(BalancesMessage.All_Balances_Performative)
_sym_db.RegisterMessage(BalancesMessage.Balance_Performative)
_sym_db.RegisterMessage(BalancesMessage.Error_Performative)
_sym_db.RegisterMessage(BalancesMessage.Error_Performative.ErrorDataEntry)

if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _BALANCESMESSAGE_GET_ALL_BALANCES_PERFORMATIVE_PARAMSENTRY._options = None
    _BALANCESMESSAGE_GET_ALL_BALANCES_PERFORMATIVE_PARAMSENTRY._serialized_options = b'8\001'
    _BALANCESMESSAGE_ERROR_PERFORMATIVE_ERRORDATAENTRY._options = None
    _BALANCESMESSAGE_ERROR_PERFORMATIVE_ERRORDATAENTRY._serialized_options = b'8\001'
    _BALANCESMESSAGE._serialized_start = 52
    _BALANCESMESSAGE._serialized_end = 1712
    _BALANCESMESSAGE_BALANCE._serialized_start = 553
    _BALANCESMESSAGE_BALANCE._serialized_end = 634
    _BALANCESMESSAGE_BALANCE_BALANCE._serialized_start = 564
    _BALANCESMESSAGE_BALANCE_BALANCE._serialized_end = 634
    _BALANCESMESSAGE_BALANCES._serialized_start = 636
    _BALANCESMESSAGE_BALANCES._serialized_end = 734
    _BALANCESMESSAGE_BALANCES_BALANCES._serialized_start = 648
    _BALANCESMESSAGE_BALANCES_BALANCES._serialized_end = 734
    _BALANCESMESSAGE_ERRORCODE._serialized_start = 737
    _BALANCESMESSAGE_ERRORCODE._serialized_end = 915
    _BALANCESMESSAGE_ERRORCODE_ERRORCODEENUM._serialized_start = 844
    _BALANCESMESSAGE_ERRORCODE_ERRORCODEENUM._serialized_end = 915
    _BALANCESMESSAGE_GET_ALL_BALANCES_PERFORMATIVE._serialized_start = 918
    _BALANCESMESSAGE_GET_ALL_BALANCES_PERFORMATIVE._serialized_end = 1148
    _BALANCESMESSAGE_GET_ALL_BALANCES_PERFORMATIVE_PARAMSENTRY._serialized_start = 1103
    _BALANCESMESSAGE_GET_ALL_BALANCES_PERFORMATIVE_PARAMSENTRY._serialized_end = 1148
    _BALANCESMESSAGE_GET_BALANCE_PERFORMATIVE._serialized_start = 1150
    _BALANCESMESSAGE_GET_BALANCE_PERFORMATIVE._serialized_end = 1215
    _BALANCESMESSAGE_ALL_BALANCES_PERFORMATIVE._serialized_start = 1217
    _BALANCESMESSAGE_ALL_BALANCES_PERFORMATIVE._serialized_end = 1321
    _BALANCESMESSAGE_BALANCE_PERFORMATIVE._serialized_start = 1323
    _BALANCESMESSAGE_BALANCE_PERFORMATIVE._serialized_end = 1420
    _BALANCESMESSAGE_ERROR_PERFORMATIVE._serialized_start = 1423
    _BALANCESMESSAGE_ERROR_PERFORMATIVE._serialized_end = 1696
    _BALANCESMESSAGE_ERROR_PERFORMATIVE_ERRORDATAENTRY._serialized_start = 1648
    _BALANCESMESSAGE_ERROR_PERFORMATIVE_ERRORDATAENTRY._serialized_end = 1696
# @@protoc_insertion_point(module_scope)
