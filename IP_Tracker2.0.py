import tkinter as tk
from tkinter import scrolledtext
import json
import requests
import random

Bl = '\033[30m'  
Re = '\033[1;31m'
Gr = '\033[1;32m'
Ye = '\033[1;33m'
Blu = '\033[1;34m'
Mage = '\033[1;35m'
Cy = '\033[1;36m'
Wh = '\033[1;37m'
# Function to clear the GUI output
def clear_output():
    output_box.delete(1.0, tk.END)

# Function to display the main menu
def main_menu():
    clear_output()
    output_box.insert(tk.END, "----------- Options -----------\n")
    output_box.insert(tk.END, "[1] Track Any IP Address\n")
    output_box.insert(tk.END, "[2] Show Your IP Address\n")
    output_box.insert(tk.END, "[3] Exit\n")
    output_box.insert(tk.END, "===============================\n")
    output_box.insert(tk.END, "What can I do for you?\n")
    submit_button.config(command=handle_command)

# Function to handle user commands
# Function to handle user commands
def handle_command():
    command = input_field.get()
    input_field.delete(0, tk.END)  # Clear the input field
    if command == "1":
        clear_output()
        output_box.insert(tk.END, "Enter the IP address to track:\n")
        submit_button.config(command=track_ip)
    elif command == "2":
        clear_output()
        show_ip()
    elif command == "3":
        clear_output()
        output_box.insert(tk.END, "Exiting... Bye!\n")
        root.after(2000, root.destroy)  # Close the GUI after 2 seconds
    else:
        clear_output()
        output_box.insert(tk.END, "Invalid option. Please try again.\n")
        main_menu()

# Bind the "Enter" key to the handle_command function

# Function to track an IP address
def track_ip():
    ip = input_field.get()
    input_field.delete(0, tk.END)  # Clear the input field
    clear_output()

    try:
        output_box.insert(tk.END, f"Tracking IP: {ip}\n")
        req_api = requests.get(f"http://ipwho.is/{ip}")
        ip_data = json.loads(req_api.text)

        if ip_data.get("success") is False:
            output_box.insert(tk.END, f"Error: {ip_data.get('message')}\n")
            return_to_menu()
            return

        lat = ip_data['latitude']
        lon = ip_data['longitude']

        # Display the information
        output_box.insert(tk.END, f"=====Location=====\n")
        output_box.insert(tk.END, f"Latitude: {lat}\n")
        output_box.insert(tk.END, f"Longitude: {lon}\n")
        output_box.insert(tk.END, f"Maps: https://www.google.com/maps/@{lat},{lon},8z\n")
        output_box.insert(tk.END, f"Country: {ip_data['country']}\n")
        output_box.insert(tk.END, f"\n")
        output_box.insert(tk.END, f"====General Location ===\n")
        output_box.insert(tk.END, f" Continent Code  :", ip_data["continent_code"])
        output_box.insert(tk.END, f"Continent: {ip_data['continent']}\n")
        output_box.insert(tk.END, f"Region: {ip_data['region']}\n")
        output_box.insert(tk.END, f"\n")
        output_box.insert(tk.END, f"======Time Zone ======\n")
        output_box.insert(tk.END,f" ID              :{ip_data["timezone"]["id"]}\n")
        output_box.insert(tk.END,f" ABBR            :{ip_data["timezone"]["abbr"]}\n")
        output_box.insert(tk.END,f" DST             :{ip_data["timezone"]["is_dst"]}\n")
        output_box.insert(tk.END,f" Offset          :{ip_data["timezone"]["offset"]}\n")
        output_box.insert(tk.END,f" UTC             :{ip_data["timezone"]["utc"]}\n")
        output_box.insert(tk.END,f" Current Time    :{ip_data["timezone"]["current_time"]}\n")
        output_box.insert(tk.END, f"\n")
        output_box.insert(tk.END, f"===========Connection============\n")
        output_box.insert(tk.END, f" ASN             :{ip_data["connection"]["asn"]}\n")
        output_box.insert(tk.END, f" ORG             :{ip_data["connection"]["org"]}\n")
        output_box.insert(tk.END, f" ISP             :{ip_data["connection"]["isp"]}\n")
        output_box.insert(tk.END, f" Domain          :{ip_data["connection"]["domain"]}\n") 
        
    except requests.exceptions.RequestException as e:
        output_box.insert(tk.END, f"Error: {e}\n")
    except KeyError:
        output_box.insert(tk.END, "Invalid IP address\n")
    except json.JSONDecodeError:
        output_box.insert(tk.END, "Error decoding JSON response\n")
    except Exception as e:
        output_box.insert(tk.END, f"An unexpected error occurred: {e}\n")
    finally:
        return_to_menu()

# Function to show the user's IP address
def show_ip():
    try:
        response = requests.get('https://api.ipify.org/')
        show_ip = response.text

        output_box.insert(tk.END, "========== SHOW INFORMATION YOUR IP ==========\n")
        output_box.insert(tk.END, f"Your IP Address: {show_ip}\n")
        output_box.insert(tk.END, "==============================================\n")
    except requests.exceptions.RequestException as e:
        output_box.insert(tk.END, f"Error: {e}\n")
    except Exception as e:
        output_box.insert(tk.END, f"An unexpected error occurred: {e}\n")
    finally:
        return_to_menu()

# Function to return to the main menu
def return_to_menu():
    output_box.insert(tk.END, "\nPress Enter to return to the main menu...\n")
    submit_button.config(command=main_menu)

# Function to create the particle effect
def create_particles():
    for _ in range(5):  # Create 5 particles per frame
        x = random.randint(0, canvas.winfo_width())
        y = random.randint(0, canvas.winfo_height())
        size = random.randint(2, 5)
        particle = canvas.create_oval(x, y, x + size, y + size, fill="orange", outline="")
        particles.append((particle, random.randint(-2, 2), random.randint(-2, 2)))

    # Update particle positions
    for particle, dx, dy in particles:
        canvas.move(particle, dx, dy)
        x1, y1, x2, y2 = canvas.coords(particle)
        if x1 < 0 or x2 > canvas.winfo_width() or y1 < 0 or y2 > canvas.winfo_height():
            canvas.delete(particle)
            particles.remove((particle, dx, dy))

    root.after(50, create_particles)  # Repeat every 50ms

# Create the main window
root = tk.Tk()
root.title("IP Tracker")
root.geometry("800x600")

# Create a canvas for the background
canvas = tk.Canvas(root, bg="black", highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

# Create a frame for the GUI elements
frame = tk.Frame(root, bg="black")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Bind the "Enter" key to the handle_command function

# Output box
output_box = scrolledtext.ScrolledText(frame, width=60, height=20, bg="black", fg="orange", insertbackground="orange")
output_box.pack(pady=10)

# Input field
input_field = tk.Entry(frame, width=50, bg="black", fg="orange", insertbackground="orange")
input_field.pack(pady=5)


# Submit button
submit_button = tk.Button(frame, text="Submit", command=handle_command, bg="orange", fg="black")
submit_button.pack(pady=5)

# Particle list
particles = []

# Start the particle effect
create_particles()

# Display the main menu when the program starts
main_menu()

# Run the GUI event loop
root.mainloop()