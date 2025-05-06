import tkinter as tk
from tkinter import messagebox
import re
import json
import os

class LoginApp:
    def __init__(self, root):
        """Inisialisasi aplikasi login dengan Tkinter"""
        self.root = root
        self.root.title("Login Application")
        self.root.geometry("400x350")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        # Coba load user data dari file
        self.users_file = "users.json"
        self.load_users()
        
        self.create_widgets()
    
    def load_users(self):
        """Load user data dari file JSON jika ada, jika tidak buat default"""
        try:
            if os.path.exists(self.users_file):
                with open(self.users_file, "r") as file:
                    self.users = json.load(file)
            else:
                # Default users jika file tidak ada
                self.users = {
                    "admin": {"password": "admin123", "email": "admin@example.com"},
                    "user": {"password": "user123", "email": "user@example.com"}
                }
                # Simpan default users ke file
                self.save_users()
        except Exception as e:
            messagebox.showerror("Error", f"Gagal memuat data pengguna: {str(e)}")
            # Fallback ke default users
            self.users = {
                "admin": {"password": "admin123", "email": "admin@example.com"},
                "user": {"password": "user123", "email": "user@example.com"}
            }
    
    def save_users(self):
        """Simpan user data ke file JSON"""
        try:
            with open(self.users_file, "w") as file:
                json.dump(self.users, file, indent=4)
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menyimpan data pengguna: {str(e)}")
    
    def create_widgets(self):
        """Membuat widget-widget untuk form login"""
        # Frame utama
        self.main_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.main_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Judul
        self.title_label = tk.Label(
            self.main_frame, 
            text="Login System", 
            font=("Arial", 18, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        self.title_label.pack(pady=10)
        
        # Frame untuk input
        self.input_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.input_frame.pack(pady=20)
        
        # Label dan input untuk username
        tk.Label(
            self.input_frame, 
            text="Username:", 
            font=("Arial", 12),
            bg="#f0f0f0",
            anchor="w",
            width=10
        ).grid(row=0, column=0, sticky="w", pady=5)
        
        self.username_entry = tk.Entry(
            self.input_frame, 
            font=("Arial", 12),
            width=20
        )
        self.username_entry.grid(row=0, column=1, pady=5)
        
        # Label dan input untuk password
        tk.Label(
            self.input_frame, 
            text="Password:", 
            font=("Arial", 12),
            bg="#f0f0f0",
            anchor="w",
            width=10
        ).grid(row=1, column=0, sticky="w", pady=5)
        
        self.password_entry = tk.Entry(
            self.input_frame, 
            font=("Arial", 12),
            width=20,
            show="*"
        )
        self.password_entry.grid(row=1, column=1, pady=5)
        
        # Frame untuk tombol
        self.button_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.button_frame.pack(pady=10)
        
        # Tombol login
        self.login_button = tk.Button(
            self.button_frame,
            text="Login",
            font=("Arial", 12),
            command=self.validate_login,
            bg="#4CAF50",
            fg="white",
            width=8
        )
        self.login_button.grid(row=0, column=0, padx=5)
        
        # Tombol reset
        self.reset_button = tk.Button(
            self.button_frame,
            text="Reset",
            font=("Arial", 12),
            command=self.reset_form,
            bg="#f44336",
            fg="white",
            width=8
        )
        self.reset_button.grid(row=0, column=1, padx=5)
        
        # Tombol register
        self.register_button = tk.Button(
            self.button_frame,
            text="Register",
            font=("Arial", 12),
            command=self.open_register_window,
            bg="#2196F3",
            fg="white",
            width=8
        )
        self.register_button.grid(row=0, column=2, padx=5)
        
        # Status label
        self.status_label = tk.Label(
            self.main_frame,
            text="",
            font=("Arial", 10),
            fg="#666666",
            bg="#f0f0f0"
        )
        self.status_label.pack(pady=10)
        
        # Bind Enter key to login button
        self.root.bind('<Return>', lambda event: self.validate_login())
        
        # Set focus ke username entry
        self.username_entry.focus()
    
    def validate_login(self):
        """Validasi login pengguna"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Validasi sederhana - hanya cek jika kosong
        if not username or not password:
            self.status_label.config(text="Username dan password tidak boleh kosong!")
            return
        
        # Cek apakah username ada di database
        if username in self.users:
            # Cek apakah password benar
            if self.users[username]["password"] == password:
                messagebox.showinfo("Login Berhasil", f"Selamat datang, {username}!")
                self.show_welcome_page(username)
            else:
                self.status_label.config(text="Password salah!")
        else:
            self.status_label.config(text="Username tidak ditemukan!")
    
    def reset_form(self):
        """Reset form ke keadaan awal"""
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.status_label.config(text="")
        self.username_entry.focus()
    
    def open_register_window(self):
        """Buka window register baru"""
        register_window = tk.Toplevel(self.root)
        register_window.title("Register New User")
        register_window.geometry("450x400")
        register_window.resizable(False, False)
        register_window.configure(bg="#f0f0f0")
        register_window.transient(self.root)  # Set window to be on top of main window
        register_window.grab_set()  # Make window modal
        
        # Frame utama
        main_frame = tk.Frame(register_window, bg="#f0f0f0")
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Judul
        title_label = tk.Label(
            main_frame, 
            text="Register New User", 
            font=("Arial", 18, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        title_label.pack(pady=10)
        
        # Frame untuk input
        input_frame = tk.Frame(main_frame, bg="#f0f0f0")
        input_frame.pack(pady=15)
        
        # Label dan input untuk username
        tk.Label(
            input_frame, 
            text="Username:", 
            font=("Arial", 12),
            bg="#f0f0f0",
            anchor="w",
            width=12
        ).grid(row=0, column=0, sticky="w", pady=5)
        
        username_entry = tk.Entry(
            input_frame, 
            font=("Arial", 12),
            width=25
        )
        username_entry.grid(row=0, column=1, pady=5)
        
        # Label dan input untuk email
        tk.Label(
            input_frame, 
            text="Email:", 
            font=("Arial", 12),
            bg="#f0f0f0",
            anchor="w",
            width=12
        ).grid(row=1, column=0, sticky="w", pady=5)
        
        email_entry = tk.Entry(
            input_frame, 
            font=("Arial", 12),
            width=25
        )
        email_entry.grid(row=1, column=1, pady=5)
        
        # Label dan input untuk password
        tk.Label(
            input_frame, 
            text="Password:", 
            font=("Arial", 12),
            bg="#f0f0f0",
            anchor="w",
            width=12
        ).grid(row=2, column=0, sticky="w", pady=5)
        
        password_entry = tk.Entry(
            input_frame, 
            font=("Arial", 12),
            width=25,
            show="*"
        )
        password_entry.grid(row=2, column=1, pady=5)
        
        # Label dan input untuk confirm password
        tk.Label(
            input_frame, 
            text="Confirm Pass:", 
            font=("Arial", 12),
            bg="#f0f0f0",
            anchor="w",
            width=12
        ).grid(row=3, column=0, sticky="w", pady=5)
        
        confirm_pass_entry = tk.Entry(
            input_frame, 
            font=("Arial", 12),
            width=25,
            show="*"
        )
        confirm_pass_entry.grid(row=3, column=1, pady=5)
        
        # Status label
        status_label = tk.Label(
            main_frame,
            text="",
            font=("Arial", 10),
            fg="#666666",
            bg="#f0f0f0"
        )
        status_label.pack(pady=5)
        
        # Frame untuk tombol
        button_frame = tk.Frame(main_frame, bg="#f0f0f0")
        button_frame.pack(pady=10)
        
        # Fungsi untuk handle registrasi
        def register_user():
            username = username_entry.get()
            email = email_entry.get()
            password = password_entry.get()
            confirm_pass = confirm_pass_entry.get()
            
            # Validasi input
            if not username or not email or not password or not confirm_pass:
                status_label.config(text="Semua field harus diisi!")
                return
            
            # Validasi format username
            if not re.match(r'^[a-zA-Z0-9_]+$', username):
                status_label.config(text="Username hanya boleh berisi huruf, angka, dan underscore!")
                return
            
            # Validasi format email
            if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
                status_label.config(text="Format email tidak valid!")
                return
            
            # Validasi password match
            if password != confirm_pass:
                status_label.config(text="Password tidak cocok!")
                return
            
            # Validasi kekuatan password (minimal 6 karakter)
            if len(password) < 6:
                status_label.config(text="Password harus minimal 6 karakter!")
                return
            
            # Cek username sudah ada
            if username in self.users:
                status_label.config(text="Username sudah digunakan!")
                return
            
            # Tambahkan user baru
            self.users[username] = {
                "password": password,
                "email": email
            }
            self.save_users()  # Simpan ke file
            
            messagebox.showinfo("Register Berhasil", "Registrasi berhasil! Silakan login dengan akun baru.")
            register_window.destroy()  # Tutup window register
        
        # Tombol register
        register_button = tk.Button(
            button_frame,
            text="Register",
            font=("Arial", 12),
            command=register_user,
            bg="#2196F3",
            fg="white",
            width=10
        )
        register_button.grid(row=0, column=0, padx=10)
        
        # Tombol cancel
        cancel_button = tk.Button(
            button_frame,
            text="Cancel",
            font=("Arial", 12),
            command=register_window.destroy,
            bg="#f44336",
            fg="white",
            width=10
        )
        cancel_button.grid(row=0, column=1, padx=10)
        
        # Set focus ke username entry
        username_entry.focus()
    
    def show_welcome_page(self, username):
        """Menampilkan halaman selamat datang setelah login berhasil"""
        # Hapus semua widget dari root
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Buat halaman welcome
        welcome_frame = tk.Frame(self.root, bg="#f0f0f0")
        welcome_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Welcome message
        welcome_label = tk.Label(
            welcome_frame,
            text=f"Selamat Datang, {username}!",
            font=("Arial", 18, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        welcome_label.pack(pady=20)
        
        # Info user
        user_info_frame = tk.Frame(welcome_frame, bg="#f0f0f0")
        user_info_frame.pack(pady=10)
        
        # Tampilkan info user
        tk.Label(
            user_info_frame,
            text=f"Username: {username}",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#333333",
            anchor="w"
        ).pack(fill="x", pady=2)
        
        tk.Label(
            user_info_frame,
            text=f"Email: {self.users[username]['email']}",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#333333",
            anchor="w"
        ).pack(fill="x", pady=2)
        
        # Pesan berhasil login
        message_label = tk.Label(
            welcome_frame,
            text="Login berhasil. Anda telah masuk ke sistem.",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#333333"
        )
        message_label.pack(pady=10)
        
        # Tombol logout
        logout_button = tk.Button(
            welcome_frame,
            text="Logout",
            font=("Arial", 12),
            command=self.logout,
            bg="#f44336",
            fg="white",
            width=10
        )
        logout_button.pack(pady=20)
    
    def logout(self):
        """Kembali ke halaman login"""
        # Hapus semua widget dari root
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Kembalikan ke halaman login
        self.__init__(self.root)


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
