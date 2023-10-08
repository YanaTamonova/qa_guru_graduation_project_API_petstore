from conftest import api
from random import randrange
from utils import get_file
from jsonschema.validators import validate
import allure
from allure_commons.types import Severity

pytestmark = [
    allure.label('layer', 'API test'),
    allure.label('owner', 'ytamonova'),
    allure.tag('API')
]


section = 'store'
order_id = randrange(1, 11)


@allure.title('Creating a new order')
@allure.severity(Severity.CRITICAL)
@allure.feature('Store')
def test_create_order():

    pet_id = randrange(1, 11)
    quantity = randrange(1, 11)

    json_body = {
      "id": order_id,
      "petId": pet_id,
      "quantity": quantity,
      "shipDate": "2023-10-07T18:37:16.066Z",
      "status": "placed",
      "complete": True
    }

    response = api(method='post', section=section, url='/order', json=json_body)

    assert response.status_code == 200
    assert len(response.json()) == 6
    assert response.json()['id'] == order_id
    assert response.json()['petId'] == pet_id
    assert response.json()['quantity'] == quantity
    validate(instance=response.json(), schema=get_file.schema(section, 'order_by_id_schema.json'))


@allure.title('Search for an order')
@allure.severity(Severity.CRITICAL)
@allure.feature('Store')
def test_get_order_by_id():
    response = api(method='get', section=section, url=f'/order/{order_id}')

    assert response.status_code == 200
    assert len(response.json()) == 6
    assert response.json()['id'] == order_id
    validate(instance=response.json(), schema=get_file.schema(section, 'order_by_id_schema.json'))


@allure.title('Deleting an order')
@allure.severity(Severity.CRITICAL)
@allure.feature('Store')
def test_delete_order():
    response = api(method='delete', section=section, url=f'/order/{order_id}')

    validate(instance=response.json(), schema=get_file.schema(section, 'delete_order_schema.json'))
    assert response.status_code == 200
    assert response.json()['message'] == str(order_id)
