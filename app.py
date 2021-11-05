from flask import Flask, jsonify
from db_mysql import BuyDb
from datetime import datetime

app = Flask(__name__)

buy_db = BuyDb()


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
    app.run()
