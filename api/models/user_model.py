from tortoise import fields
from tortoise.models import Model
from passlib.hash import bcrypt

class User(Model):
    id = fields.IntField(pk = True)
    username = fields.CharField(50, unique = True)
    password_hash = fields.CharField(128)

    class Meta:
        table = "user"

    def __str__(self):
        return self.username

    @classmethod
    async def get_user(cls, username):
        return cls.get(username = username)

    def verify_password(self, password):
        return bcrypt.verify(password, self.password_hash)
