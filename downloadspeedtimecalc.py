import tkinter as tk
from tkinter import ttk
packages = ["idna", "os","sys"]
# Conversion factor for bits to megabits
bits_to_megabits = 1 / 1e6

# Conversion factors for different download speed units to Mbps
speed_units = {
    "bps": 1 / 1e6,     # Convert bits per second to megabits per second
    "Kbps": 1 / 1e3,    # Convert kilobits per second to megabits per second
    "Mbps": 1,          # Keep megabits per second as is
    "Gbps": 1e3,        # Convert gigabits per second to megabits per second
}

# Conversion factors for different file size units to MB
size_units = {
    "B": 1 / 1024 / 1024,   # Convert bytes to MB
    "KB": 1 / 1024,         # Convert kilobytes to MB
    "MB": 1,                # Keep megabytes as is
    "GB": 1024,             # Convert gigabytes to MB
    "TB": 1024 * 1024,      # Convert terabytes to MB
    "b": 8 / 1024 / 1024,   # Convert bits to MB
    "Kb": 8 / 1024,         # Convert kilobits to MB
    "Gb": 1024 * 8,         # Convert gigabits to MB
    "Tb": 1024 * 1024 * 8,  # Convert terabits to MB
}

def calculate_download_time():
    try:
        file_size = float(file_size_entry.get())  # File size
        selected_file_unit = size_unit_combobox.get()
        download_speed = float(download_speed_entry.get())  # Download speed in Mbps
        selected_speed_unit = speed_unit_combobox.get()
        
        # Convert file size to MB
        file_size_in_mb = file_size * size_units[selected_file_unit]
        
        # Convert download speed to Mbps
        download_speed_mbps = download_speed * speed_units[selected_speed_unit]
        
        # Calculate download time in seconds
        download_time = file_size_in_mb * 8 / download_speed_mbps  # Bits to Mbps
        
        # Convert seconds to hours, minutes, and seconds
        hours, remainder = divmod(download_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        result_label.config(text=f"Download Time: {int(hours)}h {int(minutes)}m {int(seconds)}s")
    except ValueError:
        result_label.config(text="Please enter valid numbers for File Size and Download Speed.")

def main():
    # Create the main tkinter window
    window = tk.Tk()
    window.title("Download Time Calculator")

    # Configure background and text colors
    window.configure(bg="white")  # Set background color to white
    
    # Create and place input labels and entry fields using grid
    file_size_label = tk.Label(window, text="File Size:", bg="white", fg="purple")
    file_size_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    
    global file_size_entry
    file_size_entry = tk.Entry(window)
    file_size_entry.grid(row=0, column=1, padx=10, pady=5)
    
    size_unit_label = tk.Label(window, text="Unit:", bg="white", fg="purple")
    size_unit_label.grid(row=0, column=2, padx=10, pady=5, sticky="w")

    # Create a dropdown menu for selecting the file size unit
    size_units_list = ["B", "KB", "MB", "GB", "TB", "b", "Kb", "Gb", "Tb"]
    global size_unit_combobox
    size_unit_combobox = ttk.Combobox(window, values=size_units_list)
    size_unit_combobox.set("MB")  # Set the default unit to MB
    size_unit_combobox.grid(row=0, column=3, padx=10, pady=5)

    download_speed_label = tk.Label(window, text="Download Speed:", bg="white", fg="purple")
    download_speed_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    
    global download_speed_entry
    download_speed_entry = tk.Entry(window)
    download_speed_entry.grid(row=1, column=1, padx=10, pady=5)
    
    speed_unit_label = tk.Label(window, text="Unit:", bg="white", fg="purple")
    speed_unit_label.grid(row=1, column=2, padx=10, pady=5, sticky="w")

    # Create a dropdown menu for selecting the download speed unit
    speed_units_list = ["bps", "Kbps", "Mbps", "Gbps"]
    global speed_unit_combobox
    speed_unit_combobox = ttk.Combobox(window, values=speed_units_list)
    speed_unit_combobox.set("Mbps")  # Set the default unit to Mbps
    speed_unit_combobox.grid(row=1, column=3, padx=10, pady=5)

    # Create the Calculate button
    calculate_button = tk.Button(window, text="Calculate", command=calculate_download_time, bg="purple", fg="white")
    calculate_button.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

    # Create and place the result label
    global result_label
    result_label = tk.Label(window, text="", bg="white", fg="purple")
    result_label.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

    # Set column weights to make widgets expand proportionally
    for col in range(4):
        window.grid_columnconfigure(col, weight=1)

    # Start the tkinter main loop
    window.mainloop()

if __name__ == "__main__":
    main()
