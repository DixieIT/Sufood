from flask import render_template, redirect, url_for, request, flash
from app import app, db
from .forms import RegistrationForm
from .models import Customer
from .forms import LoginForm

# Manually enable CSRF protection for all routes
@app.before_request
def csrf_protect():
    if request.method == "POST":
        token = request.form.get("csrf_token", "")
        if not app.csrf_token or not app.csrf_token.check_token(token):
            # Handle CSRF violation (e.g., redirect to an error page)
            return render_template("csrf_error.html")

# Your routes continue below...

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if request.method == 'POST' and form.validate():
        new_customer = Customer(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            username=form.username.data
        )
        new_customer.set_password(form.password.data)

        db.session.add(new_customer)
        db.session.commit()

        return redirect(url_for('login'))
    

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST' and form.validate():
        # Retrieve the user by username
        user = Customer.query.filter_by(username=form.username.data).first()

        if user and user.check_password(form.password.data):
            # Log the user in (you can use Flask-Login for more advanced login management)
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password. Please try again.', 'danger')

    return render_template('login.html', form=form)

@app.route('/get_customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return render_template('customer_list.html', customers=customers)

