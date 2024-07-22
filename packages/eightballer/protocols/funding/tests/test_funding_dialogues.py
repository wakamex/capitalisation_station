# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2024 Mihai Cosma
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

"""Test dialogues module for funding protocol."""

import pytest

# pylint: disable=too-many-statements,too-many-locals,no-member,too-few-public-methods,redefined-builtin
# pylint: disable=R1735
from aea.test_tools.test_protocol import BaseProtocolDialoguesTestCase

from packages.eightballer.protocols.funding.dialogues import FundingDialogue, FundingDialogues
from packages.eightballer.protocols.funding.message import FundingMessage


@pytest.mark.skip("Not implemented yet")
class TestDialoguesFunding(BaseProtocolDialoguesTestCase):
    """Test for the 'funding' protocol dialogues."""

    MESSAGE_CLASS = FundingMessage

    DIALOGUE_CLASS = FundingDialogue

    DIALOGUES_CLASS = FundingDialogues

    ROLE_FOR_THE_FIRST_MESSAGE = FundingDialogue.Role.PUBLISHER  # CHECK

    def make_message_content(self) -> dict:
        """Make a dict with message contruction content for dialogues.create."""
        return dict(
            performative=FundingMessage.Performative.SUBSCRIBE,
            exchange_id="some str",
            symbol="some str",
            precision="some str",
            interval=12,
        )
