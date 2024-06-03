from flask import Flask

app = Flask(__name__)

@app.route("/home")
def hello_world():
    return "<p>Hellowww this is some  sabre alam, World!</p>"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080 , debug=True)

a = 10
print(a)

arr = [1,2,3,45]


