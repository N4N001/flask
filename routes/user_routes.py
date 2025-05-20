from flask import Blueprint, render_template, request, redirect, url_for

user_bp = Blueprint('user', __name__)

# In-memory store (you could move this to a separate module too)
users = []

@user_bp.route('/')
def home():
    return render_template('index.html', users=users)

@user_bp.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')

        if name and age:
            users.append({'name': name, 'age': int(age)})
            return redirect(url_for('user.home'))

    return render_template('add_user.html')

@user_bp.route('/delete/<int:index>')
def delete_user(index):
    if 0 <= index < len(users):
        users.pop(index)
    return redirect(url_for('user.home'))


@user_bp.route('/user/<int:index>')
def user_detail(index):
    if 0 <= index < len(users):
        user = users[index]
        return render_template('user_detail.html', user=user, index=index)
    return redirect(url_for('user.home'))
