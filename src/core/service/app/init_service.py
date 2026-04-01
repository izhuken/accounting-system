from pathlib import Path

from alembic import command
from alembic.config import Config as AlembicConfig
from alembic.util.exc import CommandError

from core.config import Config
from core.service.exceptions import InitialError


class InitDBService:
    def init_db(self):
        self.__create_db()
        self.__migrate_db()

    def __create_db(self):
        db_path = Path(Config.db_path)

        if not db_path.exists():
            db_path.parent.mkdir(parents=True, exist_ok=True)
            db_path.touch()

    def __migrate_db(self):
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
            alembic_config.set_main_option("sqlalchemy.url", Config.db_url)
            command.upgrade(alembic_config, "head")
        except CommandError:
            raise InitialError
