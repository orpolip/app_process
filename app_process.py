from connect_creator import connect_route
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def diplsay_menu():
    return render_template("menu.html")


@app.route('/mentors', methods=["GET", "POST"])
def mentors_and_school():
    cursor = connect_route().cursor()
    cursor.execute("""SELECT CONCAT(mentors.first_name,' ',mentors.last_name), schools.name, schools.country FROM mentors
    JOIN schools ON mentors.city = schools.city ORDER BY mentors.id;""")
    rows = cursor.fetchall()
    return render_template("mentors_and_school.html", rows=rows)


@app.route('/all-school', methods=["GET", "POST"])
def all_school():
    cursor = connect_route().cursor()
    cursor.execute("""SELECT CONCAT(mentors.first_name,' ',mentors.last_name), schools.name, schools.country FROM mentors
    RIGHT JOIN schools ON mentors.city = schools.city ORDER BY mentors.id;""")
    rows = cursor.fetchall()
    return render_template("all_school.html", rows=rows)


@app.route('/mentors-by-country', methods=["GET", "POST"])
def mentors_by_country():
    cursor = connect_route().cursor()
    cursor.execute("""SELECT COUNT(mentors.id),schools.country FROM mentors
    RIGHT JOIN schools ON mentors.city = schools.city GROUP BY schools.country;""")
    rows = cursor.fetchall()
    return render_template("mentors_by_country.html", rows=rows)


@app.route('/contacts', methods=["GET", "POST"])
def contacts_school():
    cursor = connect_route().cursor()
    cursor.execute("""SELECT schools.name, CONCAT(mentors.first_name,' ',mentors.last_name) FROM mentors
    RIGHT JOIN schools ON mentors.id = schools.contact_person ORDER BY schools.name;""")
    rows = cursor.fetchall()
    return render_template("contacts.html", rows=rows)


@app.route('/applicants', methods=["GET", "POST"])
def applicants_school():
    cursor = connect_route().cursor()
    cursor.execute("""SELECT applicants.first_name, applicants.application_code, applicants_mentors.creation_date FROM applicants 
    JOIN applicants_mentors ON applicants.id = applicants_mentors.applicant_id 
    ORDER BY applicants_mentors.creation_date DESC;""")
    rows = cursor.fetchall()
    return render_template("applicants.html", rows=rows)


if __name__ == '__main__':
    app.run(debug=True)
