# @Time    : 9/22/2021 12:47 PM
# @Author  : arthur
# @Email   : arthurwanggang@outlook.com
# @File    : book.py
# @Software: PyCharm

from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired, Regexp


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
