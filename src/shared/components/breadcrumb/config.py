from dataclasses import dataclass, field


@dataclass
class BreadcrumbsConfig:
    location: str
    link: str | None = field(default=None)
