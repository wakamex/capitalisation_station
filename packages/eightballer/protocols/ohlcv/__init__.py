# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2022 eightballer
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

"""
This module contains the support resources for the ohlcv protocol.

It was created with protocol buffer compiler version `libprotoc 3.6.1` and aea protocol generator version `1.0.0`.
"""

from aea.configurations.data_types import PublicId

from packages.eightballer.protocols.ohlcv.message import OhlcvMessage
from packages.eightballer.protocols.ohlcv.serialization import OhlcvSerializer

OhlcvMessage.serializer = OhlcvSerializer

PUBLIC_ID = PublicId.from_str("eightballer/ohlcv:0.1.0")