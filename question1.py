from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def default():
    return "Welcome, to my CSCB20 website!"


@app.route('/<name>')
def welcome(name):
    return "Welcome, " + updateStr(name) + ", to my CSCB20 website!"


def generateResponse(name):
    output = ""
    if name.isalpha():
        for c in name:
            output += c.swapcase()
    else:
        for c in name:
            if c.isalpha():
                output += c
    return output


if __name__ == '__main__':
    # app.run()
    app.run(debug=True)
