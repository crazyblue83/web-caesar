from flask import Flask, request
from caesar import rotate_string, encrypt

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    
<!DOCTYPE html>

<html>
    <head>
        <style>
            .error {{color: red;}}

            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <form method="POST">
            <label for="rotate-by">Rotate by:</label>
            <input type="text" name="rot" value="0"/>
            <p class="error">{rot_error}</p>
            <label for="submit-rotate">Submit Query</label>
            <input type="submit"/>
            <textarea name="text">{0}</textarea>
    </body>
</html>
</form>
"""

@app.route('/')
def index():
    return form.format(rot='', rot_error='',
        text='')

def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

@app.route("/", methods=['POST'])
def encrypt_input():
    rot = request.form['rot']
    text = request.form['text']
    text_new = ""
    
    if not is_integer(rot):
        rot_error = 'Not a valid integer'
        rot = ''
    else:
        rot = int(rot)
        if rot > 26 or rot < 0:
            rot_error = 'Rotation value out of range (0-26).'
            rot = ''
    
    if not rot_error:
        text_new = encrypt(rot, text)
        return form.format(text_new='')
        
    else:
        return form.format(rot_error=rot_error,
            text=text,
            rot=rot)

app.run()