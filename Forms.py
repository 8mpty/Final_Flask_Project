from wtforms import Form, StringField, validators, SelectField, FileField, ValidationError
from wtforms.fields import EmailField


class UserFormCreation(Form):

    username = StringField('', [validators.Length(min=1, max=12), validators.DataRequired()])
    npass = StringField('', [validators.Length(min=8, max=20), validators.DataRequired()])
    npass_con = StringField('', [validators.Length(min=8, max=20), validators.DataRequired()])

    sec_ops = SelectField('', [validators.DataRequired()], choices=[
        ('', 'Select Security Question'),
        ('favplc', 'What is your favourite place to visit?'),
        ('sib', 'How many siblings do you have?'),
        ('favmov', 'What is your favourite movie?')], default='')

    sec_ans = StringField('', [validators.DataRequired()])

    contact_no = StringField('', [validators.Optional()])
    ship_addr = StringField('', [validators.Optional()])
    prof_img = FileField('')

    def validate_npass(form, field):
        if field.data != form.npass_con.data:
            raise ValidationError("Passwords are not the same, Please recheck!!")


class AdminCreation(Form):
    username = StringField('', [validators.Length(min=1, max=12), validators.DataRequired()])
    npass = StringField('', [validators.Length(min=8, max=20), validators.DataRequired()])
    npass_con = StringField('', [validators.Length(min=8, max=20), validators.DataRequired()])
    sec_ops = SelectField('', [validators.DataRequired()], choices=[
        ('', 'Select Security Question'),
        ('favplc', 'What is your favourite place to visit?'),
        ('sib', 'How many siblings do you have?'),
        ('favmov', 'What is your favourite movie?')], default='')

    sec_ans = StringField('', [validators.DataRequired()])
    email = EmailField('', [validators.Email(), validators.Optional()])
    # contact_no = StringField('', [validators.Optional()])
    ship_addr = StringField('', [validators.Optional()])


class Login(Form):
    username = StringField('', [validators.Length(min=5, max=12), validators.DataRequired()])
    npass = StringField('', [validators.Length(min=8, max=20), validators.DataRequired()])


class UpdateUser(Form):
    username = StringField('', [validators.Length(min=5, max=12), validators.DataRequired()])
    npass = StringField('', [validators.Length(min=8, max=20), validators.DataRequired()]) #, render_kw={'readonly': True})
    sec_ops = SelectField('', [validators.DataRequired()], choices=[
        ('', 'Select Security Question'),
        ('favplc', 'What is your favourite place to visit?'),
        ('sib', 'How many siblings do you have?'),
        ('favmov', 'What is your favourite movie?')], default='')

    sec_ans = StringField('', [validators.DataRequired()])
    ship_addr = StringField('', [validators.Optional()])
    prof_img = FileField('')
