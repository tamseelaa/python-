from flask import Flask, Response
import json
app = Flask(__name__)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route('/prime_number/<int:number>', methods=['GET'])
def check_prime(number):
    prime_status = is_prime(number)
    response_data = {
        "Number": number,
        "isPrime": prime_status
    }
    response_json = json.dumps(response_data)
    return Response(response_json, mimetype='application/json')

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)