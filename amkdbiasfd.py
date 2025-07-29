from datetime import datetime, timedelta
import random

# Define different types of logs and their respective messages
log_types = {
    "system.log": [
        "Started Network Manager Script Dispatcher Service.",
        "Service only ran for 0 seconds. Pushing respawn out by 10 seconds.",
        "Started Update UTMP about System Boot/Shutdown.",
        "Stopped target Graphical Interface.",
        "Reached target Sleep."
    ],
    "auth.log": [
        "Failed password for root from 192.168.1.101 port 22 ssh2",
        "Accepted password for admin from 10.0.0.5 port 22 ssh2",
        "session opened for user root by (uid=0)",
        "session closed for user admin",
        "sudo:    user : TTY=pts/0 ; PWD=/home/user ; USER=root ; COMMAND=/bin/ls"
    ],
    "kernel.log": [
        "CPU0: Core temperature above threshold, cpu clock throttled",
        "usb 1-1: new high-speed USB device number 3 using xhci_hcd",
        "eth0: Link is Up - 1Gbps/Full - flow control rx/tx",
        "EXT4-fs (sda1): mounted filesystem with ordered data mode",
        "systemd-journald[123]: File /var/log/journal/xyz/system.journal corrupted"
    ],
    "cron.log": [
        "CRON[12345]: (root) CMD (run-parts /etc/cron.hourly)",
        "CRON[23456]: (user) CMD (/usr/bin/python3 /home/user/script.py)",
        "CRON[34567]: (backup) CMD (/usr/local/bin/backup.sh)",
        "CRON[45678]: (daemon) CMD (/bin/sh /etc/cron.daily/logrotate)",
        "CRON[56789]: (nobody) CMD (echo 'hello world')"
    ],
    "network.log": [
        "eth0: Link is Down",
        "eth0: Link is Up",
        "NetworkManager[999]: <info>  [timestamp] device (eth0): state change: disconnected -> prepare",
        "wlan0: deauthenticating from 192.168.1.1 by local choice (Reason: 3=DEAUTH_LEAVING)",
        "dhclient: DHCPREQUEST of 192.168.1.100 on wlan0 to 192.168.1.1 port 67"
    ],
    "boot.log": [
        "Starting Initrd Default Target...",
        "Started Show Plymouth Boot Screen.",
        "Started Forward Password Requests to Plymouth Directory Watch.",
        "Reached target Basic System.",
        "Started Remount Root and Kernel File Systems."
    ],
    "dmesg.log": [
        "[    0.000000] Initializing cgroup subsys cpuset",
        "[    0.004000] smpboot: CPU0: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz",
        "[    1.345678] usb 1-1: new high-speed USB device number 2 using xhci_hcd",
        "[    2.234567] EXT4-fs (sda1): mounted filesystem with ordered data mode",
        "[    3.123456] systemd[1]: Started Journal Service."
    ],
    "secure.log": [
        "sshd[5555]: Accepted password for user1 from 10.0.0.1 port 22 ssh2",
        "sshd[6666]: Failed password for invalid user root from 192.168.0.2 port 22 ssh2",
        "sshd[7777]: Received disconnect from 10.0.0.2: 11: Bye Bye",
        "sudo: pam_unix(sudo:session): session opened for user root by user1(uid=0)",
        "sshd[8888]: Connection closed by authenticating user user1 10.0.0.3 port 22"
    ],
    "xorg.log": [
        "(EE) Failed to load module \"nouveau\" (module does not exist, 0)",
        "(II) NVIDIA(0): Creating default Display subsection in Screen section",
        "(WW) VGA arbiter: cannot open kernel arbiter, no multi-card support",
        "(II) LoadModule: \"glx\"",
        "(--) NVIDIA(0): Valid display device(s) on GPU-0 at PCI:1:0:0"
    ],
    "application.log": [
        "app[1234]: INFO - Application started successfully.",
        "app[1234]: WARNING - Configuration file not found. Using defaults.",
        "app[1234]: ERROR - Database connection failed.",
        "app[1234]: DEBUG - Fetching user data...",
        "app[1234]: INFO - Shutdown complete."
    ]
}

# Generate logs
base_time = datetime.now()

for log_filename, messages in log_types.items():
    with open(log_filename, "w") as log_file:
        for _ in range(100):  # 100 entries per log file
            log_time = base_time - timedelta(seconds=random.randint(0, 86400))
            log_line = f"{log_time.strftime('%b %d %H:%M:%S')} localhost {random.choice(messages)}\n"
            log_file.write(log_line)
