# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from endpoints.apis.general_api_base import BaseGeneralApi
import endpoints.endpoints

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from endpoints.models.extra_models import TokenModel  # noqa: F401
from endpoints.models.read_root200_response import ReadRoot200Response


router = APIRouter()

ns_pkg = endpoints.endpoints
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/",
    responses={
        200: {"model": ReadRoot200Response, "description": "Приветственное сообщение"},
    },
    tags=["General"],
    summary="Read Root",
    response_model_by_alias=True,
)
async def read_root(
) -> ReadRoot200Response:
    if not BaseGeneralApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseGeneralApi.subclasses[0]().read_root()
