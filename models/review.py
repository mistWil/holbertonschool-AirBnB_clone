#!/usr/bin/python3


from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a Review for AirBnB clone"""
    place_id = ""  # Place.id
    user_id = ""  # User.id
    text = ""
