from flask import Flask, render_template, redirect, request
import csv


app = Flask(__name__)

@app.route('/')
def hello_world():
     return render_template("index.html")

# @app.route('/index/<username>/<int:post_id>')
# def username(username, post_id):
#     # return '<h1> This is about us</h2>'
#     return render_template("index.htm", name=username, id = post_id)


# dynamically route the url page
@app.route('/<string:page_url>')
def pass_url(page_url):
    return render_template(page_url+'.html')


def sendToDb(data) :
    
    with open('db.txt', mode ='a') as database :
        email = data['email']
        message = data['message']
        subject = data['subject']
        file = database.write(f'\n{email},{message},{subject}')
     
def sendToCsv(data) :
    
    with open('db.csv', mode ='a', newline ='') as database2 :
        email = data['email']
        message = data['message']
        subject = data['subject']
        csvWriter = csv.writer(database2,  delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL )
        csvWriter.writerow([email, message, subject])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    error = None
    if request.method == 'POST':
        try:
            # return "Hurray, submitted successfully!"
            # if valid_login(request.form['username'],
            #                request.form['password']):
            # return log_the_user_in(request.form['username'])
            redirect = request.form['thanks']
            data = request.form
            sendToCsv(data)
            #return redirect
            # convert to dictionary
            # return redirect('index')
            return render_template(redirect+'.htm', email = request.form['email'])
        except :
            return "THERE IS AN ERROR"
    else:
        error = 'Invalid username/password'
        return error
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    # return render_template('login.html', error=error)



# @app.route('/aboutus')
# def about():
#     return render_template('about.html')

# @app.route('/works')
# def works():
#     return render_template('works.html')


# @app.route('/contact/manager')
# def contact2():
#     return '<h1> Only Manager should Please, contact me</h2>'

if __name__ == '__main__':
    app.run()