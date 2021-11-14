from flask import Flask, jsonify, render_template
from db_mysql import BuyDb, LotteryDb
from datetime import datetime

app = Flask(__name__)

buy_db = BuyDb()
lottery_db = LotteryDb()


@app.route('/newest')
def get_newest():

    newest_data = lottery_db.get_newest()

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
            "carryover": newest_data.carryover,
            "sales": newest_data.sales,
        }

        response_data.append(json_data)

    return render_template('newest.html', newest_data=json_data)


@app.route('/newest.json')
def get_newest_json():

    newest_data = lottery_db.get_newest()

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
def get_winning():
    newest_list = buy_db.get_newest()

    response_data = []

    for newest_data in newest_list:
        winning_str = ''
        if newest_data.winning > 0:
            lottery_data = lottery_db.get_lottery_date(newest_data.target_date)
            amount = 0
            if newest_data.winning == 6:
                amount = lottery_data.six_amount
            if newest_data.winning == 5:
                amount = lottery_data.five_amount
            if newest_data.winning == 4:
                amount = lottery_data.four_amount
            if newest_data.winning == 3:
                amount = lottery_data.three_amount
            if newest_data.winning == 2:
                amount = lottery_data.two_amount
            if newest_data.winning == 1:
                amount = lottery_data.one_amount

            if newest_data.winning > 0:
                winning_str = '{} {}'.format(newest_data.winning, amount)
            else:
                winning_str = '{}'.format(newest_data.winning)
        json_data = {
            "target_date": datetime.strftime(newest_data.target_date, '%Y-%m-%d'),
            "times": newest_data.times,
            "seq": newest_data.seq,
            "kind": newest_data.kind,
            "winning": winning_str,
        }

        response_data.append(json_data)

    return render_template('winning.html', winning_list=response_data)


@app.route('/winning.json')
def get_winning_json():
    newest_list = buy_db.get_newest()

    response_data = []

    for newest_data in newest_list:
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
    app.run(debug=False, host='0.0.0.0', port=5000)
