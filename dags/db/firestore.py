from typing import Dict, Literal, Optional
from datetime import datetime, timezone


from .config import client

from .utils import DBUtils
from google.cloud.firestore_v1.base_query import FieldFilter


class Firestore():
    """
    This wrapper is an abstraction layer between the 
    application and the database.

    It provides a consistent interface to execute database
    operations, making it simpler to use, easier to maintain
    and avoiding code duplication.

    This encapsulation enhances code robustness, scalability, 
    and accelerates development.
    """

    @staticmethod
    def scan(collection: str):
        ref = client.collection(collection)
        docs = ref.stream()
        return DBUtils.filter_empty([DBUtils.parse_doc(doc) for doc in docs])
