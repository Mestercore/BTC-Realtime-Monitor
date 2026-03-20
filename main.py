import requests
import time
from datetime import datetime


url = "YOUR_API_ENDPOINT_HERE" 
memory = 0
log_file = "trading_log.txt"

print("🚀 Bot Started... Logging to:", log_file)

while True:
    try:
        
        data = requests.get(url).json()
        current_price = float(data['data']['amount'])
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_message = f"[{now}] Price: ${current_price}"
        action = "WAITING"

        if memory > 0:
            diff = current_price - memory
            percent = (diff / memory) * 100
            log_message += f" | Change: {percent:.4f}%"

            if percent > 0.01:
                action = "STRONG BUY 🚀"
            elif percent < -0.01:
                action = "STRONG SELL 📉"
            else:
                action = "HOLD ⚖️"

        
        print(f"{log_message} | Action: {action}")

        
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"{log_message} | Action: {action}\n")

        memory = current_price
        
    except Exception as e:
        print(f"❌ Error: {e}")

    time.sleep(10)
