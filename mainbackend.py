from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)        # SETS VAR AS THE APPLICATION

@app.route("/") # THIS IS THE BASIC HOME PAGE WITH NO EXTRA ARGS, EX. (GOOGLE.COM/)
def home(): # WHAT HAPPENS WHEN WE VISIT THE HOME PAGE
    return render_template("index.html") # INDEX.HTML CONTROLS WHAT IS SHOWN ON SCREEN
@app.route("/login", methods=["POST", "GET"]) # THIS IS THE LOGIN PAGE WITH THE ARG: LOGIN, EX. (GOOGLE.COM/LOGIN)
def login(): # WHAT HAPPENS WHEN WE VISIT THE LOGIN PAGE
    if request.method == "POST": # IF THE OUPUT GIVEN BY THE WEBSITE IS IN FORM: "POST"
        user = request.form["nm"] # SET VAR TO WHATEVER USER ENTERED IN INPUT BAR
        return redirect(url_for("user", usr = user)) # SEND THEM TO A WEBSITE THAT HAS THEIR INPUT AS ARG, EX. IF ARG = JOHN, (GOOGLE.COM/JOHN)
    else:
        return render_template("login.html") # GET REQUEST MEANS THAT WEBSITE IS LOADING, WE WANT TO KEEP IT THERE
    
@app.route("/<usr>") # SET USR TO ARG, EX. IF URL = (GOOGLE.COM/JOHN), USR = JOHN
def user(usr): # WHAT HAPPENS WHEN USER FUNCTION OPENED UP
    return f"<h1>{usr}</h1>" # DISPLAY THE USER'S NAME

@app.route("/spreadsheet")
def spreadsheet():
    return "this is the spreadsheet page"

@app.route("/todo")
def todo():
    return "this is the to-do list page"

@app.route("/calendar")
def calendar():
    return "this is the calendar page"

@app.route("/notepad")
def notepad():
    return "this is the notepad page"

if __name__ == "__main__":
    app.run(debug=True)

