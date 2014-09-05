from bottle import get, post, request, run
from test2 import lovechart
@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if True:
        return "<img src=http://bitatm.io/kenzo/"+ lovechart(username,password) + " >" 
    else:
        return "<p>Login failed.</p>"

run(host='0.0.0.0', port=8080, debug=True)

