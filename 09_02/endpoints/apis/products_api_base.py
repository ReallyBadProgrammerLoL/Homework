# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import StrictStr
from typing import Any, List
from endpoints.models.create_product import CreateProduct
from endpoints.models.product import Product
from endpoints.models.update_product import UpdateProduct
from endpoints.models.validation_error import ValidationError


class BaseProductsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseProductsApi.subclasses = BaseProductsApi.subclasses + (cls,)
    async def create_product(
        self,
        create_product: CreateProduct,
    ) -> Product:
        ...


    async def delete_product(
        self,
        id: StrictStr,
    ) -> Product:
        ...


    async def edit_product(
        self,
        update_product: UpdateProduct,
    ) -> Product:
        ...


    async def get_product(
        self,
        id: StrictStr,
    ) -> Product:
        ...


    async def get_products(
        self,
    ) -> List[Product]:
        ...
