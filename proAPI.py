from re import U
from flask import Flask,jsonify,request
from jinja2.utils import F

app = Flask(__name__)
datas = [
    {
        "Id":1,
        "Name":u"Darsh",
        "Contact":u"1223456789",
        "Done":False,
    },
    {
        "Id":2,
        "Name":u"Ram",
        "Contact":u"1234567890",
        "Done":False,
    }
]

@app.route("/get")
def get_task():
    return jsonify({
        "data":datas
    })

@app.route("/add",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"pls provide data"
        },400)
    data={
        "Id":datas[-1]["Id"]+1,
        "Name":request.json["Name"],
        "Contact":request.json.get("Contact",""),
        "Done":False
    }
    datas.append(data)
    return jsonify({
        "status":"success",
        "message":"task added successfuly"
    })

if(__name__=="__main__"):
    app.run(debug=True)