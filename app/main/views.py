from . import main
from .forms import CommentForm,UpdateProfile,FormBlog
from ..requests import get_quote
from ..models import Quotes,Comment,Blog,User
from flask import render_template,redirect,url_for,abort,request,flash
from flask_login import login_required,current_user
from .. import db,photos

@main.route('/')
def index():
    """
     View root page function that returns the index page and its data
    """
    title = 'Welcome to the JBlvck_Blog home of the best Information in the net'
    blog = Blog.query.order_by(Blog.date_created).all()
    quote=get_quote()
    return render_template('index.html', title=title, quote =quote,blog=blog )


@main.route('/createblog', methods=['GET', 'POST'])
@login_required
def new_blog():
    form = FormBlog()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        new_blog= Blog(title=title, content=content,user_id=current_user.id)
        new_blog.save_blog()
        flash('Your blog has been Created','Success')
        return redirect(url_for('main.index'))
    return render_template('blog.html', title='New Post',form = form)

@main.route('/blog/<blog_id>', methods=['GET', 'POST'])
def blog(blog_id):
    blog=Blog.query.filter_by(id=blog_id).first()
    print(blog)
    return render_template('blogcont.html',blog=blog)


@main.route('/blog/<blog_id>/update',methods=['GET', 'POST'])
@login_required
def update_blog(blog_id):
    blog=Blog.query.filter_by(id=blog_id).first()
    if blog.user != current_user:
        abort(403)

    form=FormBlog()
    if form.validate_on_submit():
        blog.title=form.title.data
        blog.content=form.content.data
        db.session.commit()
        flash('Your Blog has been Updated','Success')
        return redirect(url_for('.blog',blog_id=blog.id) )
    elif request.method=='GET':
        form.title.data=blog.title
        form.content.data=blog.content
        
    return render_template('blog.html', form = form,title='Update Post')

@main.route('/blog/<blog_id>/delete',methods=['GET', 'POST'])
@login_required
def delete_blog(blog_id):
    blog=Blog.query.filter_by(id=blog_id).first()
    if blog.user != current_user:
        abort(403)
    db.session.delete(blog)
    db.session.commit()
    flash('Your blog has been deleted successfully!','success')
    return redirect(url_for('main.index'))

@main.route('/comments/<blog_id>', methods=['GET', 'POST'])
@login_required
def comments(blog_id):
    comments = Comment.query.filter_by(blog_id=blog_id).all()
    blog = Blog.query.get(blog_id)
    form = CommentForm()
    if blog is None:
        abort(404)
    if form.validate_on_submit():
            comment = Comment(
            content=form.content.data,
            blog_id=blog_id,
            user_id=current_user.id
        )
            db.session.add(comment)
            db.session.commit()
            form.content.data = ''
            flash('Your comment has been posted successfully!','success')
    return render_template('comments.html',blogs= blog, comment=comments, form = form)

@main.route('/comment/<comment_id>', methods=['POST','GET'])
def delete_comment(comment_id):
    comment = Comment.query.filter_by(id = comment_id).first()
    blog_id = comment.blog_id
    db.session.delete(comment)
    db.session.commit()
    flash('Your comment has been deleted successfully!','success')
    return redirect(url_for('.blog',blog_id = blog_id))





@main.route('/user/<name>/update/pic',methods= ['POST'])
@login_required
def update_pic(name):
    user = User.query.filter_by(username = name).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',name=name))

@main.route('/user/<name>/updateprofile', methods = ['POST','GET'])
@login_required
def updateprofile(name):
    form = UpdateProfile()
    user = User.query.filter_by(username = name).first()
    if user == None:
        abort(404)
    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()
      
        return redirect(url_for('.profile',name = name))
    return render_template('profile/update.html',form =form) 
@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username = name).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)