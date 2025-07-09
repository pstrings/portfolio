"""Flask server for portfolio website."""
import csv

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


def write_to_csv(data):
    """Write form data to a csv file."""
    with open("database.csv", mode="a", newline="", encoding="utf-8") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=",",
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route("/")
def home():
    """Render the home page of the portfolio website."""
    return render_template("index.html")


@app.route("/<string:page_name>")
def render_page(page_name):
    """Render a specific page based on the page name."""
    try:
        return render_template(page_name)
    except Exception as e:
        return f"Error rendering page: {e}", 404


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    """Handle form submission."""
    if request.method == 'POST':
        try:
            # Process the form data
            data = request.form.to_dict()
            # Here you can add code to save the data or send an email
            write_to_csv(data)
        except Exception as e:
            return f"An error occurred while adding data to database: {e}", 500

        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))
