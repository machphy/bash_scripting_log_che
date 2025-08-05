echo "📁 Finding .log files modified in the last 1 day..."
find . -name "*.log" -mtime -1

echo -e "\n🔍 Checking for 'ERROR' in application.log:"
grep "ERROR" application.log

echo -e "\n🔢 Total 'ERROR' count in application.log:"
grep -c "ERROR" application.log

echo -e "\n🔢 Total 'FATAL' count in application.log:"
grep -c "FATAL" application.log

echo -e "\n🔢 Total 'FATAL' count in system.log:"
grep -c "FATAL" system.log

echo -e "\n🔢 Total 'CRITICAL' count in system.log:"
grep -c "CRITICAL" system.log

echo -e "\n🔍 Showing all 'CRITICAL' lines in system.log:"
grep "CRITICAL" system.log