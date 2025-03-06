from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class EmergencyAccess(FlaskForm):
    staff_id = StringField('ID астронавта', validators=[DataRequired()])
    staff_password = StringField('Пароль астронавта', validators=[DataRequired()])
    capitan_id = StringField('ID капитана', validators=[DataRequired()])
    capitan_password = StringField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Войти')
