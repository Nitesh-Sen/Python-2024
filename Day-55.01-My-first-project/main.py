import tkinter as tk
from tkinter import messagebox, filedialog
import paramiko

def connect_and_execute():
    hostname = hostname_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    command = command_entry.get()

    if not hostname or not username or not password or not command:
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        # Establish SSH connection
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, username=username, password=password)

        # Execute command
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode()
        error = stderr.read().decode()

        # Clear and display output or error
        result_text.delete(1.0, tk.END)
        if output:
            result_text.insert(tk.END, output)
        if error:
            result_text.insert(tk.END, error)

        ssh.close()
    except Exception as e:
        messagebox.showerror("Connection Error", str(e))

def select_icon():
    file_path = filedialog.askopenfilename(filetypes=[("Icon Files", ".ico")])
    if file_path:
        root.iconbitmap(file_path)

# Create the main window
root = tk.Tk()
root.title("SSH Client")
root.geometry("500x400")

# Add an icon
try:
    root.iconbitmap("default.ico")  # Replace with your .ico file path
except Exception as e:
    print(f"Icon Error: {e}")

# Hostname
tk.Label(root, text="Hostname:").grid(row=0, column=0, padx=10, pady=10)
hostname_entry = tk.Entry(root, width=40)
hostname_entry.grid(row=0, column=1, padx=10, pady=10)

# Username
tk.Label(root, text="Username:").grid(row=1, column=0, padx=10, pady=10)
username_entry = tk.Entry(root, width=40)
username_entry.grid(row=1, column=1, padx=10, pady=10)

# Password
tk.Label(root, text="Password:").grid(row=2, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, show="*", width=40)
password_entry.grid(row=2, column=1, padx=10, pady=10)

# Command
tk.Label(root, text="Command:").grid(row=3, column=0, padx=10, pady=10)
command_entry = tk.Entry(root, width=40)
command_entry.grid(row=3, column=1, padx=10, pady=10)

# Execute Button
execute_button = tk.Button(root, text="Execute", command=connect_and_execute)
execute_button.grid(row=4, column=0, columnspan=2, pady=10)

# Result Text Area
tk.Label(root, text="Result:").grid(row=5, column=0, padx=10, pady=10)
result_text = tk.Text(root, height=10, width=50)
result_text.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Add Icon Button
icon_button = tk.Button(root, text="Set Icon", command=select_icon)
icon_button.grid(row=7, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
