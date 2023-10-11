from allure_commons.types import Severity
from conftest import api
from random import choice, randrange
from utils import get_file
from jsonschema.validators import validate
import allure

pytestmark = [
    allure.label('layer', 'API test'),
    allure.label('owner', 'ytamonova'),
    allure.tag('API')
]

section = 'pet'
pet_id = randrange(0, 10 ^ 4)


@allure.title('Adding a new pet')
@allure.severity(Severity.CRITICAL)
@allure.feature('Pet')
def test_add_new_pet():
    json_body = {
        "id": pet_id,
        "category": {
            "id": 1,
            "name": "dogs"
        },
        "name": "Doggie",
        "photoUrls": [
            get_file.image('Dog.jpg')
        ],
        "tags": [
            {
                "id": 1,
                "name": "Tag"
            }
        ],
        "status": "available"
    }

    response = api(method='post', section=section, url='', json=json_body)

    validate(instance=response.json(), schema=get_file.schema(section, 'post_pet_schema.json'))
    assert response.status_code == 200
    assert response.json()['id'] == pet_id


@allure.title('Finding pets by status')
@allure.severity(Severity.CRITICAL)
@allure.feature('Pet')
def test_get_pet_by_status():
    statuses = ['pending', 'sold', 'available']
    status = choice(statuses)
    response = api(method='get', section=section, url=f'/findByStatus?status={status}')

    validate(instance=response.json()[0], schema=get_file.schema(section, 'get_pet_by_status_schema.json'))
    assert response.status_code == 200
    assert response.json()[0]['status'] == status


@allure.title('Update info about a pet')
@allure.severity(Severity.CRITICAL)
@allure.feature('Pet')
def test_update_pet():
    statuses = ['pending', 'sold', 'available']
    status = choice(statuses)

    json_body = {
        "id": pet_id,
        "category": {
            "id": 1,
            "name": "dogs"
        },
        "name": "Doggie",
        "photoUrls": [
            get_file.image('Dog.jpg')
        ],
        "tags": [
            {
                "id": 1,
                "name": "Tag"
            }
        ],
        "status": status
    }

    response = api(method='put', section=section, url='', json=json_body)

    validate(instance=response.json(), schema=get_file.schema(section, 'put_pet_schema.json'))
    assert response.status_code == 200
    assert response.json()['id'] == pet_id
    assert response.json()['status'] == status


@allure.title('Delete a pet')
@allure.severity(Severity.CRITICAL)
@allure.feature('Pet')
def test_delete_pet():
    response = api(method='delete', section=section, url=f'/{pet_id}')

    validate(instance=response.json(), schema=get_file.schema(section, 'delete_pet_id_schema.json'))
    assert response.status_code == 200
    assert len(response.json()) == 3
