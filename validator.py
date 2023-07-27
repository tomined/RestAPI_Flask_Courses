from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, Length

class CourseForm(Form):
    #<input max="50" min="3" required name='name' placeholder="www"/>
    name = StringField(
        'name',
        validators=[
            DataRequired(message="Name is requird"),
            Length(min=3,max=50, message="Chars length beetwen 3 and 50 reqiuired")
        ],
        render_kw={"placeholder": "Type a course name"}
    )
    category = StringField(
        'category',
        validators=[ DataRequired(message="Category is required")],
        render_kw={"placeholder":"Type a course category"}
    )
    price = IntegerField(
        'price',
        validators=[ 
            DataRequired(message="Price is required")
            ],
            render_kw={"placeholder":"Type a course price"}
    )
    city = StringField(
        'city',
        validators=[ 
            DataRequired(message="City is required"),
            Length(min=1,max=150, message="Chars length beetwen 1 and 150 reqiuired")
            ],
            render_kw={"placeholder":"Type a course city"}
    )
    hours = IntegerField(
        'hours',
        validators=[ 
            DataRequired(message="Hours is required")
            ],
            render_kw={"placeholder":"Type a course hours"}
    )