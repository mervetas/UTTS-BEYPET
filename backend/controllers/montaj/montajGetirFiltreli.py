from flask import request, jsonify
import mysql.connector
from datetime import datetime, date, timedelta
import os
from dotenv import load_dotenv
import sys
import io

# Fix Turkish character encoding issues in logs
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Load environment variables from .env file
load_dotenv()

def montajGetirFiltreli():
    try:
        print("1. Fonksiyon basladi")
        
        technician = request.args.get('technician')
        print(f"2. Technician: {technician}")

        if technician is None:
            print("3. Technician None")
            return jsonify({"message": "Technician parametresi sağlanmadı."}), 400

        print("4. Technician var")
        
        # Get database credentials from environment variables
        db = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME'),
            charset="utf8mb4"
        )
        print("5. Database baglandi")
        
        query = """
                SELECT * FROM montaj_kayitlari
                WHERE technicianFullName = %s
                ORDER BY lastModified DESC
                LIMIT 500
        """
        
        cur = db.cursor()
        print("6. Cursor olustu")
        cur.execute(query, (technician,))
        print("7. Sorgu calisti")
        
        columns = [col[0] for col in cur.description]
        results = cur.fetchall()
        cur.close()
        db.close()

        print(f"8. {len(results)} sonuc bulundu")

        if not results:
            print("9. Sonuc yok")
            return jsonify({"message": "Veri bulunamadı!"}), 404

        print("10. Sonuc var, isleniyor")
        
        # Process and format data for API response
        response_data = []
        for row in results:
            row_dict = {}
            for i, column_name in enumerate(columns):
                value = row[i]
                if isinstance(value, datetime):
                    row_dict[column_name] = value.strftime("%Y-%m-%d %H:%M:%S")
                elif isinstance(value, date):
                    row_dict[column_name] = value.strftime("%Y-%m-%d")
                elif isinstance(value, timedelta):
                    row_dict[column_name] = str(value)
                else:
                    row_dict[column_name] = value
            response_data.append(row_dict)

        print(f"11. {len(response_data)} kayit hazir")
        return jsonify(response_data)

    except Exception as e:
        print(f"12. HATA: {str(e)}")
        return jsonify({"error": "Bir hata oluştu.", "details": str(e)}), 500