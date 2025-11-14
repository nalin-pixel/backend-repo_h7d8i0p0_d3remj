"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

# Example schemas (you can keep or ignore):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: EmailStr = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in EUR")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Gym website specific schemas

class Inquiry(BaseModel):
    """
    Inquiries from the website contact form
    Collection name: "inquiry"
    """
    name: str = Field(..., min_length=2, max_length=120)
    email: EmailStr
    phone: Optional[str] = Field(None, description="Contact phone number")
    message: str = Field(..., min_length=5, max_length=2000)
    interest: Optional[str] = Field(None, description="What they're interested in: membership, personal training, classes")

class GymClass(BaseModel):
    """
    Group classes offered by the gym
    Collection name: "gymclass" (lowercase of class name)
    """
    title: str
    description: Optional[str] = None
    coach: Optional[str] = None
    day: Optional[str] = Field(None, description="Day of week, e.g., Monday")
    time: Optional[str] = Field(None, description="Time string, e.g., 18:30")
    level: Optional[str] = Field(None, description="Beginner / Intermediate / Advanced")
    spots: Optional[int] = Field(None, ge=0, description="Available spots")

# Note: The Flames database viewer can use these schemas automatically.
