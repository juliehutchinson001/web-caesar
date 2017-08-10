from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

# @app.route("/", method=['POST'])
# def encrypt():
#     new_encrypt = rotate_string(request.form['text'])
#     return "<h1>"+new_encrypt+"</h1>"

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>

    <body>
        <form action="/" method="POST">
           <label for="search-term">Rotate by:</label>
           <input id="search-term" type="text" name="rot" value="0" />
           <textarea name= "text">{0}</textarea> 
           <input type="submit" value="submit query">
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    new_encrypt = rotate_string(request.form['text'], int(request.form['rot']))
    return "<h1>"+form.format(new_encrypt)+"</h1>"

app.run()