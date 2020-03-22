from flask_wtf import FlaskForm
from wtforms import (
		StringField,
		SubmitField,
		TextAreaField
	)
from wtforms.validators import (
		DataRequired,
		Length
	)


class CreateEditForm(FlaskForm):
	name = StringField(
		'Name', 
		validators=[DataRequired(), Length(max=32)]
		)
	content = TextAreaField(
		'Content',
		validators=[DataRequired(), Length(max=128)]
		)
	submit = SubmitField('Submit!')
