from typing import Any

from bson import ObjectId
from pydantic import GetCoreSchemaHandler, GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import CoreSchema, core_schema

"""
MongoDB는 데이터를 BSON 타입으로 저장한다.
FastAPI는 데이터를 JSON 타입으로 인코딩/디코딩한다.
BSON은 JSON보다 더 많은 데이터 타입을 추가적으로 지원한다. 이 데이터 타입 중 ObjectId은 JSON으로 바로 인코딩되지 않는다.
따라서 ObjectId를 _id로 저장하기 전에 문자열로 변환시켜줘야 한다.
"""


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid Ojectid")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        _source_type: Any,
        _handler: GetCoreSchemaHandler,
    ) -> CoreSchema:
        return core_schema.no_info_plain_validator_function(
            function=cls.validate,
            serialization=core_schema.to_string_ser_schema(),
        )

    @classmethod
    def __get_pydantic_json_schema__(
        cls, _core_schema: CoreSchema, handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:
        return handler(core_schema.str_schema())
