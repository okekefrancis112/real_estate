# import uuid

# def generate_ref_code():
#     code = str(uuid.uuid4()).replace("-", "")[:12]
#     return code

import random

def generate_ref_code():
    code = random.randint(100000, 1000000)
    return code