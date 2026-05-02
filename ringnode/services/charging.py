# RNG-SAST-006: SSRF via urllib on caller URL.
from urllib.request import urlopen


def call_charging_gateway(url: str, body: bytes) -> int:
    resp = urlopen(url, data=body, timeout=5)
    return resp.status
