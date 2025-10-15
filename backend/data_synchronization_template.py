"""
UTTS API Data Synchronization Template
-------------------------------------
This template demonstrates the real-time data synchronization system
used in production for fetching assembly data from UTTS APIs.

Key Features:
- Secure API authentication with token management
- Optimized database operations with duplicate prevention  
- Real-time data synchronization
- Comprehensive error handling
"""

from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
import requests
from datetime import datetime
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

def senkronize_montajlar():
    """
    Main synchronization function
    Fetches real-time assembly data from UTTS API and syncs with local database
    """
    print("Starting UTTS data synchronization...")
    
    try:
        # Initialize database connection
        db = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', ''),
            database=os.getenv('DB_NAME', 'utts_bey_pet'),
            charset="utf8mb4"
        )
        cursor = db.cursor()

        # Step 1: Authenticate with UTTS API
        login_url = "https://api.utts.gov.tr/users/login"
        login_payload = {
            "email": os.getenv('UTTS_EMAIL', 'your_email@company.com'),
            "password": os.getenv('UTTS_PASSWORD', 'your_secure_password')
        }
        login_res = requests.post(login_url, json=login_payload)
        token = login_res.json()["item"]["accessToken"]

        # Step 2: Fetch assembly data from API
        montaj_url = "https://api.utts.gov.tr/support-operations/installation-progresses"
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(montaj_url, headers=headers)
        montajlar = response.json()["item"]["items"]

        # Date parsing functions
        def parse_date(date_str):
            return datetime.strptime(date_str, "%d.%m.%Y").date() if date_str else None

        def parse_time(time_str):
            return datetime.strptime(time_str, "%H:%M").time() if time_str else None

        def parse_datetime(dt_str):
            if not dt_str:
                return None
            trimmed = dt_str.split("T")[0] + "T" + dt_str.split("T")[1].split(".")[0]
            return datetime.strptime(trimmed, "%Y-%m-%dT%H:%M:%S")

        # Process each record
        processed_count = 0
        for kayit in montajlar:
            kayit_id = kayit.get("vehicleOrderInstallationId")
            api_last_modified = parse_datetime(kayit.get("lastModified"))

            # Check if record needs update
            cursor.execute("SELECT lastModified FROM montaj_kayitlari WHERE vehicleOrderInstallationId = %s", (kayit_id,))
            result = cursor.fetchone()

            if result:
                db_last_modified = result[0]
                if db_last_modified == api_last_modified:
                    print(f"Skipped unchanged record: {kayit_id}")
                    continue

            print(f"Saving record: {kayit_id}")
            
            # Insert or update record
            cursor.execute("""
                INSERT INTO montaj_kayitlari (
                    vehicleOrderInstallationId, licensePlate, installationCode, companyName, 
                    ttbServiceName, vehicleCompanyName, taxInfoNumber, taxInfoOffice, 
                    driverEmail, driverPhoneNumber, address, city, district, 
                    vehicleOrderInstallationStatus, vehicleOrderInstallationStatusId,
                    productName, ttbServiceReferenceNumber, vehicleCompanyPhoneNumber, 
                    identificationNumberForInvoice, lastModified, technicianFullName, 
                    salePriceString, netSalePriceString, activation_date, activation_time, 
                    installment_date, installment_time, hasReceiptInfo, companyTypeStr, 
                    guncellenme_zamani
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    licensePlate = VALUES(licensePlate),
                    installationCode = VALUES(installationCode),
                    companyName = VALUES(companyName),
                    ttbServiceName = VALUES(ttbServiceName),
                    vehicleCompanyName = VALUES(vehicleCompanyName),
                    taxInfoNumber = VALUES(taxInfoNumber),
                    taxInfoOffice = VALUES(taxInfoOffice),
                    driverEmail = VALUES(driverEmail),
                    driverPhoneNumber = VALUES(driverPhoneNumber),
                    address = VALUES(address),
                    city = VALUES(city),
                    district = VALUES(district),
                    vehicleOrderInstallationStatus = VALUES(vehicleOrderInstallationStatus),
                    vehicleOrderInstallationStatusId = VALUES(vehicleOrderInstallationStatusId),
                    productName = VALUES(productName),
                    ttbServiceReferenceNumber = VALUES(ttbServiceReferenceNumber),
                    vehicleCompanyPhoneNumber = VALUES(vehicleCompanyPhoneNumber),
                    identificationNumberForInvoice = VALUES(identificationNumberForInvoice),
                    lastModified = VALUES(lastModified),
                    technicianFullName = VALUES(technicianFullName),
                    salePriceString = VALUES(salePriceString),
                    netSalePriceString = VALUES(netSalePriceString),
                    activation_date = VALUES(activation_date),
                    activation_time = VALUES(activation_time),
                    installment_date = VALUES(installment_date),
                    installment_time = VALUES(installment_time),
                    hasReceiptInfo = VALUES(hasReceiptInfo),
                    companyTypeStr = VALUES(companyTypeStr),
                    guncellenme_zamani = VALUES(guncellenme_zamani)
            """, (
                kayit_id, kayit.get("licensePlate"), kayit.get("installationCode"), 
                kayit.get("companyName"), kayit.get("ttbServiceName"), 
                kayit.get("vehicleCompanyName"), kayit.get("taxInfoNumber"), 
                kayit.get("taxInfoOffice"), kayit.get("driverEmail"), 
                kayit.get("driverPhoneNumber"), kayit.get("address"), 
                kayit.get("city"), kayit.get("district"), 
                kayit.get("vehicleOrderInstallationStatus"), 
                kayit.get("vehicleOrderInstallationStatusId"), kayit.get("productName"), 
                kayit.get("ttbServiceReferenceNumber"), kayit.get("vehicleCompanyPhoneNumber"), 
                kayit.get("identificationNumberForInvoice"), api_last_modified, 
                kayit.get("technicianFullName"), kayit.get("salePriceString"), 
                kayit.get("netSalePriceString"), parse_date(kayit.get("activationDateString")), 
                parse_time(kayit.get("activationHourString")), 
                parse_date(kayit.get("installmentDateString")), 
                parse_time(kayit.get("installmentHourString")), 
                kayit.get("hasReceiptInfo"), kayit.get("companyTypeStr"), datetime.now()
            ))
            
            processed_count += 1

        db.commit()
        db.close()

        return jsonify({
            "message": "Synchronization completed successfully", 
            "records_processed": processed_count,
            "total_records": len(montajlar)
        })

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

# Flask route for manual triggering
@app.route("/api/synchronize", methods=["GET"])
def synchronize_endpoint():
    """Endpoint for manual synchronization triggers"""
    return senkronize_montajlar()

if __name__ == "__main__":
    app.run(debug=True)