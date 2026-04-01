from dataclasses import dataclass, field
from os import path

from appdirs import user_data_dir


@dataclass
class _ApplicationConfig:
    secret_key: str = field(default=b"CPmZz-zW8vxIJEAAW7swJTJT_Hjjwt25KjOvCU2fCcw=")
    is_dev_mode: bool = field(default=False)

    data_dir: str = field(default=path.join(user_data_dir(), "as-admin"))

    db_url: str = field(default="")
    db_path: str = field(default="")

    def __post_init__(self) -> None:
        self.db_path = path.join(self.data_dir, "admin.db")
        self.db_url = f"sqlite:///{self.db_path}"


Config = _ApplicationConfig()
