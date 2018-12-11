from flask_wtf import Form 
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

from models import Post


class PostForm(Form):
	title = StringField(
			'Blog Title',
			validators=[DataRequired()]
		)
	subtitle = StringField(
			'Blog Subtitle',
			validators=[DataRequired()]
		)
	author = StringField(
			'Blog Author',
			validators=[DataRequired()]
		)
	content = TextAreaField(
			'Blog Content',
			validators=[DataRequired()]
		)





