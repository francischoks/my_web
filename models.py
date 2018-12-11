import datetime

from peewee import *

db = SqliteDatabase('diwa_blog.db')
# db = PostgresqlDatabase(database='diwa', user='postgres', password='nokutenda', host='localhost')

class Post(Model):
	title = CharField(max_length=255)
	subtitle = CharField(max_length=255)
	author = CharField(max_length=100)
	content = TextField()
	created_at = DateTimeField(default=datetime.datetime.now)

	class Meta:
		database = db
		order_by = ('-created_at',)

	def __str__(self):
		return self.title


def initialise():
	db.connect()
	db.create_tables([Post], safe=True)
	db.close()