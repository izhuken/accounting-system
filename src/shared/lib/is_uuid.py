from re import IGNORECASE, compile


def is_uuid(uuid_string: str) -> bool:
    pattern = compile(
        r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
        IGNORECASE,
    )
    return bool(pattern.match(uuid_string))
