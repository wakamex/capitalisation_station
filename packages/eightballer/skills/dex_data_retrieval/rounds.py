# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2023 Valory AG
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

"""This package contains the rounds of AbciApp."""

import json
from enum import Enum
from typing import Dict, Optional, Set, Tuple

from packages.eightballer.skills.dex_data_retrieval.payloads import (
    FetchDexBalancesPayload,
    FetchDexMarketsPayload,
    FetchDexOrdersPayload,
    FetchDexPositionsPayload,
    FetchDexTickersPayload,
)
from packages.valory.skills.abstract_round_abci.base import (
    AbciApp,
    AbciAppTransitionFunction,
    AppState,
    BaseSynchronizedData,
    CollectSameUntilThresholdRound,
    DegenerateRound,
    EventToTimeout,
)


class Event(Enum):
    """AbciApp Events"""

    FAILED = "failed"
    DONE = "done"


class SynchronizedData(BaseSynchronizedData):
    """
    Class to represent the synchronized data.

    This data is replicated by the tendermint application.
    """


class FetchDexBalancesRound(CollectSameUntilThresholdRound):
    """FetchDexBalancesRound"""

    payload_class = FetchDexBalancesPayload
    payload_attribute = "dex_balances"
    synchronized_data_class = SynchronizedData

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        if not self.threshold_reached:
            return None
        if json.loads(self.most_voted_payload) is None:
            return self.synchronized_data, Event.FAILED
        state = self.synchronized_data.update(
            synchronized_data_class=self.synchronized_data_class, **{self.payload_attribute: self.most_voted_payload}
        )
        return state, Event.DONE


class FetchDexMarketsRound(CollectSameUntilThresholdRound):
    """FetchDexMarketsRound"""

    payload_class = FetchDexMarketsPayload
    payload_attribute = "dex_markets"
    synchronized_data_class = SynchronizedData

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        if not self.threshold_reached:
            return None
        if json.loads(self.most_voted_payload) is None:
            return self.synchronized_data, Event.FAILED
        state = self.synchronized_data.update(
            synchronized_data_class=self.synchronized_data_class, **{self.payload_attribute: self.most_voted_payload}
        )
        return state, Event.DONE


class FetchDexOrdersRound(CollectSameUntilThresholdRound):
    """FetchDexOrdersRound"""

    payload_class = FetchDexOrdersPayload
    payload_attribute = "dex_orders"
    synchronized_data_class = SynchronizedData

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        if not self.threshold_reached:
            return None

        state = self.synchronized_data.update(
            synchronized_data_class=self.synchronized_data_class, **{self.payload_attribute: self.most_voted_payload}
        )
        return state, Event.DONE


class FetchDexPositionsRound(CollectSameUntilThresholdRound):
    """FetchDexPositionsRound"""

    payload_class = FetchDexPositionsPayload
    payload_attribute = "dex_positions"
    synchronized_data_class = SynchronizedData

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        if not self.threshold_reached:
            return None
        state = self.synchronized_data.update(
            synchronized_data_class=self.synchronized_data_class, **{self.payload_attribute: self.most_voted_payload}
        )
        return state, Event.DONE


class FetchDexTickersRound(CollectSameUntilThresholdRound):
    """FetchDexTickersRound"""

    payload_class = FetchDexTickersPayload
    payload_attribute = "dex_tickers"
    synchronized_data_class = SynchronizedData

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        if not self.threshold_reached:
            return None
        state = self.synchronized_data.update(
            synchronized_data_class=self.synchronized_data_class, **{self.payload_attribute: self.most_voted_payload}
        )
        return state, Event.DONE


class FailedDexRound(DegenerateRound):
    """FailedDexRound"""


class RetrievedDexDataRound(DegenerateRound):
    """RetrievedDexDataRound"""


class DexDataRetrievalAbciApp(AbciApp[Event]):
    """DexDataRetrievalAbciApp"""

    initial_round_cls: AppState = FetchDexMarketsRound
    initial_states: Set[AppState] = {FetchDexMarketsRound}
    transition_function: AbciAppTransitionFunction = {
        FetchDexBalancesRound: {
            Event.DONE: FetchDexPositionsRound,
            Event.FAILED: FailedDexRound,
        },
        FetchDexMarketsRound: {
            Event.DONE: FetchDexTickersRound,
            Event.FAILED: FailedDexRound,
        },
        FetchDexTickersRound: {
            Event.DONE: FetchDexBalancesRound,
            Event.FAILED: FailedDexRound,
        },
        FetchDexOrdersRound: {
            Event.DONE: RetrievedDexDataRound,
            Event.FAILED: FailedDexRound,
        },
        FetchDexPositionsRound: {
            Event.DONE: FetchDexOrdersRound,
            Event.FAILED: FailedDexRound,
        },
        RetrievedDexDataRound: {},
        FailedDexRound: {},
    }
    final_states: Set[AppState] = {RetrievedDexDataRound, FailedDexRound}
    event_to_timeout: EventToTimeout = {}
    cross_period_persisted_keys: Set[str] = []
    db_pre_conditions: Dict[AppState, Set[str]] = {
        FetchDexMarketsRound: set({}),
    }
    db_post_conditions: Dict[AppState, Set[str]] = {
        RetrievedDexDataRound: {
            "dex_balances",
            "dex_markets",
            "dex_orders",
            "dex_positions",
            "dex_tickers",
        },
        FailedDexRound: set({}),
    }