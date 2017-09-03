from flask import Flask

app = Flask(import_name=__name__,
            template_folder='./templates',
            static_folder='./static')

import bitbelt.routes

if __name__ == '__main__':
    app.run(host='localhost', port=2550)