from dataclasses import dataclass, field
from typing import Any, Callable

from flet import Container


@dataclass
class TableAccessor:
    header: str
    accessor: str
    on_click: Callable | None = field(default=None)
    view: Container | None = field(default=None)
    value: Callable | None = field(default=None)
    width: int | float | None = field(default=None)
    expand: bool = field(default=False)


@dataclass
class TableData:
    data: list[dict[str, Any]] = field(default_factory=list)
    has_next: bool = field(default=False)
    has_previous: bool = field(default=False)
    page: int = field(default=1)
    total_pages: int = field(default=1)

    def __init__(
        self,
        data: list[dict[str, Any]] = [],
        has_next: bool = False,
        has_previous: bool = False,
        page: int = 1,
        total_pages: int = 1,
    ):
        self.data = data
        self.has_next = has_next
        self.has_previous = has_previous
        self.page = page
        self.total_pages = total_pages
