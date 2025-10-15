import schedule
import time
from main import senkronize_montajlar  # Production: Import from main application
# For GitHub demo: Use the template instead
# from data_synchronization_template import senkronize_montajlar
from datetime import datetime

def job():
    print(f"\n⏰ [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Senkronizasyon başlatıldı...")
    result = senkronize_montajlar()
    print("✅ Sonuç:", result)

# Call every 30 minutes
schedule.every(30).minutes.do(job)

print("🟢 Senkronizasyon servisi başlatıldı. Her 30 dakikada bir çalışacak...\n")

# Perform first sync immediately
job()

# Infinite loop
while True:
    schedule.run_pending()
    time.sleep(1)
    