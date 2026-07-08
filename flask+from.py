from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>Registration Form</title>
</head>
<body>

<form action="/login" method="post">

Name:
<input type="text" name="user" placeholder="Enter the name"><br><br>

Password:
<input type="password" name="password" placeholder="Enter the password"><br><br>

Email:
<input type="email" name="email" placeholder="Enter the email"><br><br>

Number:
<input type="number" name="number"><br><br>

Color:
<input type="color" name="color"><br><br>

Range:
<input type="range" name="range"><br><br>

Date & Time:
<input type="datetime-local" name="datetime"><br><br>

<input type="submit" value="Submit">
<input type="reset" value="Reset">

</form>

</body>
</html>
'''

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("user")
        return "Welcome " + username

    return "Please submit the form."

if __name__ == "__main__":
    app.run(debug=True)