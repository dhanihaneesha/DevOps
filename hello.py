from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello():
    return("Hello to 2nd command")


if __name__=='__main__':
    app.run(debug=True)
    