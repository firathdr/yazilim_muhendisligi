from datetime import datetime
from flask import Flask, request, jsonify
from db import get_db_connection
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # CORS'u etkinleştirir, diğer cihazlardan gelen isteklere izin verir.

# Route: Ana sayfa
@app.route('/')
def home():
    return "Flask MySQL Backend is running!"

# Route: Veri listeleme
@app.route('/data', methods=['GET'])
def get_data():
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
        connection.close()
        return jsonify(result)
    else:
        return jsonify({"error": "Database connection failed"}), 500
@app.route('/payment/<int:x>', methods=['GET'])
def get_data_payment(x):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM payment where user_id=%s", (x,))
        result = cursor.fetchall()
        connection.close()
        print(result[0]['rent_id'])
        for i in range(len(result)):
            result[i]['sure']=sure_hesapla(result[i]['rent_id'])





        return jsonify(result)
    else:
        return jsonify({"error": "Database connection failed"}), 500
def sure_hesapla(id):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT start_time, end_time FROM rents WHERE id = %s", (id,))
        result = cursor.fetchall()
        connection.close()

        if result:
            # Tarihleri string olarak alıp datetime'a çevir
            start_time = result[0]["start_time"]
            end_time = result[0]["end_time"]

            # Farkı hesapla ve dakikaya çevir
            time_difference = round((end_time - start_time).total_seconds())
            return time_difference
        else:
            return "Kayıt bulunamadı."
# Route: Veri ekleme
@app.route('/data', methods=['POST'])
def insert_data():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    card_id = data.get("card_id")
    role = data.get("role")

    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        query = "INSERT INTO users (name,email,password,card_id,role) VALUES (%s, %s,%s, %s,%s)"
        cursor.execute(query, (name,email,password,card_id,role))
        connection.commit()
        connection.close()
        return jsonify({"message": "Data inserted successfully"}), 201
    else:
        return jsonify({"error": "Database connection failed"}), 500

@app.route('/update_data', methods=['POST'])
def update_data():
    try:
        # JSON verisini al
        new_data = request.get_json()
        # Veriyi global stored_data içine kaydet
        temperature = new_data['temperature']
        humidity = new_data['humidity']
        distance = new_data['distance']
        uid = new_data['uid']
        connection = get_db_connection()
        cursor = connection.cursor()

        query_end="select start_time,end_time from rents where user_id=(select id from users where card_id=%s) order by start_time desc limit 1"
        cursor.execute(query_end, (uid,))
        time = cursor.fetchone()
        if(time==None):
            time=[None,None]
        print(time[0],"aaaaa")
        if (time[1]==None and time[0]!=None ):
            update_query = """
                UPDATE rents 
                SET end_time = NOW() 
                WHERE user_id = (SELECT id FROM users WHERE card_id = %s) and end_time is null
                
            """
            #order by id desc limit 1
            cursor.execute(update_query, (uid,))

            # İlgili rent_id'yi bul
            select_rent_query = """
                SELECT id, start_time 
                FROM rents 
                WHERE user_id = (SELECT id FROM users WHERE card_id = %s) 
                ORDER BY id DESC 
                LIMIT 1
            """
            cursor.execute(select_rent_query, (uid,))
            rent_record = cursor.fetchone()
            if rent_record:
                rent_id = rent_record[0]
                rent_start_time = rent_record[1]

                # Ödeme miktarını hesapla
                time_difference = datetime.now() - rent_start_time
                amount = round(time_difference.total_seconds() / 60 * 20)  # Saat başına ücretlendirme örneği
                payment_query = """
                       INSERT INTO payment (user_id, rent_id, amount, name) 
                       VALUES (
                           (SELECT id FROM users WHERE card_id = %s),
                           %s,
                           %s,
                           (SELECT name FROM users WHERE id = (SELECT user_id FROM rents WHERE id = %s))
                       )
                   """
                cursor.execute(payment_query, (uid, rent_id, amount, rent_id))

            connection.commit()
            connection.close()
            return jsonify({"message": "success"}), 200

        else:
            print("else calsiyı")
            query_user = "select id from users where card_id=%s"
            cursor.execute(query_user, (uid,))
            user_id = cursor.fetchone()
            print(user_id)

            query = ("insert into rents(user_id,start_time,end_time) values (%s,now(),null) ")
            cursor.execute(query, user_id, )

            connection.commit()
            connection.close()

            # Başarılı yanıt
            return jsonify({"message": "success"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400
@app.route('/kontrol', methods=['GET'])
def kontrol():
    return jsonify({"message": "success"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
