from flask import Flask, render_template, request, redirect, url_for
import csv
import os
import mail

app = Flask(__name__)

CSV_FILE = 'anmeldungen.csv'


def write_to_csv(data):
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)


@app.route('/')
def index():
    return render_template('anmeldung.html')


@app.route('/anmelden', methods=['POST'])
def anmelden():
    vorname = request.form['vorname']
    nachname = request.form['nachname']
    email = request.form['email']
    adresse = request.form['adresse']
    disziplin = request.form.getlist('disziplin')
    verein = request.form['verein']
    schule = request.form['schule']
    print(disziplin)
    data = {
        'Vorname': vorname,
        'Nachname': nachname,
        'E-Mail': email,
        'Adresse': adresse,
        'Verein': verein,
        'Schule': schule,
        'Disziplin': disziplin
    }

    write_to_csv(data)
    mail.send_email(email,disziplin)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
