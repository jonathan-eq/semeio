#!/usr/bin/env python
# pylint: disable=consider-using-f-string,invalid-name
from resdata.summary import Summary

OIL_PRICES = {
    "2010-01-01": 78.33,
    "2010-02-01": 76.39,
    "2010-03-01": 81.20,
    "2010-04-01": 84.29,
    "2010-05-01": 73.74,
    "2010-06-01": 75.34,
    "2010-07-01": 76.32,
    "2010-08-01": 76.60,
    "2010-09-01": 75.24,
    "2010-10-01": 81.89,
    "2010-11-01": 84.25,
    "2010-12-01": 89.15,
    "2011-01-01": 89.17,
    "2011-02-01": 88.58,
    "2011-03-01": 102.86,
    "2011-04-01": 109.53,
    "2011-05-01": 100.90,
    "2011-06-01": 96.26,
    "2011-07-01": 97.30,
    "2011-08-01": 86.33,
    "2011-09-01": 85.52,
    "2011-10-01": 86.32,
    "2011-11-01": 97.16,
    "2011-12-01": 98.56,
    "2012-01-01": 100.27,
    "2012-02-01": 102.20,
    "2012-03-01": 106.16,
    "2012-04-01": 103.32,
    "2012-05-01": 94.65,
    "2012-06-01": 82.30,
    "2012-07-01": 87.90,
    "2012-08-01": 94.13,
    "2012-09-01": 94.51,
    "2012-10-01": 89.49,
    "2012-11-01": 86.53,
    "2012-12-01": 87.86,
    "2013-01-01": 94.76,
    "2013-02-01": 95.31,
    "2013-03-01": 92.94,
    "2013-04-01": 92.02,
    "2013-05-01": 94.51,
    "2013-06-01": 95.77,
    "2013-07-01": 104.67,
    "2013-08-01": 106.57,
    "2013-09-01": 106.29,
    "2013-10-01": 100.54,
    "2013-11-01": 93.86,
    "2013-12-01": 97.63,
    "2014-01-01": 94.62,
    "2014-02-01": 100.82,
    "2014-03-01": 100.80,
    "2014-04-01": 102.07,
    "2014-05-01": 102.18,
    "2014-06-01": 105.79,
    "2014-07-01": 103.59,
    "2014-08-01": 96.54,
    "2014-09-01": 93.21,
    "2014-10-01": 84.40,
    "2014-11-01": 75.79,
    "2014-12-01": 59.29,
    "2015-01-01": 47.22,
    "2015-02-01": 50.58,
    "2015-03-01": 47.82,
    "2015-04-01": 54.45,
    "2015-05-01": 59.27,
    "2015-06-01": 59.82,
    "2015-07-01": 50.90,
    "2015-08-01": 42.87,
    "2015-09-01": 45.48,
}

if __name__ == "__main__":
    summary = Summary("SNAKE_OIL_FIELD")
    start_time = summary.get_start_time()
    date_ranges = summary.time_range(start_time, interval="1M")
    production_sums = summary.blocked_production("FOPT", date_ranges)

    npv = 0.0
    for index in range(0, len(date_ranges) - 1):
        date = date_ranges[index + 1]  # end of period
        production_sum = production_sums[index]

        oil_price = OIL_PRICES[date.date().strftime("%Y-%m-%d")]

        production_value = oil_price * production_sum
        npv += production_value

    with open("snake_oil_npv.txt", "w", encoding="utf-8") as output_file:
        output_file.write(f"NPV {npv !s}\n")

        if npv < 80000:
            rating = "POOR"
        elif 80000 <= npv < 100000:
            rating = "AVERAGE"
        elif 100000 <= npv < 120000:
            rating = "GOOD"
        else:
            rating = "EXCELLENT"

        output_file.write(f"RATING {rating !s}\n")
