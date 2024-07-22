"""
This module contains the support resources for the funding protocol.

It was created with protocol buffer compiler version `libprotoc 3.19.4` and aea protocol generator version `1.0.0`.
"""

from packages.eightballer.protocols.funding.message import FundingMessage
from packages.eightballer.protocols.funding.serialization import FundingSerializer

FundingMessage.serializer = FundingSerializer
