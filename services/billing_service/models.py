from pydantic import BaseModel, Field
from sqlmodel import SQLModel


class Account(SQLModel, table=True):
    user_id: int = Field(primary_key=True)
    balance: float = Field(default=0, ge=0)


class AccountCreate(BaseModel):
    user_id: int = Field(..., ge=1)


class AccountRead(BaseModel):
    user_id: int
    balance: float


class PaymentRequest(BaseModel):
    amount: float = Field(..., gt=0)


class PaymentResult(BaseModel):
    user_id: int
    balance: float
    withdrawn: bool
    message: str
