import random
from dataclasses import dataclass


@dataclass
class XRPConsts:
    MINIMUM_XRP = 10
    XRP_MAINNET_URL = "https://xrplcluster.com"


def get_minimum_xrp_wallet(decimal):
    return XRPConsts.MINIMUM_XRP * pow(10, decimal)


def xrp_generate_destination_tag():
    return random.randint(10000, 99999)
