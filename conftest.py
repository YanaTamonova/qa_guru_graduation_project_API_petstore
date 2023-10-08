import json

import allure
from allure_commons.types import AttachmentType
from requests import sessions
from curlify import to_curl


def api(method, section, url, **kwargs):

    base_url = "https://petstore.swagger.io/v2/"
    new_url = base_url + section + url

    with allure.step(f"{method.upper()} {section} {url}"):
        with sessions.Session() as session:
            response = session.request(method=method, url=new_url, **kwargs)
            message = to_curl(response.request)
            allure.attach(body=message.encode("utf8"), name="Curl", attachment_type=AttachmentType.TEXT,
                          extension='txt')
            if not response.content:
                allure.attach(body=message.encode("utf8"), name="Text", attachment_type=AttachmentType.TEXT)
            else:
                allure.attach(body=json.dumps(response.json(), indent=4).encode("utf8"), name="Response Json",
                              attachment_type=AttachmentType.JSON, extension='json')
    return response
