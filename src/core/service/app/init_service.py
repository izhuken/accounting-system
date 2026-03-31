from pathlib import Path

from alembic import command
from alembic.config import Config as AlembicConfig
from alembic.util import CommandError

from core.config import Config
from core.service.exceptions.initial_error import InitialError


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
            alembic_cfg = AlembicConfig("assets/db/alembic.ini")
            command.upgrade(alembic_cfg, "head")
        except CommandError:
            raise InitialError
