import os
import json


def schema(section, schema_name):
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resourses', 'schemas', section, schema_name)) \
            as file:
        schema = json.loads(file.read())

    return schema


def image(image_name):
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resourses', 'images', image_name)
