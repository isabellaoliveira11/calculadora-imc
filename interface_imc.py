import tkinter as tk
from calculadora_imc import calcular_imc, classificar_imc  # Certifique-se de que o arquivo calculadora_imc.py está na mesma pasta

# Função para capturar os dados da interface e calcular o IMC
def calcular():
    peso = float(entry_peso.get())
    altura = float(entry_altura.get())
    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)
    resultado_label.config(text=f"Seu IMC é {imc:.2f}. Classificação: {classificacao}")

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora de IMC")

# Criando widgets
tk.Label(root, text="Digite o peso (kg):").grid(row=0, column=0)
entry_peso = tk.Entry(root)
entry_peso.grid(row=0, column=1)

tk.Label(root, text="Digite a altura (m):").grid(row=1, column=0)
entry_altura = tk.Entry(root)
entry_altura.grid(row=1, column=1)

tk.Button(root, text="Calcular IMC", command=calcular).grid(row=2, column=0, columnspan=2)

resultado_label = tk.Label(root, text="")
resultado_label.grid(row=3, column=0, columnspan=2)

# Executando a interface
root.mainloop()
