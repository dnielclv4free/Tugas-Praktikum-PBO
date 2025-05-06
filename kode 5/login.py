import tkinter as tk
from tkinter import messagebox

class LoginApp:
    def __init__(self, root):
        """Inisialisasi aplikasi login dengan Tkinter"""
        self.root = root
        self.root.title("Login Application")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        # Database pengguna sederhana (username: password)
        self.users = {
            "admin": "1234",
            "daniel": "1234"
        }
        
        self.create_widgets()
    
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
        
        # Label dan input langsung untuk username
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
        
        # Label dan input langsung untuk password
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
            width=10
        )
        self.login_button.grid(row=0, column=0, padx=10)
        
        # Tombol reset
        self.reset_button = tk.Button(
            self.button_frame,
            text="Reset",
            font=("Arial", 12),
            command=self.reset_form,
            bg="#f44336",
            fg="white",
            width=10
        )
        self.reset_button.grid(row=0, column=1, padx=10)
        
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
            if self.users[username] == password:
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
