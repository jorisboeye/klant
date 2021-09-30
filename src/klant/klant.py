"""Main module."""
import os
from pathlib import Path
from typing import Union

import attr
import httpx

def make_url(*segments, base_url: str = ""):
    if base_url:
        segments = (base_url,) + segments
    else:
        segments = (os.environ.get("KLANT-BASE-URL"),) + segments
    return "/".join(segments)

def load_configuration(configuration: Union[str, dict]) -> dict:
    if isinstance(configuration, dict):
        return dict
    elif isinstance(configuration, str):
        if Path(configuration).isfile():
            raise NotImplementedError
        else:
            return {
                "api": {"name": "api", "base": configuration},
                ""
            }
    else:
        raise ValueError

@attr.s
class Klant:
    configuration = attr.ib(converter=load_configuration)
    

    def get(*segments, api=""):

