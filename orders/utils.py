from datetime import datetime
import random

from uuid import uuid4

def generate_order_number():

    unique = uuid4().hex[:8].upper()

    return f"ORD-{unique}"