from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from flask_bcrypt import Bcrypt
import os
from dotenv import load_dotenv
import logging
import sys

load_dotenv()  # Required for environment variables

print("DB_HOST:", os.getenv("DB_HOST"))
print("DB_NAME:", os.getenv("DB_NAME"))

# Configure logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('debug.log', encoding='utf-8')
    ]
)

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'), 
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        charset="utf8mb4"
    )

@app.route('/login', methods=['POST'])
def login_route():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        print("1. Login basladi")
        
        # Establish direct database connection
        db = get_db_connection()
        print("2. Database baglandi")
        
        cursor = db.cursor()
        cursor.execute("SELECT first_name, last_name, password FROM users WHERE email=%s", (email,))
        user = cursor.fetchone()
        cursor.close()
        db.close()

        print("3. Sorgu tamamlandi")
        
        if user:
            print("4. Kullanici BULUNDU")
            stored_hash = user[2]
            print(f"5. Hash: {stored_hash}")
            
            # Verify password against stored hash
            if bcrypt.check_password_hash(stored_hash, password):
                print("6. SIFRE DOGRU")
                return jsonify({
                    "message": "Giriş başarılı!",
                    "technicianFullName": f"{user[0]} {user[1]}"
                }), 200
            else:
                print("6. SIFRE YANLIS")
                return jsonify({"message": "Hatalı şifre!"}), 401
        else:
            print("4. Kullanici BULUNAMADI")
            return jsonify({"message": "Kullanıcı bulunamadı!"}), 401
        
    except Exception as e:
        print("HATA:", str(e))
        return jsonify({"message": "Sunucu hatası!"}), 500

# Import other route handlers
from controllers.montaj.montajGetirFiltreli import montajGetirFiltreli

@app.route('/montajGetirFiltreli', methods=['GET'])
def montajGetirFiltreli_route():
    return montajGetirFiltreli()

if __name__ == '__main__':
    app.run(debug=True)