from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    """ Returns welcome message when landing on this page."""
    return """
        <h1>Welcome</h1>
        """

@app.route('/welcome/home')
def welcome_home():
    """ Returns 'Welcome Home' message when landing on this page."""
    return """
        <h1>Welcome Home</h1>
        """

@app.route('/welcome/back')
def welcome_back():
    """ Returns 'Welcome Back' message when landing on this page."""
    return """
        <h1>Welcome Back</h1>
    """