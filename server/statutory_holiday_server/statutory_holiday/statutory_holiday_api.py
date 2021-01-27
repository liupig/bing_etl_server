from flask import Blueprint, render_template
from server.statutory_holiday_server.statutory_holiday.statutory_holiday_process import get_statutory_holiday_info, \
    statutory_holiday_info_to_csv
import json
import datetime
import pandas as pd

STATUTORY_HOLIDAY_PATH = "./server/statutory_holiday_server/statutory_holiday/"

STATUTORY_HOLIDAY_API = Blueprint("statutory_holiday_api", __name__)
STATUTORY_HOLIDAY_INFO = {}


@STATUTORY_HOLIDAY_API.route("/v1/bing/etl/statutoryHoliday", methods=["GET"])
def get_statutory_holiday():
    year = datetime.datetime.now().year
    df = pd.read_csv(STATUTORY_HOLIDAY_PATH + "national_holidays.csv", encoding="utf8")

    df = df.loc[df["year"] == year]
    if df.empty:
        statutory_holiday_info_to_csv()

    df = pd.read_csv(STATUTORY_HOLIDAY_PATH + "national_holidays.csv", encoding="utf8")
    data = pd.DataFrame(df, columns=["name", "startDate", "endDate"]).to_dict(orient="records")
    result = {"result": json.dumps(data, indent=4, ensure_ascii=False), "status": "ok"}

    return render_template("statutoryHoliday.html", variable=result)
