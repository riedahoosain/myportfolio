# A REST API built with Python and Flask to serve historical weather data for various cities.
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
FILEPATH = "data/stations.txt"

stations = pd.read_csv(FILEPATH, skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]

# Loads the home api page


@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())

# For one station for one date: http://127.0.0.1:5000/api/v1/10/1988-10-25


@app.route("/api/v1/<station>/<date>")
def api(station, date):
    filename = "data/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {"station": station,
            "date": date,
            "temperature": temperature}

# for one station for all dates: http://127.0.0.1:5000/api/v1/10


@app.route("/api/v1/<station>")
def all_data_per_stations(station):
    filename = "data/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient='records')
    return result

# for one station for one year: http://127.0.0.1:5000/api/v1/yearly/10/1988


@app.route("/api/v1/yearly/<station>/<year>")
def all_data_per_year(station, year):
    filename = "data/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(
        str(year))].to_dict(orient='records')
    return result


if __name__ == "__main__":
    # Default Port is 5000 but specifying we can change the ports to run multiple apps
    app.run(debug=True, port=5000)
