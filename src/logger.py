import logging
import os
from datetime import datetime

# 1. Ensure logs directory
logs_dir = os.path.join(os.getcwd(), "logs")
print(logs_dir)
os.makedirs(logs_dir, exist_ok=True)

# 2. Build log file path
log_file = os.path.join(logs_dir, f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log")

# 3. Setup logging (force=True ensures overwrite if already configured)
logging.basicConfig(
    filename=log_file,
    format="[%(asctime)s] [%(levelname)s] - %(message)s",
    level=logging.INFO,
    force=True  # This is IMPORTANT in VS Code or notebooks
)

# 4. Write a test log
logging.info("This is a test log message.")
print("Logging complete.")
print(f"Expected log path: {log_file}")
print("Log file exists:", os.path.exists(log_file))
