from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField
from wtforms.validators import InputRequired,Length,EqualTo


class FormBlog(FlaskForm):
  title = StringField('Blog Title', validators=[InputRequired(), Length(1, 64)])
  author = StringField('Author : ',)
  category = RadioField('Blog Category :', choices = [('Health & Fitness', 'Health & Fitness'),  ('Entertinment', ' Entertainment'), ('Technology', 'Technology')], validators = [InputRequired()])
  content = TextAreaField('Your Blog', validators=[InputRequired()])
  submit = SubmitField('Post')
  
  
class CommentForm(FlaskForm):
  content = TextAreaField('Leave a comment ...', validators=[InputRequired()])
  submit = SubmitField('Comment')
  
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')
 