from flask import Flask, render_template, request
from datetime import datetime
from fetch_metar import fetch_all_metar

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        icao = request.form['icao'].strip().upper()

        # Start datetime
        start_date = request.form['start_date']
        start_hour = request.form['start_hour']
        start_min = request.form['start_min']
        start_dt = datetime.strptime(f"{start_date} {start_hour}:{start_min}", "%Y-%m-%d %H:%M")

        # End datetime
        end_date = request.form['end_date']
        end_hour = request.form['end_hour']
        end_min = request.form['end_min']
        end_dt = datetime.strptime(f"{end_date} {end_hour}:{end_min}", "%Y-%m-%d %H:%M")

        fetch_all_metar(icao, start_dt, end_dt)

        return f"<h3>✅ METAR data fetched successfully for {icao}</h3><a href='/'>Go back</a>"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
