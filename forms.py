from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# WTform for registering new users
class RegisterForm(FlaskForm):
    users_email = EmailField("Email", validators=[DataRequired()])
    users_password = PasswordField("Password", validators=[DataRequired()])
    users_name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("SIGN ME UP!")

# WTform for letting the user log in
class LoginForm(FlaskForm):
    users_email = EmailField("Email", validators=[DataRequired()])
    users_password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("LET ME IN!")


class CommentForm(FlaskForm):
    body = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
