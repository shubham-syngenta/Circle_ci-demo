from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return 'Hello Python'
#@app.route('/test')
#def test():
 #   return '<h1>Hello World</h2>'


if __name__ == "__main__":
    app.run(debug=True)

#print("Hello world")
