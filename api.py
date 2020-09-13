import pymysql
from app import app
from conn import mysql
from flask import jsonify, request, flash

#GET ALL
@app.route('/')
@app.route('/select', methods=['GET'])

def user():
    try:
        conn mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * FROM details")
        rows = cur.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()

#GET ONE
@app.route('/select/<id>', methods=['GET'])

def userone(id):
    try:
        conn mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * FROM details WHERE NAMEID ="+id)
        rows = cur.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()

#INSERT
@app.route('/insert', methods=['POST'])

def inst():
    conn = mysql.connect()
    cur = conn.cursor(mysql.cursors.DictCursor)
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    query = "insert into details (firstname, lastname) values ('"+ firstname +"', '"+ lastname +"')"
    cur.execute(query)
    conn.commit()
    cur.close()
    output = {'firstname' : request.json['firstname'], 'lastname' : request.json['lastname'], 'Message': 'Success'}

    return jsonify({'result' : output})

#UPDATE
@app.route('/update/<id>', methods=['PUT'])

def updates(id):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    query = "update details set firstname = '"+ firstname +"', lastname = '"+ lastname +"' Where NameID = '"+ id +"'"
    cur.execute(query)
    conn.commit()
    cur.close()
    output = {'firstname' : request.json['firstname'], 'lastname' : request.json['lastname'], 'Message': 'Success'}

    return jsonify({'result' : output})

#DELETE
@app.route('/delete/<id>', methods=['DELETE'])

def delete(id):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    query = "DELETE from details Where NameID = '"+ id +"'"
    cur.execute()
    conn.commit()
    cur.close()
    output = {'firstname' : request.json['firstname'], 'lastname' : request.json['lastname'], 'Message': 'DELETED'}

    return jsonify({'result' : output})

if __name__ == "__main__":
    app.debug = True
    app.run()