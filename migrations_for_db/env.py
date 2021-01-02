import os
import importlib
from logging.config import fileConfig

from sqlalchemy import engine_from_config, MetaData
from sqlalchemy import pool
from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
def combine_metadata(metadata_objects):
    metadata = MetaData()
    for metadata_object in metadata_objects:
        for table in metadata_object.tables.values():
            # The aim of this line is to avoid a warning that table X already exists
            if str(table) not in list(metadata.tables.keys()):
                table.tometadata(metadata)
    return metadata

def get_metadata_of_all_models():
    # Attention: we have to set the python path to models folder so that we dont get an error
    # set PYTHONPATH=%PYTHONPATH%;D:\Projects\postgres\models
    metadata_objects = []
    for model_module in os.listdir('D:\Projects\postgres\models'):
        if model_module not in ['__init__.py', 'get_all.py', '__pycache__']:
            model_module_name = model_module[:-3]
            globals()[model_module_name] = importlib.import_module(model_module_name, package='models')
            metadata_objects.append(globals()[model_module_name].metadata)
    return metadata_objects

target_metadata = combine_metadata(get_metadata_of_all_models())

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
