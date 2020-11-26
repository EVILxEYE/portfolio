import csv
from flask import Flask, render_template, request
app = Flask(__name__)


def write_to_csv(data):
    with open('database.csv', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writter = csv.writer(database, delimiter=',',
                                 quotechar='"', newline='', quoting=csv.QUOTE_MINIMAL)
        csv_writter.writerow([email, subject, message])


@app.route('/')
def root():
    return render_template('home.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name + ".html")


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return render_template('thankyou.html')
