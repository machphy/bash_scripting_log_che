find . -name "*.log" -mtime -1
grep "ERROR" application.log
grep -c "ERROR" application.log
grep -c "FATAL" application.log
grep -c "FATAL" system.log
grep -c "CRITICAL" system.log
grep "CRITICAL" system.log
grep -c "CRITICAL" application.log