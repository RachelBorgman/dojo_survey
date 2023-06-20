from flask import Flask, render_template, request, redirect, session
# from dotenv import load_dotenv

# load_dotenv()

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def new_user():
    return render_template('user.html')

@app.route('/result', methods=["POST"])
def show_user():    
    session['user_name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    print(request.form)
    return render_template('result.html')
# , name_on_template=session['user_name'], location_on_template=session['location'], language_on_template=session['language'], comment_on_template=session['comment']

if __name__=="__main__":   
    app.run(debug=True, host="localhost", port=8000)