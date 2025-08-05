
echo "analyzing logs for recent changes..." 
find . -name "*.log" -mtime -1

echo "Searching for specific log entries..."
grep "ERROR" application.log
echo "Count of ERROR entries in application.log:"
grep -c "ERROR" application.log
echo "Searching for specific log entries in system.log..."
grep -c "FATAL" application.log

echo "Count of FATAL entries in application.log:"
grep -c "FATAL" system.log
echo "Searching for CRITICAL entries in system.log..."
grep -c "CRITICAL" system.log
echo "Count of CRITICAL entries in system.log:"
grep "CRITICAL" system.log
