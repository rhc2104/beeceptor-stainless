# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["User"]


class User(BaseModel):
    id: int

    email: str

    name: str
