import string
import secrets
import uuid


def generate_secure_password(length: int, use_upper: bool, use_digits: bool, use_symbols: bool) -> str:
    # 1. Start with the "Always included" (lowercase)
    pool = string.ascii_lowercase

    # 2. Add to pool based on user choice
    if use_upper:
        pool += string.ascii_uppercase
    if use_digits:
        pool += string.digits
    if use_symbols:
        pool += "!@#$%^&*"

    # 3. Filter the pool
    exclude = set("lI1O0o")
    clean_pool = "".join(c for c in pool if c not in exclude)

    # 4. Generate and Validate
    while True:
        password = "".join(secrets.choice(clean_pool) for _ in range(length))

        # We only validate the things the user actually wanted
        check_upper = (any(c.isupper() for c in password) if use_upper else True)
        check_digit = (any(c.isdigit() for c in password) if use_digits else True)
        check_symbol = (any(c in "!@#$%^&*" for c in password) if use_symbols else True)

        if check_upper and check_digit and check_symbol:
            return f"{password}-{str(uuid.uuid4())[:8]}"