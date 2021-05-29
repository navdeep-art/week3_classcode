from flask import Flask, request, render_template
app = Flask(__name__)

# http://127.0.0.1:5000/
@app.route('/')
def hello_world():
    return '<h1>Hello World</h1>'

# Using Jinja2 template
# http://127.0.0.1:5000/picture
@app.route('/picture')
def welcome():
    return render_template('hello.html')  # Using render function from flask

# Using Jinja2 template for PATH parameter
# http://127.0.0.1:5000/welcome/Navdeep
@app.route('/welcome/<name>')
def welcome_name(name):
    return render_template('welcome.html', myname=name)  # Passing Parameter to template

# http://127.0.0.1:5000/name
@app.route('/name')
def my_name():
    return '<h1>Navdeep</h1> <h3>Kaur</h3>'

#app.add_url_rule('/', 'name', my_name)

# GET request is a default
# http://127.0.0.1:5000/sum?a=50&b=40
@app.route('/sum', methods=['GET'])
def add_number():
    a = request.args.get('a')
    b = request.args.get('b')
    c = int(a) + int(b)
    return 'SUM : ' + str(c)

@app.route('/user-data', methods=['GET', 'POST'])
def user_data():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        # Declare Dictionary of values
        # dict={'first_name': first_name, 'last_name': last_name}
        result = '''
                <h1>First Name : {}<h1>
                <h1>Last Name : {}<h1>
            '''
        return result.format(first_name, last_name)
        # return dict

    return 'No GET method allowed, Only POST method is accepted'

# http://127.0.0.1:5000/user
@app.route('/user')
def user_form():
    return '''
        <form method="POST" action="http://127.0.0.1:5000/user-data">
               <div><label>First Name: <input type="text" name="first_name"></label></div>
               <div><label>Last Name: <input type="text" name="last_name"></label></div>
               <input type="submit" value="Submit">
        </form>
    '''
if __name__ == '__main__':
    app.run()
