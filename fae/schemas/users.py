import datetime
import typing
import validators
from pydantic import BaseModel, Field, validator, EmailStr


class UserSocial(BaseModel):
    github: typing.Optional[str]
    website: typing.Optional[str]
    youtube: typing.Optional[str]
    discord: typing.Optional[str]
    twitter: typing.Optional[str]
    facebook: typing.Optional[str]
    vk: typing.Optional[str]
    reddit: typing.Optional[str]

    @validator("website")
    def validate_website(cls, v):
        if v is not None:
            if not validators.url(v):
                raise ValueError("An invalid website was provided")
        return v


class UserInResponse(BaseModel):
    id: int
    created_at: datetime.datetime
    username: str
    email: EmailStr
    social: UserSocial


class UserInRequest(BaseModel):
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now, const=True)
    username: str = Field(min_length=2, max_length=32)
    email: EmailStr
    social: UserSocial = {}


class UserInRequestEdit(BaseModel):
    username: typing.Optional[str] = Field(min_length=2, max_length=32)
    email: typing.Optional[EmailStr]
    social: UserSocial = {}