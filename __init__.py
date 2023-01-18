import random

from flask import Flask, render_template, request, redirect, url_for, session
from Forms import *
import shelve, User, Admin

app = Flask(__name__)
app.secret_key = '1029384756'

@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/adminpanel')
def adminpanel():
    admins_dict = {}
    admins_db = shelve.open('admin.db', 'r')
    admins_dict = admins_db['Admins']
    admins_db.close()

    admins_list = []
    for key in admins_dict:
        admin = admins_dict.get(key)
        admins_list.append(admin)

    users_dict = {}
    db = shelve.open('user.db', 'r')
    users_dict = db['Users']
    db.close()

    users_list = []
    for key in users_dict:
        user = users_dict.get(key)
        users_list.append(user)

    return render_template('adminpanel.html', count=len(users_list), counta=len(admins_list), users_list=users_list,
                           admins_list=admins_list)


@app.route('/loginpanel', methods=['GET', 'POST'])
def loginpanel():
    user_login_form = Login(request.form)

    admins_dict = {}
    admins_db = shelve.open('admin.db', 'r')
    admins_dict = admins_db['Admins']
    admins_db.close()

    users_dict = {}
    db = shelve.open('user.db', 'r')
    # users_dict = db['Users']
    users_dict = db
    
    username = user_login_form.username.data
    password = user_login_form.npass.data

    # for values in db.values():
    #     print(values)

    for key, value in users_dict.items():
        if username in users_dict.values():
            # if password == users_dict:
            print('Loggin')
            return redirect(url_for('homepage'))
    else:
        print(list(value))
        print(username)
        print(list(db.keys()))
        print(list(db['Users']))
        print(list(db.items()))
        print(list(db.values()))

        print('Wrong Username')

    db.close()
    return render_template('loginpanel.html', form=user_login_form)


@app.route('/regispanel', methods=['GET', 'POST'])
def regispanel():
    global user_id
    user_reg_form = UserFormCreation(request.form)
    if request.method == 'POST' and user_reg_form.validate():
        user_dict = {}
        user_db = shelve.open('user.db', 'c')

        try:
            user_dict = user_db['Users']
            user_count = len(user_dict)
            rand1 = random.randint(1, 999999)
            rand2 = random.randint(1, 999999)
            id = rand1 + rand2
            user_id = user_count + id
        except:
            print("Error in getting Users from user.db")
            user_count = 0
            user_id = 1

        user = User.User(
            user_id,
                         user_reg_form.username.data,
                         user_reg_form.npass.data,
                         user_reg_form.sec_ops.data,
                         user_reg_form.sec_ans.data,
                         user_reg_form.ship_addr.data,
                         user_reg_form.contact_no.data, user_reg_form.prof_img.data)
        user_dict[user.get_user_id()] = user
        user_db['Users'] = user_dict
        session['user_created'] = user.get_username()

        return redirect(url_for('loginpanel'))
    return render_template('createUser.html', form=user_reg_form)


@app.route('/regispaneladmin', methods=['GET', 'POST'])
def regispaneladmin():
    admin_reg_form = AdminCreation(request.form)
    if request.method == 'POST' and admin_reg_form.validate():
        admin_dict = {}
        admin_db = shelve.open('admin.db', 'c')

        try:
            admin_dict = admin_db['Admins']
        except:
            print("Error in getting Admins from admin.db")

        admin = Admin.Admin(admin_reg_form.username.data,
                            admin_reg_form.npass.data,
                            admin_reg_form.sec_ops.data,
                            admin_reg_form.sec_ans.data,
                            admin_reg_form.ship_addr.data,
                            # admin_reg_form.contact_no.data,
                            admin_reg_form.email.data
                            )

        admin_dict[admin.get_admin_id()] = admin
        admin_db['Admins'] = admin_dict

        # admin_dict = admin_db['Admins']
        # admin = admin_dict[admin.get_admin_id()]
        # print(admin.get_username(),
        #       admin.get_sec_ans(),
        #       admin.get_password(), "was stored in admin.db successfully with id ==", admin.get_user_id())
        # admin_db.close()

        return redirect(url_for('homepage'))
    return render_template('createAdmin.html', form=admin_reg_form)


@app.route('/deleteUser/<int:id>', methods=['POST'])
def delete_user(id):
    users_dict = {}
    db = shelve.open('user.db', 'w')
    users_dict = db['Users']

    user = users_dict.pop(id)

    db['Users'] = users_dict
    db.close()

    session['user_deleted'] = user.get_username()

    return redirect(url_for('adminpanel'))


@app.route('/recpanel')
def recpanel():
    return render_template('forgotPass.html')


@app.route('/updateUser/<int:id>/', methods=['GET', 'POST'])
def update_user(id):

    update_user_form = UpdateUser(request.form)

    if request.method == 'POST' and update_user_form.validate():

        db = shelve.open('user.db', 'w')
        users_dict = db['Users']

        user = users_dict.get(id)
        user.set_prof_img(update_user_form.prof_img.data)
        user.set_username(update_user_form.username.data)
        user.set_password(update_user_form.npass.data)
        user.set_sec_ops(update_user_form.sec_ops.data)
        user.set_sec_ans(update_user_form.sec_ans.data)
        user.set_ship_addr(update_user_form.ship_addr.data)

        db['Users'] = users_dict
        db.close()

        session['user_updated'] = user.get_username()

        return redirect(url_for('homepage'))
    else:

        users_dict = {}
        db = shelve.open('user.db', 'r')
        users_dict = db['Users']
        db.close()
        user = users_dict.get(id)
        update_user_form.prof_img.data = user.get_prof_img()
        update_user_form.username.data = user.get_username()
        update_user_form.npass.data = user.get_password()
        update_user_form.sec_ops.data = user.get_sec_ops()
        update_user_form.sec_ans.data = user.get_sec_ans()
        update_user_form.ship_addr.data = user.get_ship_addr()

        return render_template('updateUser.html', form=update_user_form)


if __name__ == '__main__':
    app.run(debug=True)
