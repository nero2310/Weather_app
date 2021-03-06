from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class GetWeatherForm(FlaskForm):
    city_name = StringField("City Name", validators=[DataRequired(message="Please enter city name.")])
    country = StringField("Country Code")
    state = StringField("State Name")
    submit = SubmitField("Get weather info")


class NavbarForm(FlaskForm):
    city_name = StringField(validators=[DataRequired(message="Enter city name")])
    submit = SubmitField("Search")