# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from endpoints.apis.products_api_base import BaseProductsApi
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
from pydantic import StrictStr
from typing import Any, List
from endpoints.models.create_product import CreateProduct
from endpoints.models.product import Product
from endpoints.models.update_product import UpdateProduct
from endpoints.models.validation_error import ValidationError


router = APIRouter()

ns_pkg = endpoints.endpoints
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/api/products",
    responses={
        200: {"model": Product, "description": "Товар создан"},
        422: {"model": ValidationError, "description": "Ошибка валидации"},
    },
    tags=["Products"],
    summary="Создать новый товар",
    response_model_by_alias=True,
)
async def create_product(
    create_product: CreateProduct = Body(None, description=""),
) -> Product:
    if not BaseProductsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseProductsApi.subclasses[0]().create_product(create_product)


@router.delete(
    "/api/products/{id}",
    responses={
        200: {"model": Product, "description": "Товар удалён"},
        404: {"description": "Товар не найден"},
        422: {"model": ValidationError, "description": "Ошибка валидации"},
    },
    tags=["Products"],
    summary="Удалить товар по ID",
    response_model_by_alias=True,
)
async def delete_product(
    id: StrictStr = Path(..., description=""),
) -> Product:
    if not BaseProductsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseProductsApi.subclasses[0]().delete_product(id)


@router.put(
    "/api/products",
    responses={
        200: {"model": Product, "description": "Товар обновлён"},
        404: {"description": "Товар не найден"},
        422: {"model": ValidationError, "description": "Ошибка валидации"},
    },
    tags=["Products"],
    summary="Редактировать существующий товар",
    response_model_by_alias=True,
)
async def edit_product(
    update_product: UpdateProduct = Body(None, description=""),
) -> Product:
    if not BaseProductsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseProductsApi.subclasses[0]().edit_product(update_product)


@router.get(
    "/api/products/{id}",
    responses={
        200: {"model": Product, "description": "Товар найден"},
        404: {"description": "Товар не найден"},
        422: {"model": ValidationError, "description": "Ошибка валидации"},
    },
    tags=["Products"],
    summary="Получить товар по ID",
    response_model_by_alias=True,
)
async def get_product(
    id: StrictStr = Path(..., description=""),
) -> Product:
    if not BaseProductsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseProductsApi.subclasses[0]().get_product(id)


@router.get(
    "/api/products",
    responses={
        200: {"model": List[Product], "description": "Успешный ответ"},
    },
    tags=["Products"],
    summary="Получить список всех товаров",
    response_model_by_alias=True,
)
async def get_products(
) -> List[Product]:
    if not BaseProductsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseProductsApi.subclasses[0]().get_products()
