#!/bin/bash

echo "================================="
echo " SRE Linux Diagnostics"
echo "================================="

echo ""
echo "Hostname:"
hostname

echo ""
echo "Uptime:"
uptime

echo ""
echo "CPU:"
top -bn1 | head -n 5

echo ""
echo "Memory:"
free -h

echo ""
echo "Disk:"
df -h

echo ""
echo "Top Processes:"
ps aux --sort=-%cpu | head -n 10

echo ""
echo "Network:"
ip -brief address

echo ""
echo "Listening Ports:"
ss -tuln

echo ""
echo "Diagnostics completed."
