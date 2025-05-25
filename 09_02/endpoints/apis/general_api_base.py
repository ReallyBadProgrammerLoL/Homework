# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from endpoints.models.read_root200_response import ReadRoot200Response


class BaseGeneralApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseGeneralApi.subclasses = BaseGeneralApi.subclasses + (cls,)
    async def read_root(
        self,
    ) -> ReadRoot200Response:
        ...
