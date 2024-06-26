#!/usr/bin/env python3
"""
Insert a document in python
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    insert a document into collection
    """
    data = mongo_collection.insert_one(kwargs)
    return data.inserted_id
