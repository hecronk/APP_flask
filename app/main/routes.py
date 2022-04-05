from app.main import bp
from flask import render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from datetime import datetime
from app import db
from app.main.forms import PostForm, EmptyForm
from app.models.user import User
from app.models.post import Post


@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@bp.route('/feed', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@bp.route('/', methods=['GET', 'POST'])
@login_required
def feed():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=str(form.post), author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('main.feed'))
    posts = current_user.followed_posts()
    return render_template('main/feed.html', title='Home page', posts=posts, form=form)


@bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = user.posts
    form = EmptyForm()
    return render_template('main/user.html', user=user, posts=posts, form=form)


@bp.route('/follow/<username>', methods=['GET', 'POST'])
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found'.format(username))
        return redirect(url_for('main.feed'))
    current_user.follow(user=user)
    if user == current_user:
        flash('You cannot follow yourself!')
        return redirect(url_for('main.user', username=username))
    current_user.follow(user)
    db.session.commit()
    flash('You are following {} now!'.format(username))
    return redirect(url_for('main.user', username=username))


@bp.route('/unfollow/<username>', methods=['GET', 'POST'])
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found'.format(username))
        return redirect(url_for('main.feed'))
    current_user.follow(user=user)
    if user == current_user:
        flash('You cannot unfollow yourself!')
        return redirect(url_for('main.user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash('You are not following {} now!'.format(username))
    return redirect(url_for('main.user', username=username))
