from tortoise import fields
from tortoise.models import Model


class Book(Model):
    id = fields.IntField(pk=True)
    author = fields.ForeignKeyField('models.User', on_delete=fields.CASCADE, related_name="books")
    title = fields.CharField(max_length=150)
    description = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
