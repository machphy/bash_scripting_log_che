from datetime import datetime, timedelta
import random

# Define different types of logs and their respective messages
log_types = {
    "rajeev.log": [
        "Started Network Manager Script Dispatcher Service.",
        "Service only ran for 0 seconds. Pushing respawn out by 10 seconds.",
        "Started Update UTMP about System Boot/Shutdown.",
        "Stopped target Graphical Interface.",
        "Reached target Sleep.",
        "   Started Session c1 of user rajeev.",
        "   Started Session c2 of user rajeev.",
        "   Started Session c3 of user rajeev.",
        "   Started Session c4 of user rajeev.",
        
    ],
    
}

# Generate logs
base_time = datetime.now()

for log_filename, messages in log_types.items():
    with open(log_filename, "w") as log_file:
        for _ in range(100):  # 100 entries per log file
            log_time = base_time - timedelta(seconds=random.randint(0, 86400))
            log_line = f"{log_time.strftime('%b %d %H:%M:%S')} localhost {random.choice(messages)}\n"
            log_file.write(log_line)
