# generated by datamodel-codegen:
#   filename:  storage.json

from __future__ import annotations

from typing import Union

from pydantic import BaseModel, Extra


class Metadatum(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class Royalty(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class Swap(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class Storage(BaseModel):
    curate: str
    genesis: str
    hdao: str
    locked: bool
    manager: str
    metadata: Union[int, Metadatum]
    objkt: str
    objkt_id: str
    royalties: Union[int, Royalty]
    size: str
    swap_id: str
    swaps: Union[int, Swap]