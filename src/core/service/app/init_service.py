from os import getenv
from pathlib import Path
from uuid import UUID

from alembic import command
from alembic.config import Config as AlembicConfig
from alembic.util.exc import CommandError

from core.config import Config
from core.domain.entities.user import User
from core.domain.value_objects.user import UserId, UserPassword, UserStatus
from core.service.exc import InitialException

from .user_service import UserService


class InitDBService:
    async def init_db(self):
        self.__create_db()
        self.__migrate_db()
        await self.__bootstrap()

    def __create_db(self):
        db_path = Path(Config.db_path)

        if not db_path.exists():
            db_path.parent.mkdir(parents=True, exist_ok=True)
            db_path.touch()

    def __migrate_db(self) -> None:
        try:
            alembic_config = AlembicConfig()
            alembic_config.set_main_option(
                "script_location",
                str(
                    Path(__file__).parent.parent.parent.parent
                    / "core"
                    / "infrastructure"
                    / "sqlite"
                    / "migrations"
                ),
            )
            alembic_config.set_main_option("sqlalchemy.url", Config.sync_db_url)
            command.upgrade(alembic_config, "head")
        except CommandError:
            raise InitialException

    async def __bootstrap(self):
        user_service = UserService()
        user = User(
            UserId(UUID("1f2b6af6-c386-4d88-ac85-0b2407f88f43")),
            "Балакирев Я. И.",
            UserPassword(getenv("ADMIN_PASSWORD")),
            UserStatus.LOGGED_IN,
        )

        if not await user_service.exists(user):
            await user_service.save(user)
