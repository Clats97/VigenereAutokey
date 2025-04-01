import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkFont

def encrypt(text: str, keyword: str) -> str:
    plaintext_alpha = [c for c in text if c.isalpha()]
    if len(plaintext_alpha) <= len(keyword):
        effective_key = keyword[:len(plaintext_alpha)]
    else:
        effective_key = keyword + ''.join(plaintext_alpha)[:len(plaintext_alpha) - len(keyword)]
    
    result = []
    letter_count = 0 
    for char in text:
        if char.isalpha():
            shift = ord(effective_key[letter_count]) - ord('A')
            encrypted_char = chr((ord(char.upper()) - ord('A') + shift) % 26 + ord('A'))
            result.append(encrypted_char)
            letter_count += 1
        else:
            result.append(char)
    return "".join(result)

def decrypt(cipher_text: str, keyword: str) -> str:
    effective_key = list(keyword) 
    result = []
    letter_count = 0  
    for char in cipher_text:
        if char.isalpha():
            shift = ord(effective_key[letter_count]) - ord('A')
            plain_char = chr((ord(char.upper()) - ord('A') - shift + 26) % 26 + ord('A'))
            result.append(plain_char)
            effective_key.append(plain_char) 
            letter_count += 1
        else:
            result.append(char)
    return "".join(result)

