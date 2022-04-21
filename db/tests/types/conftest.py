import pytest
from sqlalchemy import MetaData, Table
from db.tables.operations.select import get_oid_from_table
from db.types.base import MathesarCustomType
from db.columns.operations.alter import alter_column_type


@pytest.fixture
def uris_table_obj(engine_with_uris, uris_table_name):
    engine, schema = engine_with_uris
    metadata = MetaData(bind=engine)
    table = Table(uris_table_name, metadata, schema=schema, autoload_with=engine)
    # Cast "uri" column from string to URI
    with engine.begin() as conn:
        uri_column_name = "uri"
        uri_type = MathesarCustomType.URI
        alter_column_type(
            get_oid_from_table(table.name, schema, engine),
            uri_column_name,
            engine,
            conn,
            uri_type,
        )
    yield table, engine


@pytest.fixture
def roster_table_obj(engine_with_roster, roster_table_name):
    engine, schema = engine_with_roster
    metadata = MetaData(bind=engine)
    table = Table(roster_table_name, metadata, schema=schema, autoload_with=engine)
    # Cast "Teacher Email" column from string to Email
    with engine.begin() as conn:
        email_column_name = "Teacher Email"
        email_type = MathesarCustomType.EMAIL
        alter_column_type(
            get_oid_from_table(table.name, schema, engine),
            email_column_name,
            engine,
            conn,
            email_type,
        )
    yield table, engine
