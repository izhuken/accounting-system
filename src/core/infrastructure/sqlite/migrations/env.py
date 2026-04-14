import logging
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

from core.config.app import Config
from core.infrastructure.sqlite.database import Base
from core.infrastructure.sqlite.models import *  # noqa: F403

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

logger = logging.getLogger("alembic.env")

target_metadata = Base.metadata

section = config.config_ini_section
config.set_section_option(section, "DATABASE_URL", Config.sync_db_url)


def run_migrations_offline():
    """Run migrations without DB connection."""
    url = config.get_main_option("sqlalchemy.url")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
        compare_server_default=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations with DB connection."""

    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        logger.info(f"DB URL: {config.get_main_option('sqlalchemy.url')}")
        logger.info(f"Tables in metadata: {list(target_metadata.tables.keys())}")

        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True,
            render_as_batch=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
