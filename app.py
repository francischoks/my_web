from flask import Flask, render_template, redirect, url_for, flash

import models
import forms


app = Flask(__name__)
app.secret_key = 'djghgavbnQ7YHEQGHSVAFJHFAVZGfadv'


@app.route('/')
def index():
	posts = models.Post.select().limit(100).order_by(models.Post.created_at.desc())
	return render_template('index.html', posts=posts)


@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/contact')
def contact():
	return render_template('contact.html')


@app.route('/post/<int:post_id>')
def post(post_id):
	post = models.Post.select().where(models.Post.id == post_id)
	return render_template('post.html', posts=post)


@app.route('/addpost', methods=('GET', 'POST'))
def addpost():
	form = forms.PostForm()
	if form.validate_on_submit():
		models.Post.create(
				title=form.title.data,
				subtitle=form.subtitle.data,
				author=form.author.data,
				content=form.content.data
			)
		flash('Blog posted! Thanks!', 'success')
		return redirect(url_for('index'))
	return render_template('addpost.html', form=form)


if __name__ == '__main__':
	models.initialise()
	app.run(debug=True)