from flask import Flask, request, render_template
import json
import requests


app = Flask(__name__)
TG_BOT_TOKEN = '5959422704:AAF5qnJSo-Xwohm3sp6xV7SiLSa5TEtvQ8M'


def number_count(serial_num):
    f = open('db.json', 'r')
    data = json.load(f)
    try:
        if data[serial_num]:
            f.close()
            d = open('db.json', 'w')
            data[serial_num] += 1
            d.write(json.dumps(data))
            return True
        else:
            return True
    except KeyError:
        return False


mess = []
@app.route('/', methods=['GET', 'POST'])
def main_page():
    message = request.args.get('msg')
    if message is not None:
        mess.append(message)
        if len(mess) == 2:
            if number_count(str(mess[1])) == True:
                requests.get(f'https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage?chat_id=443420791&text=пользовательно ввел правильный серийный номер')
            else:
                requests.get(f'https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage?chat_id=443420791&text=пользовательно ввел неправильный серийный номер')
    else:
        pass
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5002)
