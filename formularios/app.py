from flask import Flask, request

app = Flask(__name__)

@app.route('/miguel', methods=['POST', 'GET'])
def numeros():
    if request.method == 'POST':
        numero_um = float(request.form['numero_um'])
        numero_dois = float(request.form['numero_dois'])
        numero_tres = float(request.form['numero_tres'])
    else:
        numero_um = float(request.args.get('numero_um'))
        numero_dois = float(request.args.get('numero_dois'))
        numero_tres = float(request.args.get('numero_tres'))
    return str((numero_um + numero_dois)/numero_tres)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)