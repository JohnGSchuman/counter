from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = "not4you"

#@app.route('/second')
#def second():
#    return render_template("second.html")
# "second" on lines 9 and 10 and 11 are independent of each other
# 9 on the web address
#10 it's the function name, won't really use this
#11  name of the html file

@app.route('/')
def counter():
    if 'counterNum' not in session:
        session['counterNum'] = 1
    print ("on initial route")
#    counterPassed = 
#    return render_template("counter.html", counterPassed =session['counterNum'])
    return render_template("index.html")

@app.route('/counter')
def users_post():
    print ("session counter returning from initial call")
    print(session['counterNum'])
    session['counterNum'] += 1
    return redirect("/")

@app.route('/reset',)
def from_post():
    print ("submitted new route after submit via button")
    session.clear()
    return redirect("/")


if __name__=="__main__":
    app.run(debug=True, port=5000)