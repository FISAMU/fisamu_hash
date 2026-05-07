import tkinter as tk
from tkinter import messagebox

PLACEHOLDER_TEXT = "Entrez votre message ici..."

def custom_hash_64(message):
    # Algorithme FNV-1a (64 bits)
    FNV_OFFSET_BASIS = 0xcbf29ce484222325
    FNV_PRIME = 0x100000001b3
    MASK_64 = 0xffffffffffffffff

    hash_value = FNV_OFFSET_BASIS
    data = message.encode('utf-8')

    for byte in data:
        hash_value ^= byte
        hash_value = (hash_value * FNV_PRIME) & MASK_64

    return f"{hash_value:016x}"


def generate_hash():
    user_input = entry_message.get().strip()
    if not user_input or user_input == PLACEHOLDER_TEXT:
        messagebox.showwarning("Erreur", "Veuillez entrer un message valide.")
        return

    result = custom_hash_64(user_input)
    label_result.config(text=result, fg="#ecf0f1")
    copy_button.config(state=tk.NORMAL)


def copy_to_clipboard():
    if label_result['text'] and label_result['text'] != "Le résultat s'affichera ici":
        root.clipboard_clear()
        root.clipboard_append(label_result['text'])
        messagebox.showinfo("Copié", "Le hash a été copié dans le presse-papier.")


def clear_placeholder(event):
    if entry_message.get() == PLACEHOLDER_TEXT:
        entry_message.delete(0, tk.END)
        entry_message.config(fg="#2c3e50")


def add_placeholder(event):
    if not entry_message.get().strip():
        entry_message.insert(0, PLACEHOLDER_TEXT)
        entry_message.config(fg="#7f8c8d")


def on_enter_button(event):
    btn_hash.config(bg="#2980b9")


def on_leave_button(event):
    btn_hash.config(bg="#3498db")


def on_enter_copy(event):
    copy_button.config(bg="#2ecc71")


def on_leave_copy(event):
    copy_button.config(bg="#27ae60")

# --- Configuration de la fenêtre principale ---
root = tk.Tk()
root.title("Générateur de Hash 64-bit")
root.geometry("520x340")
root.configure(bg="#1f2833")
root.resizable(False, False)

container = tk.Frame(root, bg="#1f2833")
container.pack(fill="both", expand=True, padx=20, pady=20)

card = tk.Frame(container, bg="#2c3e50", bd=0, relief="flat")
card.pack(fill="both", expand=True, padx=10, pady=10)

label_title = tk.Label(card, text="Générateur de hash 64-bit", font=("Segoe UI", 16, "bold"), bg="#2c3e50", fg="#ecf0f1")
label_title.pack(pady=(18, 12))

entry_message = tk.Entry(card, width=42, font=("Segoe UI", 11), bd=0, relief="flat", fg="#7f8c8d")
entry_message.pack(pady=(0, 10), padx=18, ipady=8)
entry_message.insert(0, PLACEHOLDER_TEXT)
entry_message.bind("<FocusIn>", clear_placeholder)
entry_message.bind("<FocusOut>", add_placeholder)

btn_hash = tk.Button(card, text="Hacher le message", command=generate_hash, bg="#3498db", fg="white", font=("Segoe UI", 10, "bold"), bd=0, activebackground="#2980b9", activeforeground="white")
btn_hash.pack(pady=(0, 8), ipadx=8, ipady=8)
btn_hash.bind("<Enter>", on_enter_button)
btn_hash.bind("<Leave>", on_leave_button)

result_frame = tk.Frame(card, bg="#17202a", bd=0, relief="flat")
result_frame.pack(fill="x", padx=18, pady=(8, 10))

label_result = tk.Label(result_frame, text="Le résultat s'affichera ici", bg="#17202a", fg="#7f8c8d", font=("Courier New", 11), wraplength=460, justify="center", padx=12, pady=12)
label_result.pack(fill="x")

copy_button = tk.Button(card, text="Copier le hash", command=copy_to_clipboard, bg="#27ae60", fg="white", font=("Segoe UI", 10, "bold"), bd=0, state=tk.DISABLED, activebackground="#2ecc71", activeforeground="white")
copy_button.pack(pady=(0, 16), ipadx=8, ipady=8)
copy_button.bind("<Enter>", on_enter_copy)
copy_button.bind("<Leave>", on_leave_copy)

label_footer = tk.Label(card, text="FNV-1a 64 bits | Entrez un texte puis cliquez sur Hacher", font=("Segoe UI", 8), bg="#2c3e50", fg="#95a5a6")
label_footer.pack(pady=(0, 16))

root.mainloop()