from dataclasses import dataclass, field


@dataclass
class _ApplicationConfig:
    secret_key: str = field(default=b"CPmZz-zW8vxIJEAAW7swJTJT_Hjjwt25KjOvCU2fCcw=")
    is_dev_mode: bool = field(default=False)
    db_url: str = field(default="sqlite:///storage/data/admin.db")


Config = _ApplicationConfig()
