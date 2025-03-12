from hashlib import sha256
from typing import Any

def my_hash(data: Any) -> str:
    return sha256(str(data).encode()).hexdigest()
