# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2024 eightballer
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""Serialization module for funding protocol."""

# pylint: disable=too-many-statements,too-many-locals,no-member,too-few-public-methods,redefined-builtin,C0209,R1735
# pylint: disable=E0611,R0912,C0209,R1735
from typing import cast

from aea.mail.base_pb2 import DialogueMessage
from aea.mail.base_pb2 import Message as ProtobufMessage
from aea.protocols.base import Message, Serializer

from packages.eightballer.protocols.funding import funding_pb2
from packages.eightballer.protocols.funding.custom_types import FundingData
from packages.eightballer.protocols.funding.message import FundingMessage


class FundingSerializer(Serializer):
    """Serialization for the 'funding' protocol."""

    @staticmethod
    def encode(msg: Message) -> bytes:
        """
        Encode a 'Funding' message into bytes.

        :param msg: the message object.
        :return: the bytes.
        """
        msg = cast(FundingMessage, msg)
        message_pb = ProtobufMessage()
        dialogue_message_pb = DialogueMessage()
        funding_msg = funding_pb2.FundingMessage()

        dialogue_message_pb.message_id = msg.message_id
        dialogue_reference = msg.dialogue_reference
        dialogue_message_pb.dialogue_starter_reference = dialogue_reference[0]
        dialogue_message_pb.dialogue_responder_reference = dialogue_reference[1]
        dialogue_message_pb.target = msg.target

        performative_id = msg.performative
        if performative_id == FundingMessage.Performative.GET_FUNDING_RATE:
            performative = funding_pb2.FundingMessage.Get_Funding_Rate_Performative()  # type: ignore
            exchange_id = msg.exchange_id
            performative.exchange_id = exchange_id
            symbol = msg.symbol
            performative.symbol = symbol
            funding_msg.get_funding_rate.CopyFrom(performative)
        elif performative_id == FundingMessage.Performative.FUNDING_RATE:
            performative = funding_pb2.FundingMessage.Funding_Rate_Performative()  # type: ignore
            funding_data = msg.funding_data
            FundingData.encode(performative.funding_data, funding_data)
            funding_msg.funding_rate.CopyFrom(performative)
        elif performative_id == FundingMessage.Performative.SUBSCRIBE:
            performative = funding_pb2.FundingMessage.Subscribe_Performative()  # type: ignore
            exchange_id = msg.exchange_id
            performative.exchange_id = exchange_id
            symbol = msg.symbol
            performative.symbol = symbol
            funding_msg.subscribe.CopyFrom(performative)
        elif performative_id == FundingMessage.Performative.UNSUBSCRIBE:
            performative = funding_pb2.FundingMessage.Unsubscribe_Performative()  # type: ignore
            exchange_id = msg.exchange_id
            performative.exchange_id = exchange_id
            symbol = msg.symbol
            performative.symbol = symbol
            funding_msg.unsubscribe.CopyFrom(performative)
        elif performative_id == FundingMessage.Performative.FUNDING_UPDATE:
            performative = funding_pb2.FundingMessage.Funding_Update_Performative()  # type: ignore
            funding_data = msg.funding_data
            FundingData.encode(performative.funding_data, funding_data)
            funding_msg.funding_update.CopyFrom(performative)
        elif performative_id == FundingMessage.Performative.ERROR:
            performative = funding_pb2.FundingMessage.Error_Performative()  # type: ignore
            error_msg = msg.error_msg
            performative.error_msg = error_msg
            funding_msg.error.CopyFrom(performative)
        else:
            raise ValueError("Performative not valid: {}".format(performative_id))

        dialogue_message_pb.content = funding_msg.SerializeToString()

        message_pb.dialogue_message.CopyFrom(dialogue_message_pb)
        message_bytes = message_pb.SerializeToString()
        return message_bytes

    @staticmethod
    def decode(obj: bytes) -> Message:
        """
        Decode bytes into a 'Funding' message.

        :param obj: the bytes object.
        :return: the 'Funding' message.
        """
        message_pb = ProtobufMessage()
        funding_pb = funding_pb2.FundingMessage()
        message_pb.ParseFromString(obj)
        message_id = message_pb.dialogue_message.message_id
        dialogue_reference = (
            message_pb.dialogue_message.dialogue_starter_reference,
            message_pb.dialogue_message.dialogue_responder_reference,
        )
        target = message_pb.dialogue_message.target

        funding_pb.ParseFromString(message_pb.dialogue_message.content)
        performative = funding_pb.WhichOneof("performative")
        performative_id = FundingMessage.Performative(str(performative))
        performative_content = dict()  # type: Dict[str, Any]
        if performative_id == FundingMessage.Performative.GET_FUNDING_RATE:
            exchange_id = funding_pb.get_funding_rate.exchange_id
            performative_content["exchange_id"] = exchange_id
            symbol = funding_pb.get_funding_rate.symbol
            performative_content["symbol"] = symbol
        elif performative_id == FundingMessage.Performative.FUNDING_RATE:
            pb2_funding_data = funding_pb.funding_rate.funding_data
            funding_data = FundingData.decode(pb2_funding_data)
            performative_content["funding_data"] = funding_data
        elif performative_id == FundingMessage.Performative.SUBSCRIBE:
            exchange_id = funding_pb.subscribe.exchange_id
            performative_content["exchange_id"] = exchange_id
            symbol = funding_pb.subscribe.symbol
            performative_content["symbol"] = symbol
        elif performative_id == FundingMessage.Performative.UNSUBSCRIBE:
            exchange_id = funding_pb.unsubscribe.exchange_id
            performative_content["exchange_id"] = exchange_id
            symbol = funding_pb.unsubscribe.symbol
            performative_content["symbol"] = symbol
        elif performative_id == FundingMessage.Performative.FUNDING_UPDATE:
            pb2_funding_data = funding_pb.funding_update.funding_data
            funding_data = FundingData.decode(pb2_funding_data)
            performative_content["funding_data"] = funding_data
        elif performative_id == FundingMessage.Performative.ERROR:
            error_msg = funding_pb.error.error_msg
            performative_content["error_msg"] = error_msg
        else:
            raise ValueError("Performative not valid: {}.".format(performative_id))

        return FundingMessage(
            message_id=message_id,
            dialogue_reference=dialogue_reference,
            target=target,
            performative=performative,
            **performative_content,
        )