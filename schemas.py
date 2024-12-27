from pydantic import BaseModel, EmailStr, Field
from typing import Optional


# Address Schema
class AddressBase(BaseModel):
    street_address: str = Field(..., title="Street Address", max_length=255)
    landmark: Optional[str] = Field(None, title="Landmark")
    city: str = Field(..., title="City", max_length=100)
    state: str = Field(..., title="State", max_length=100)
    pincode: int = Field(..., title="Pincode")  # Enforcing valid pincode


# User Schema
class UserBase(BaseModel):
    name: str = Field(..., title="Full Name", max_length=100)
    email: EmailStr = Field(..., title="Email Address")
    mobile_no: int = Field(..., title="Mobile Number")  # Supports international format


# Full Registration Form Schema (Combining Address and User)
class RegistrationForm(BaseModel):
    name: str = Field(..., title="Full Name", max_length=100)
    email: EmailStr = Field(..., title="Email Address")
    mobile_no: int = Field(..., title="Mobile Number")
    street_address: str = Field(..., title="Street Address", max_length=255)
    landmark: Optional[str] = Field(None, title="Landmark")
    city: str = Field(..., title="City", max_length=100)
    state: str = Field(..., title="State", max_length=100)
    pincode: int = Field(..., title="Pincode")
    
    class Config:
        orm_mode = True
