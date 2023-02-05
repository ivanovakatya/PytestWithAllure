import pytest
from tortoise import Tortoise
from tortoise.contrib.test import finalizer, initializer
from api.models.user_model import User

@pytest.mark.asyncio
@pytest.fixture(scope='class')
async def tortoise_init():
    await Tortoise.init(db_url='sqlite://:memory:', modules={'models': [User]})
    await Tortoise.generate_schemas()
    initializer(['api.models'])

@pytest.mark.asyncio
@pytest.mark.usefixtures('tortoise_init')
class TestUserModel:

    test_user = User(username = 'Katya', password = 'password123')

    @pytest.mark.asyncio
    async def test_insert(self):
        await self.test_user.save()
    
    @pytest.mark.asyncio
    async def test_query(self):
        queried_user = await User.filter(id=self.test_user.id)
        assert queried_user.username == 'Katya'
        assert queried_user.password == 'password123'
