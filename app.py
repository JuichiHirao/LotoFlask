from flask import Flask, jsonify
from db_mysql import BuyDb, LotteryDb
from datetime import datetime

app = Flask(__name__)

buy_db = BuyDb()
lottery_db = LotteryDb()


@app.route('/newest')
def get_newest():  # put application's code here
    newest_data = lottery_db.get_newest()
    # buy_db.get_newest()

    response_data = []

    if newest_data.times > 0:
        json_data = {
            "lottery_date": datetime.strftime(newest_data.lottery_date, '%Y-%m-%d'),
            "times": newest_data.times,
            "one_unit": newest_data.one_unit,
            "one_amount": newest_data.one_amount,
            "two_unit": newest_data.two_unit,
            "two_amount": newest_data.two_amount,
            "three_unit": newest_data.three_unit,
            "three_amount": newest_data.three_amount,
            "four_unit": newest_data.four_unit,
            "four_amount": newest_data.four_amount,
            "five_unit": newest_data.five_unit,
            "five_amount": newest_data.five_amount,
            "six_unit": newest_data.six_unit,
            "six_amount": newest_data.six_amount,
        }

        response_data.append(json_data)

    return jsonify({
            'status': 'OK',
            'data': response_data
        })


@app.route('/winning')
def get_winning():  # put application's code here
    newest_list = buy_db.get_newest()

    response_data = []

    for newest_data in newest_list:
        # newest_data = BuyData()
        json_data = {
            "target_date": datetime.strftime(newest_data.target_date, '%Y-%m-%d'),
            "times": newest_data.times,
            "seq": newest_data.seq,
            "kind": newest_data.kind,
            "winning": newest_data.winning,
        }

        response_data.append(json_data)

    return jsonify({
            'status': 'OK',
            'data': response_data
        })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    # app.run()