class App:
    def __init__(self, master):
        self.master = master
        master.title("Encryption/Decryption App")
        master.geometry("900x600")
        self.mono_font = tkFont.Font(family="Courier New", size=10)
        self.main_frame = tk.Frame(master)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        ascii_art_text = (
            "██╗   ██╗██╗ ██████╗ ███████╗███╗   ██╗███████╗██████╗ ███████╗     █████╗ ██╗   ██╗████████╗ ██████╗ \n"
            "██║   ██║██║██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔════╝    ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗\n"
            "██║   ██║██║██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝█████╗      ███████║██║   ██║   ██║   ██║   ██║\n"
            "╚██╗ ██╔╝██║██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══╝      ██╔══██║██║   ██║   ██║   ██║   ██║\n"
            " ╚████╔╝ ██║╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║███████╗    ██║  ██║╚██████╔╝   ██║   ╚██████╔╝\n"
            "  ╚═══╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ \n"
            "                                                                                                      \n"
            "██╗  ██╗███████╗██╗   ██╗     ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗                               \n"
            "██║ ██╔╝██╔════╝╚██╗ ██╔╝    ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗                              \n"
            "█████╔╝ █████╗   ╚████╔╝     ██║     ██║██████╔╝███████║█████╗  ██████╔╝                              \n"
            "██╔═██╗ ██╔══╝    ╚██╔╝      ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗                              \n"
            "██║  ██╗███████╗   ██║       ╚██████╗██║██║     ██║  ██║███████╗██║  ██║                              \n"
            "╚═╝  ╚═╝╚══════╝   ╚═╝        ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                              \n"
        )
        self.ascii_label = tk.Label(self.main_frame, text=ascii_art_text, fg="red", font=self.mono_font, justify="left")
        self.ascii_label.pack(pady=10)
        self.info_frame = tk.Frame(self.main_frame)
        self.info_frame.pack(fill=tk.X, pady=10)
        self.info_frame.grid_columnconfigure(0, weight=1)
        self.info_frame.grid_columnconfigure(1, weight=1)
        self.title_label = tk.Label(self.info_frame, text="P O L Y A L P H A B E T I C    T E X T    C I P H E R", fg="blue", font=("Arial", 14))
        self.title_label.grid(row=0, column=0, sticky="e")
        self.version_label = tk.Label(self.info_frame, text="Version 1.00", fg="red", font=("Arial", 14))
        self.version_label.grid(row=0, column=1, sticky="w", padx=10)
        self.credit_label = tk.Label(self.main_frame, text="By Joshua M Clatney - Ethical Pentesting Enthusiast", fg="black", font=("Arial", 12))
        self.credit_label.pack(pady=5)
        self.encrypt_button = tk.Button(self.main_frame, text="Encrypt Text", command=self.open_encrypt_window, width=20, height=2)
        self.encrypt_button.pack(pady=10)
        self.decrypt_button = tk.Button(self.main_frame, text="Decrypt Text", command=self.open_decrypt_window, width=20, height=2)
        self.decrypt_button.pack(pady=10)
    
    def open_encrypt_window(self):
        encrypt_win = tk.Toplevel(self.master)
        encrypt_win.title("Encrypt Text")
        encrypt_win.geometry("500x400")
        tk.Label(encrypt_win, text="Enter text to encrypt:", font=("Arial", 12)).pack(pady=5)
        input_frame = tk.Frame(encrypt_win)
        input_frame.pack(pady=5)
        text_entry = tk.Text(input_frame, height=5, width=40)
        text_entry.grid(row=0, column=0)
        paste_button = tk.Button(input_frame, text="Paste", 
                                 command=lambda: text_entry.insert(tk.END, encrypt_win.clipboard_get()))
        paste_button.grid(row=0, column=1, padx=5)
        tk.Label(encrypt_win, text="Enter keyword:", font=("Arial", 12)).pack(pady=5)
        keyword_entry = tk.Entry(encrypt_win, width=30)
        keyword_entry.pack(pady=5)
        tk.Label(encrypt_win, text="Encrypted text:", font=("Arial", 12)).pack(pady=5)
        result_frame = tk.Frame(encrypt_win)
        result_frame.pack(pady=5)
        result_text = tk.Text(result_frame, height=5, width=40)
        result_text.grid(row=0, column=0)
        copy_button = tk.Button(result_frame, text="Copy", 
                                command=lambda: (encrypt_win.clipboard_clear(),
                                                 encrypt_win.clipboard_append(result_text.get("1.0", tk.END))))
        copy_button.grid(row=0, column=1, padx=5)
        
        def do_encrypt():
            text = text_entry.get("1.0", tk.END).strip().upper()
            keyword = keyword_entry.get().replace(" ", "").upper()
            if not any(c.isalpha() for c in text):
                messagebox.showerror("Error", "Text must contain at least one alphabetic character.")
                return
            if not keyword.isalpha() or keyword == "":
                messagebox.showerror("Error", "Keyword must consist of alphabetic characters only.")
                return
            encrypted = encrypt(text, keyword)
            result_text.config(state=tk.NORMAL)
            result_text.delete("1.0", tk.END)
            result_text.insert(tk.END, encrypted)
            result_text.config(state=tk.DISABLED)
        
        tk.Button(encrypt_win, text="Encrypt", command=do_encrypt, width=20).pack(pady=10)
    
    def open_decrypt_window(self):
        decrypt_win = tk.Toplevel(self.master)
        decrypt_win.title("Decrypt Text")
        decrypt_win.geometry("500x400")
        tk.Label(decrypt_win, text="Enter text to decrypt:", font=("Arial", 12)).pack(pady=5)
        input_frame = tk.Frame(decrypt_win)
        input_frame.pack(pady=5)
        text_entry = tk.Text(input_frame, height=5, width=40)
        text_entry.grid(row=0, column=0)
        paste_button = tk.Button(input_frame, text="Paste", 
                                 command=lambda: text_entry.insert(tk.END, decrypt_win.clipboard_get()))
        paste_button.grid(row=0, column=1, padx=5)
        tk.Label(decrypt_win, text="Enter keyword:", font=("Arial", 12)).pack(pady=5)
        keyword_entry = tk.Entry(decrypt_win, width=30)
        keyword_entry.pack(pady=5)
        tk.Label(decrypt_win, text="Decrypted text:", font=("Arial", 12)).pack(pady=5)
        result_frame = tk.Frame(decrypt_win)
        result_frame.pack(pady=5)
        result_text = tk.Text(result_frame, height=5, width=40)
        result_text.grid(row=0, column=0)
        copy_button = tk.Button(result_frame, text="Copy", 
                                command=lambda: (decrypt_win.clipboard_clear(),
                                                 decrypt_win.clipboard_append(result_text.get("1.0", tk.END))))
        copy_button.grid(row=0, column=1, padx=5)
        
        def do_decrypt():
            text = text_entry.get("1.0", tk.END).strip().upper()
            keyword = keyword_entry.get().replace(" ", "").upper()
            if not any(c.isalpha() for c in text):
                messagebox.showerror("Error", "Text must contain at least one alphabetic character.")
                return
            if not keyword.isalpha() or keyword == "":
                messagebox.showerror("Error", "Keyword must consist of alphabetic characters only.")
                return
            decrypted = decrypt(text, keyword)
            result_text.config(state=tk.NORMAL)
            result_text.delete("1.0", tk.END)
            result_text.insert(tk.END, decrypted)
            result_text.config(state=tk.DISABLED)
        
        tk.Button(decrypt_win, text="Decrypt", command=do_decrypt, width=20).pack(pady=10)

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()