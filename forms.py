from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, URL

class CafeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    map_url = StringField('Map URL', validators=[DataRequired(), URL()])
    img_url = StringField('Image URL', validators=[DataRequired(), URL()])
    location = StringField('Location', validators=[DataRequired()])
    has_sockets = BooleanField('Socket')
    has_toilet = BooleanField('Toilet')
    has_wifi = BooleanField('WiFi')
    can_take_calls = BooleanField('Take Calls')
    seats = StringField('Seats')
    coffee_price = StringField('Coffee Price')
    submit = SubmitField('Add Café')