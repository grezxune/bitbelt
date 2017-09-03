from bitbelt import app

@app.route('/')
def index():
    return 'Hello, from BitBelt!'
