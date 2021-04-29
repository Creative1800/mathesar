from mathesar.models import Schema
from mathesar.imports.csv import create_table_from_csv


def check_schema_response(response_schema, schema, schema_name):
    assert response_schema['id'] == schema.id
    assert response_schema['name'] == schema_name
    assert response_schema['database'] == 'mathesar_db_test_database'
    assert len(response_schema['tables']) == 1
    response_table = response_schema['tables'][0]
    assert response_table.startswith('http')
    assert '/api/v0/tables/' in response_table


def test_schema_list(engine, csv_filename, client):
    """
    Desired format:
    {
        "count": 1,
        "results": [
            {
                "id": 1,
                "name": "Libraries",
                "database": "mathesar_tables",
                "tables": [
                    "http://testserver/api/v0/tables/1/",
                ]
            }
        ]
    }
    """
    with open(csv_filename, 'rb') as csv_file:
        create_table_from_csv(
            name='Fairfax County Schema List',
            schema='Libraries',
            database_key='mathesar_db_test_database',
            csv_file=csv_file
        )
    schema = Schema.objects.get()
    response = client.get('/api/v0/schemas/')
    response_data = response.json()
    response_schema = response_data['results'][0]
    assert response.status_code == 200
    assert response_data['count'] == 1
    assert len(response_data['results']) == 1
    check_schema_response(response_schema, schema, 'Libraries')


def test_schema_detail(engine, csv_filename, client):
    """
    Desired format:
    One item in the results list in the schema list view, see above.
    """
    with open(csv_filename, 'rb') as csv_file:
        create_table_from_csv(
            name='Fairfax County Schema Detail',
            schema='Libraries',
            database_key='mathesar_db_test_database',
            csv_file=csv_file
        )
    schema = Schema.objects.get()
    response = client.get(f'/api/v0/schemas/{schema.id}/')
    response_schema = response.json()
    assert response.status_code == 200
    check_schema_response(response_schema, schema, 'Libraries')
