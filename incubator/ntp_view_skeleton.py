import csv
import os
import socket
import threading
import time
import datetime
import subprocess
import queue
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


# Function to scan network for NTP packets
def scan_network():
    while True:
        # Perform network scanning for NTP packets
        # Modify the code to implement your specific network scanning logic
        # Capture the required packet data and store it in variables
        
        # Check if user wants to exit
        if input("Press 'q' to exit network scanning: ") == 'q':
            break

        # Store the captured packet data in variables
        found_on_ip = "192.168.1.10"
        found_from_ip = "192.168.1.20"
        found_at_time = datetime.datetime.now()
        packet_data = "Sample packet data"

        # Print the captured packet data on the screen
        print(f"Found on: {found_on_ip} | Found from: {found_from_ip} | Found at: {found_at_time} | Packet Data: {packet_data}")

        # Append the captured packet data to the CSV file
        with open("./data/ntp_data.csv", "a") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([f"found_on_({found_on_ip}_{socket.gethostname()}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')})",
                             found_on_ip, found_from_ip, found_at_time, packet_data])


# Function to search through the current line and print the found time
def search_time():
    line = input("Enter the line to search: ")
    # Perform the search logic on the provided line
    # Modify the code to implement your specific search logic
    print("The time found is: NTP from: <IP Address>")


# Function to print all previous entries from the CSV file
def print_previous_entries():
    # Read the CSV file and print all the entries
    with open("./data/ntp_data.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(row)


# Function to print all seen IPs from previous NTP data
def print_seen_ips():
    ips = set()
    # Search through the CSV file and collect all the unique IPs
    with open("./data/ntp_data.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            found_on_ip = row[1]
            ips.add(found_on_ip)
    # Print all the unique IPs
    for ip in ips:
        print(ip)


# Function to show the current clock
def show_clock():
    while True:
        # Scans network for local NTP time
        # Modify the code to implement your specific local NTP scanning logic
        
        # Check if NTP time is found within 5 seconds
        if input("Press 'q' to stop showing the clock: ") == 'q':
            break


# Function to poll the gateway for NTP time
def poll_gateway_ntp():
    # Poll the gateway for NTP time and print each packet sent
    # Modify the code to implement your specific gateway polling logic
        
    # Check if NTP time is found within 1 second
    if input("Press 'q' to exit gateway polling: ") == 'q':
        return

    # Send another poll and print it

    # Check if NTP time is found within 5 seconds
    if input("Press 'q' to exit gateway polling: ") == 'q':
        return


# Function to poll NTP servers in separate threads and display the consensus time
def poll_ntp_servers():
    t1_timeval = None
    t2_timeval = None
    t3_timeval = None
    t4_timeval = None
    t5_timeval = None
    t6_timeval = None
    t7_timeval = None
    consensus_time_is = None

    # Thread function to poll NTP server and store the time value
    def ntp_thread(server, timeval_queue):
        # Perform NTP polling for the specified server
        # Modify the code to implement your specific NTP polling logic
        timeval = "Sample NTP Time Value"
        timeval_queue.put(timeval)

    # Create a queue for storing time values from NTP threads
    timeval_queue = queue.Queue()

    # Create threads to poll NTP servers
    threads = [
        threading.Thread(target=ntp_thread, args=("pool.ntp.org", timeval_queue)),
        threading.Thread(target=ntp_thread, args=("time.nist.gov", timeval_queue)),
        threading.Thread(target=ntp_thread, args=("ptbtime1.ptb.de", timeval_queue)),
        threading.Thread(target=ntp_thread, args=("clock-1.cs.wisc.edu", timeval_queue)),
        threading.Thread(target=ntp_thread, args=("time.berkeley.edu", timeval_queue)),
        threading.Thread(target=ntp_thread, args=("ntp.cam.ac.uk", timeval_queue)),
        threading.Thread(target=ntp_thread, args=("au.pool.ntp.org", timeval_queue)),
        threading.Thread(target=task_master, args=(timeval_queue,))
    ]

    # Start the threads
    for thread in threads:
        thread.start()

    # Wait for all the threads to finish
    for thread in threads:
        thread.join()

    # Function to aggregate the NTP thread results and display the current time
    def task_master(queue):
        # Aggregate the NTP thread results and update consensus time
        # Modify the code to implement your specific aggregation logic

        # Update consensus time and display current time found
        consensus_time_is = "Sample Consensus Time"

        # Open a GTK window and display the time using LED letters
        # Modify the code to implement your specific GUI logic

    # Display the consensus time and GUI

# Main menu loop
while True:
    print("Menu:")
    print("1. Scan network for NTP packets")
    print("2. Search through current line")
    print("3. Print all previous entries")
    print("4. Print all seen IPs from NTPs in the past")
    print("5. Show clock")
    print("6. Poll the gateway for NTP")
    print("7. Poll NTP servers and display consensus time")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        scan_network()
    elif choice == "2":
        search_time()
    elif choice == "3":
        print_previous_entries()
    elif choice == "4":
        print_seen_ips()
    elif choice == "5":
        show_clock()
    elif choice == "6":
        poll_gateway_ntp()
    elif choice == "7":
        poll_ntp_servers()
    elif choice == "8":
        break
    else:
        print("Invalid choice. Please try again.")

print("Program exited.")
