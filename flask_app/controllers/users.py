from flask_app import app
from flask import render_template,redirect, request, session
from flask_app.models.user import User


@app.route('/create_user')
def new_user_register():
    return render_template('index.html')

@app.route ('/create_user',methods=["POST"])
def create_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.save_user(data)
    return redirect('/')

#Home page and READ ALL Page 
@app.route('/')
def display_users():
    all_users = User.get_all_users()
    return render_template('show.html', all_users = all_users)

@app.route('/show_user/<int:users_id>')
def display_user(users_id):
    one_user = User.get_one_user_id(users_id)
    print(one_user)
    return render_template('user.html', one_user = one_user)

#EDIT page
@app.route('/edit/<int:users_id>')
def edit_user(users_id):
    one_user = User.get_one_user_id(users_id)
    print(one_user)
    return render_template('edit.html', one_user = one_user)

@app.route('/edit/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/')


#Delete
@app.route('/user/delete/<int:user_id>')
def delete_user(user_id):
    User.delete_user(user_id)
    return redirect('/')
