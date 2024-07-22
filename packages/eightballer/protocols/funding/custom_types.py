# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
# Copyright 2024 Mihai Cosma
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# ------------------------------------------------------------------------------

"""This module contains class representations corresponding to every custom type in the protocol specification."""

from dataclasses import dataclass
from typing import Optional

@dataclass
class Funding:
    """This class represents an instance of Funding."""

    symbol: str = None
    mark_price: float = None
    index_price: float = None
    interest_rate: float = None
    estimated_settle_price: Optional[float] = None
    timestamp: Optional[int] = None
    datetime: Optional[str] = None
    funding_rate: float = None
    funding_timestamp: int = None
    funding_datetime: str = None
    next_funding_rate: Optional[float] = None
    next_funding_timestamp: Optional[int] = None
    next_funding_datetime: Optional[str] = None
    previous_funding_rate: Optional[float] = None
    previous_funding_timestamp: Optional[int] = None
    previous_funding_datetime: Optional[str] = None
    exchange_id: str = None

    @staticmethod
    def encode(funding_data_protobuf_object, funding_data_object: "Funding") -> None:
        """
        Encode an instance of this class into the protocol buffer object.
        The protocol buffer object in the funding_data_protobuf_object argument is matched with the instance of this class in the 'funding_data_object' argument.
        :param funding_data_protobuf_object: the protocol buffer object whose type corresponds with this class.
        :param funding_data_object: an instance of this class to be encoded in the protocol buffer object.
        """
        funding_data_protobuf_object.symbol = funding_data_object.symbol
        funding_data_protobuf_object.mark_price = funding_data_object.mark_price
        funding_data_protobuf_object.index_price = funding_data_object.index_price
        funding_data_protobuf_object.interest_rate = funding_data_object.interest_rate
        funding_data_protobuf_object.estimated_settle_price = funding_data_object.estimated_settle_price
        funding_data_protobuf_object.timestamp = funding_data_object.timestamp
        funding_data_protobuf_object.datetime = funding_data_object.datetime
        funding_data_protobuf_object.funding_rate = funding_data_object.funding_rate
        funding_data_protobuf_object.funding_timestamp = funding_data_object.funding_timestamp
        funding_data_protobuf_object.funding_datetime = funding_data_object.funding_datetime
        funding_data_protobuf_object.next_funding_rate = funding_data_object.next_funding_rate
        funding_data_protobuf_object.next_funding_timestamp = funding_data_object.next_funding_timestamp
        funding_data_protobuf_object.next_funding_datetime = funding_data_object.next_funding_datetime
        funding_data_protobuf_object.previous_funding_rate = funding_data_object.previous_funding_rate
        funding_data_protobuf_object.previous_funding_timestamp = funding_data_object.previous_funding_timestamp
        funding_data_protobuf_object.previous_funding_datetime = funding_data_object.previous_funding_datetime
        funding_data_protobuf_object.exchange_id = funding_data_object.exchange_id

    @classmethod
    def decode(cls, funding_data_protobuf_object) -> "Funding":
        """
        Decode a protocol buffer object that corresponds with this class into an instance of this class.
        A new instance of this class is created that matches the protocol buffer object in the 'funding_data_protobuf_object' argument.
        :param funding_data_protobuf_object: the protocol buffer object whose type corresponds with this class.
        :return: A new instance of this class that matches the protocol buffer object in the 'funding_data_protobuf_object' argument.
        """
        funding_data = cls(
            symbol=funding_data_protobuf_object.symbol,
            mark_price=funding_data_protobuf_object.mark_price,
            index_price=funding_data_protobuf_object.index_price,
            interest_rate=funding_data_protobuf_object.interest_rate,
            estimated_settle_price=funding_data_protobuf_object.estimated_settle_price,
            timestamp=funding_data_protobuf_object.timestamp,
            datetime=funding_data_protobuf_object.datetime,
            funding_rate=funding_data_protobuf_object.funding_rate,
            funding_timestamp=funding_data_protobuf_object.funding_timestamp,
            funding_datetime=funding_data_protobuf_object.funding_datetime,
            next_funding_rate=funding_data_protobuf_object.next_funding_rate,
            next_funding_timestamp=funding_data_protobuf_object.next_funding_timestamp,
            next_funding_datetime=funding_data_protobuf_object.next_funding_datetime,
            previous_funding_rate=funding_data_protobuf_object.previous_funding_rate,
            previous_funding_timestamp=funding_data_protobuf_object.previous_funding_timestamp,
            previous_funding_datetime=funding_data_protobuf_object.previous_funding_datetime,
            exchange_id=funding_data_protobuf_object.exchange_id
        )
        return funding_data

    def __eq__(self, other):
        return (
            self.symbol == other.symbol
            and self.mark_price == other.mark_price
            and self.index_price == other.index_price
            and self.interest_rate == other.interest_rate
            and self.estimated_settle_price == other.estimated_settle_price
            and self.timestamp == other.timestamp
            and self.datetime == other.datetime
            and self.funding_rate == other.funding_rate
            and self.funding_timestamp == other.funding_timestamp
            and self.funding_datetime == other.funding_datetime
            and self.next_funding_rate == other.next_funding_rate
            and self.next_funding_timestamp == other.next_funding_timestamp
            and self.next_funding_datetime == other.next_funding_datetime
            and self.previous_funding_rate == other.previous_funding_rate
            and self.previous_funding_timestamp == other.previous_funding_timestamp
            and self.previous_funding_datetime == other.previous_funding_datetime
            and self.exchange_id == other.exchange_id
        )