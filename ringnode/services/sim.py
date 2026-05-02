# RNG-SAST-007: os.system with MSISDN.
import os


def push_ota(msisdn: str, profile: str) -> int:
    return os.system(f"/opt/ringnode/bin/sim-ota --msisdn {msisdn} --profile {profile}")
