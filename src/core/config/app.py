from dataclasses import dataclass, field
from os import getenv, path


@dataclass
class _ApplicationConfig:
    secret_key: str = field(default=b"CPmZz-zW8vxIJEAAW7swJTJT_Hjjwt25KjOvCU2fCcw=")
    is_dev_mode: bool = field(default=False)

    db_url: str = field(default="sqlite:///storage/data/admin.db")
    db_path: str = field(
        default=path.join(getenv("FLET_APP_STORAGE_DATA", "storage/data"), "admin.db")
    )

    def __post_init__(self) -> None:
        self.db_url = f"sqlite:///{self.db_path}"


Config = _ApplicationConfig()
