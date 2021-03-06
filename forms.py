from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, ValidationError, BooleanField
from wtforms.validators import DataRequired, AnyOf, Length, URL
from flask_wtf import FlaskForm

import re
state_choices = [
    ('AL', 'AL'),
    ('AK', 'AK'),
    ('AZ', 'AZ'),
    ('AR', 'AR'),
    ('CA', 'CA'),
    ('CO', 'CO'),
    ('CT', 'CT'),
    ('DE', 'DE'),
    ('DC', 'DC'),
    ('FL', 'FL'),
    ('GA', 'GA'),
    ('HI', 'HI'),
    ('ID', 'ID'),
    ('IL', 'IL'),
    ('IN', 'IN'),
    ('IA', 'IA'),
    ('KS', 'KS'),
    ('KY', 'KY'),
    ('LA', 'LA'),
    ('ME', 'ME'),
    ('MT', 'MT'),
    ('NE', 'NE'),
    ('NV', 'NV'),
    ('NH', 'NH'),
    ('NJ', 'NJ'),
    ('NM', 'NM'),
    ('NY', 'NY'),
    ('NC', 'NC'),
    ('ND', 'ND'),
    ('OH', 'OH'),
    ('OK', 'OK'),
    ('OR', 'OR'),
    ('MD', 'MD'),
    ('MA', 'MA'),
    ('MI', 'MI'),
    ('MN', 'MN'),
    ('MS', 'MS'),
    ('MO', 'MO'),
    ('PA', 'PA'),
    ('RI', 'RI'),
    ('SC', 'SC'),
    ('SD', 'SD'),
    ('TN', 'TN'),
    ('TX', 'TX'),
    ('UT', 'UT'),
    ('VT', 'VT'),
    ('VA', 'VA'),
    ('WA', 'WA'),
    ('WV', 'WV'),
    ('WI', 'WI'),
    ('WY', 'WY'),
]
genres_choices = [
    ('Alternative', 'Alternative'),
    ('Blues', 'Blues'),
    ('Classical', 'Classical'),
    ('Country', 'Country'),
    ('Electronic', 'Electronic'),
    ('Folk', 'Folk'),
    ('Funk', 'Funk'),
    ('Hip-Hop', 'Hip-Hop'),
    ('Heavy Metal', 'Heavy Metal'),
    ('Instrumental', 'Instrumental'),
    ('Jazz', 'Jazz'),
    ('Musical Theatre', 'Musical Theatre'),
    ('Pop', 'Pop'),
    ('Punk', 'Punk'),
    ('R&B', 'R&B'),
    ('Reggae', 'Reggae'),
    ('Rock n Roll', 'Rock n Roll'),
    ('Soul', 'Soul'),
    ('Other', 'Other'),
]

class ShowForm(Form):
    artist_id = StringField(
        'artist_id'
    )
    venue_id = StringField(
        'venue_id'
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default= datetime.today()
    )


class VenueForm(Form):


    def validate_genres(form, field):
        genres_values = [choice[1] for choice in genres_choices]
        for value in field.data:
            if value not in genres_values:
                raise ValidationError('Invalid genres value.')

    def validate_phone(form, field):
        if not re.search(r"^[0-9]{3}-[0-9]{3}-[0-9]{4}$", field.data):
            raise ValidationError("Invalid phone number.")


    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
  
    state = SelectField(
        'state', validators=[DataRequired()], choices=state_choices
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired()], choices=genres_choices
    )
    
    address = StringField(
        'address', validators=[DataRequired()]
    )
    
    phone = StringField(
        'phone', validators=[DataRequired()]
    )
    
    image_link = StringField(
        'image_link'
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL()]
    )

    
    website = StringField(
        'website', validators=[DataRequired(), URL(), Length(max=120)]
    )
    seeking_talent = SelectField(
        'seeking_talent',
        choices=[
            ('Yes', 'Yes'),
            ('No', 'No')
        ]
    )
    seeking_description = StringField(
        'seeking_description', validators=[Length(max=400)]
    )

class ArtistForm(Form):

     def validate_genres(form, field):
        genres_values = [choice[1] for choice in genres_choices]
        for value in field.data:
            if value not in genres_values:
                raise ValidationError('Invalid genres value.')
 
     def validate_phone(form, field):
        if not re.search(r"^[0-9]{3}-[0-9]{3}-[0-9]{4}$", field.data):
            raise ValidationError("Invalid phone number.")

     name = StringField(
        'name', validators=[DataRequired()]
     )
     city = StringField(
        'city', validators=[DataRequired()]
     )
     state = SelectField(
        'state', validators=[DataRequired()], choices=state_choices
     )
     phone = StringField(
        'phone', validators=[DataRequired()]
    )
     image_link = StringField(
        'image_link', validators=[DataRequired(), URL(), Length(max=300)]
    )
     genres = SelectMultipleField(
        # TODO implement enum restriction
        'genres', validators=[DataRequired()],
        choices=genres_choices
    )
     facebook_link = StringField(
        # TODO implement enum restriction
        'facebook_link', validators=[URL()]
    )

     image_link = StringField(
        'image_link', validators=[URL()]
    )
     website = StringField(
        'website', validators=[URL()]
    )
     seeking_venue = SelectField(
        'seeking_venue',
        choices=[
            ('Yes', 'Yes'),
            ('No', 'No')
        ]
    )
     seeking_description = StringField(
        'seeking_description', validators=[Length(max=400)]
    )


# TODO IMPLEMENT NEW ARTIST FORM AND NEW SHOW FORM
