import tkinter as tk
from tkinter import messagebox
from calculadora_imc import calcular_imc, classificar_imc  # Certifique-se de que este módulo está correto

# Função para calcular e mostrar o resultado
def mostrar_resultado():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        messagebox.showinfo("Resultado", f"Seu IMC é {imc:.2f}. Classificação: {classificacao}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora de IMC")

# Labels e campos de entrada
tk.Label(root, text="Peso (kg):").grid(row=0, column=0, padx=10, pady=5)
entry_peso = tk.Entry(root)
entry_peso.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Altura (m):").grid(row=1, column=0, padx=10, pady=5)
entry_altura = tk.Entry(root)
entry_altura.grid(row=1, column=1, padx=10, pady=5)

# Botão para calcular IMC
btn_calcular = tk.Button(root, text="Calcular IMC", command=mostrar_resultado)
btn_calcular.grid(row=2, column=0, columnspan=2, pady=10)

# Executando a interface
root.mainloop()
