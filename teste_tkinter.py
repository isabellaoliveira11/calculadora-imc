import tkinter as tk

# Cria uma janela
root = tk.Tk()
root.title("Teste do Tkinter")
root.geometry("300x200")

# Adiciona um rótulo à janela
label = tk.Label(root, text="Tkinter está funcionando!", font=("Arial", 16))
label.pack(pady=20)

# Executa a interface gráfica
root.mainloop()
