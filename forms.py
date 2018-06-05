# forms.py

from models import Album, Artist, User
#from wtforms.validators import Required
from wtforms import Form, StringField, SelectField, validators, PasswordField, BooleanField, Required

#from wtforms import Form, StringField, SelectField, PasswordField, validators, BooleanField
#from wtforms import StringField, BooleanField, PasswordField, TextAreaField, validators
#from wtforms.validators import Required

class RegistrationForm(Form):
    user_name = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    user_password = PasswordField('Enter Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.Required()])

   # A login Form


class LoginForm(Form):
    user_name = StringField('Username', validators=[Required()])
    user_password = PasswordField('Password', validators=[Required()])
    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None


    
    #def validate(self):

     
        #rv = Form.validate(self)
        #if not rv:
            #return False

        #user = User.query.filter_by(
            #user_name=self.user_name.data).first()
        #if user is None:
            #self.user_name.errors.append('Unknown username')
            #return False

        #if not user.check_password(self.user_password.data):
            #self.user_password.errors.append('Invalid password')
            #return False

        #self.user = user
        #return True
# Registration form to create a users


# A form to enable searching music in the data
class MusicSearchForm(Form):
    choices = [('Artist', 'Artist'),
               ('Album', 'Album'),
               ('Publisher', 'Publisher')]
    select = SelectField('Search for music:', choices=choices)
    search = StringField('')

# A form to create/Add a new Album to the database

class AlbumForm(Form):
    media_types = [('Digital', 'Digital'),
                   ('CD', 'CD'),
                   ('Cassette Tape', 'Cassette Tape')
                   ]
    artist = StringField('Artist')
    title = StringField('Title')
    release_date = StringField('Release Date')
    publisher = StringField('Publisher')
    media_type = SelectField('Media', choices=media_types)