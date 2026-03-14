from flask import Flask, render_template, request, redirect, url_for, flash, session, abort
from functools import wraps
from models import db, User, Course, Enrollment
from werkzeug.security import generate_password_hash,check_password_hash

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
'mysql+mysqlconnector://lms_user:password@localhost/lms_db'
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey'

db.init_app(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = (request.form.get('username') or '').strip()
        password = (request.form.get('password') or '').strip()
        
        if not username or not password:
            flash('Please enter both username and password')
            return render_template('login.html')
        
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            flash('Invalid username or password')
            return render_template('login.html')
        
        
        session['user_id'] = user.id
        session['role'] = user.role
        session['username'] = user.username

        if user.role == 'teacher':
            return redirect(url_for('teacher_dashboard'))
        return redirect(url_for('student_dashboard'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out')
    return redirect(url_for('home'))

def login_required(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):

        if not session.get('user_id'):
            flash('You need to be logged in to view this page', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    
    return decorated_function

def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not session.get('user_id'):
                flash('You need to be logged in to view this page', 'error')
                return redirect(url_for('login'))
            
            if session.get('role') != role:
                abort(403)  # Forbidden
            return f(*args, **kwargs)
        return decorated_function
    return decorator

@app.route('/student/dashboard')
@login_required
@role_required('student')
def student_dashboard():
    return render_template('student_dashboard.html')

@app.route('/teacher/dashboard')
@login_required
@role_required('teacher')
def teacher_dashboard():
    return render_template('teacher_dashboard.html')
        

@app.route('/users')
@login_required
def list_users():
    users= User.query.all()
    return render_template('user_list.html', users=users)

@app.route('/users/<int:id>')
@login_required
def user_detail(id):
    user = User.query.get_or_404(id)
    return render_template('user_detail.html', user=user)


@app.route('/users/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_user(id):

    user = User.query.get_or_404(id)
    if request.method == 'POST':
        username = (request.form.get('username') or '').strip()
        email = (request.form.get('email') or '').strip()
        password = (request.form.get('password') or '').strip()
        role = (request.form.get('role') or '').strip()

        if not username:
            flash('Username is required', 'error')
            return render_template('user_edit.html', user=user)

        if not email:
            flash('Email is required', 'error')
            return render_template('user_edit.html', user=user)
        
        if '@' not in email:
            flash('Email is invalid', 'error')
            return render_template('user_edit.html', user=user) 

        if not password:
            flash('Password is required', 'error')
            return render_template('user_edit.html', user=user)
        
        if len(password) < 4:
            flash('Password must be at least 8 characters long', 'error')
            return render_template('user_edit.html', user=user)
        
        if role not in ['student', 'teacher']:
            flash('Role is invalid', 'error')
            return render_template('user_edit.html', user=user)

        # unique username and email
        other = User.query.filter_by(username=username).first()
        if other and other.id != user.id:
            flash('Username already exists', 'error')
            return render_template('user_edit.html', user=user)
        
        other = User.query.filter_by(email=email).first()
        if other and other.id != user.id:
            flash('Email already exists', 'error')
            return render_template('user_edit.html', user=user)
        
        try:
            user.username = username
            user.email = email
            user.password = generate_password_hash(password)
            user.role = role
            db.session.commit()
            flash('User updated successfully', 'success')
            redirect(url_for('list_users'))
        except Exception:
            db.session.rollback()
            flash('Error updating user', 'error')
            return render_template('user_edit.html', user=user)

    return render_template('user_edit.html', user=user)

@app.route('/users/delete/<int:id>')
@login_required
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('list_users'))

@app.route('/courses')
@login_required
def list_courses():
    courses = Course.query.all()
    return render_template('course_list.html', courses=courses)

@app.route('/courses/create', methods=['GET', 'POST'])
@login_required
@role_required('teacher')
def course_create():

    if request.method == 'POST':
        title = (request.form.get('title') or '').strip()
        description = (request.form.get('description') or '').strip()
        teacher_id = (request.form.get('teacher_id') or '').strip()

        # backend validation

        if not title:
            flash('Title is required')
            teachers = User.query.filter_by(role='teacher').all()
            return render_template('course_form.html', teachers=teachers, title=title, description=description)

        


        course = Course(title=title, description=description, teacher_id=teacher_id)
        db.session.add(course)
        db.session.commit()
        return redirect(url_for('list_courses'))
    teachers = User.query.filter_by(role='teacher').all()
    return render_template('course_form.html', teachers=teachers)

@app.route('/courses/<int:id>')
@login_required
def course_detail(id):
    course = Course.query.get_or_404(id)
    user_enrollment = None

    if session.get('role') == 'student' and session.get('user_id'):
        user_enrollment = Enrollment.query.filter_by(user_id=session.get('user_id'), course_id=id).first()

    return render_template('course_detail.html', course=course, user_enrollment=user_enrollment)

@app.route('/course/<int:id>/enroll', methods=['POST'])
@login_required
@role_required('student')
def enroll_in_course(id):

    """Student clicks Enroll -> status PENDING."""
    course = Course.query.get_or_404(id)

    user_id = session.get('user_id')

    existing = Enrollment.query.filter_by(
        user_id=user_id,
        course_id=id
    ).first()


    if existing:
        flash('You have already requested enrollment or are enrolled.', 'error')
        return redirect(url_for('course_detail', id=id))

    enrollment = Enrollment(
        user_id=user_id,
        course_id=id,
        status='pending'
    )

    db.session.add(enrollment)
    db.session.commit()

    flash('Enrollment requested. Waiting for teacher approval.', 'success')
    return redirect(url_for('course_detail', id=id))

@app.route('/my-enrollments')
@login_required
@role_required('student')
def my_enrollments():
    """Student: view my enrollments."""

    user_id = session.get('user_id')

    enrollments = Enrollment.query.filter_by(
        user_id=user_id
    ).order_by(
        Enrollment.created_at.desc()
    ).all()

    return render_template('my_enrollments.html',enrollments=enrollments)


@app.route('/course/<int:id>/enrollments')
@login_required
@role_required('teacher')
def course_enrollments(id):
    """Teacher: view enrollments for their course."""
    course = Course.query.get_or_404(id)

    if course.teacher_id != session.get('user_id'):abort(403)
    enrollments = Enrollment.query.filter_by(
        course_id=id).order_by(
        Enrollment.created_at.desc()).all()
    return render_template('course_enrollments.html',course=course,enrollments=enrollments)

@app.route('/courses/edit/<int:id>', methods=['GET', 'POST'])
@login_required
@role_required('teacher')
def course_edit(id):
    course = Course.query.get_or_404(id)
    if request.method == 'POST':
        course.title = request.form['title']
        course.description = request.form['description']
        course.teacher_id = request.form['teacher_id']
        db.session.commit()
        return redirect(url_for('list_courses'))
    
    teachers = User.query.filter_by(role='teacher').all()
    return render_template('course_edit.html', course=course, teachers=teachers)

@app.route('/courses/delete/<int:id>')
@login_required
@role_required('teacher')
def delete_course(id):
    course = Course.query.get_or_404(id)
    db.session.delete(course)
    db.session.commit()
    return redirect(url_for('list_courses'))

@app.route('/register', methods=['GET','POST'])

def register():

    if request.method == 'POST':

        username = (request.form.get('username') or '').strip()
        email = (request.form.get('email') or '').strip()
        password = (request.form.get('password') or '').strip()
        role = (request.form.get('role') or '').strip()

        if not username:
            flash('Username is required', 'error')
            return render_template('register.html')

        if not email:
            flash('Email is required', 'error')
            return render_template('register.html')

        if not password:
            flash('Password is required', 'error')
            return render_template('register.html')

        if len(password) < 6:
            flash('Password must be at least 6 characters', 'error')
            return render_template('register.html')

        if not role:
            flash('Role is required', 'error')
            return render_template('register.html')

        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'error')
            return render_template('register.html')

        if User.query.filter_by(email=email).first():
            flash('Email already exists', 'error')
            return render_template('register.html', error='Email already exists', username=username, email=email, role=role)

        hashed_password = generate_password_hash(password)
        try:
            hashed_password = generate_password_hash(password)
            user = User(username=username,email=email,password=hashed_password,role=role)
            db.session.add(user)
            db.session.commit()
            flash('User created successfully', 'success')
            return redirect(url_for('list_users'))
        except Exception:
            db.session.rollback()
            flash('Error creating user', 'error')
            return render_template('register.html', username=username, email=email, role=role)
    
    return render_template('register.html')

@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403

# Create all tables when app runs(first time)
with app.app_context():
    db.create_all()
    print("Database created (user, course)")

if __name__ == "__main__":
    app.run(debug=True)