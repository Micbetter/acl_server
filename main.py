'''
@Author: your name
@Date: 2020-07-16 14:21:49
@LastEditTime: 2020-07-16 15:02:34
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /acl_server/main.py
'''
from flask import Flask, make_response

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route('/mqtt/auth',methods=["post"])
def auth():
    restp = make_response("ok")
    restp.status = "200"
    return restp
    # return json.dumps(results, ensure_ascii=False)

@app.route('/mqtt/acl')
def acl():
    restp = make_response("ok")
    restp.status = "200"
    return restp
    # return json.dumps(results, ensure_ascii=False)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8991)
