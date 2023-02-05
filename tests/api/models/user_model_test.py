import pytest
from tortoise import Tortoise
from api.models.user_model import User

@pytest.fixture(scope='class')
def tortoise_init():
    Tortoise.init(db_url="sqlite://:memory:", modules={"models": [User]})
    Tortoise.generate_schemas()

@pytest.mark.usefixtures('tortoise_init')
class TestUserModel:

    def test_insert(self):
        print('test user')

    def test_query(self):
        print('test query')