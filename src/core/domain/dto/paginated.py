from dataclasses import dataclass


@dataclass
class Paginated[T]:
    data: list[T]
    page: int
    count: int
    has_next: bool
    has_previous: bool
