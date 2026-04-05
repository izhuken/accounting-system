from dataclasses import dataclass, field
from os import path

from appdirs import user_data_dir


@dataclass
class _ApplicationConfig:
    is_dev: bool = field(default=True)
    app_name: str = field(default="as-admin")
    secret_key: str = field(default=b"CPmZz-zW8vxIJEAAW7swJTJT_Hjjwt25KjOvCU2fCcw=")
    data_dir: str = field(default=path.join(user_data_dir(), "as-admin"))
    db_url: str = field(default="")
    db_path: str = field(default="")

    def __post_init__(self) -> None:
        self.db_path = path.join(self.data_dir, "admin.db")
        self.db_url = f"sqlite:///{self.db_path}"


Config = _ApplicationConfig()
