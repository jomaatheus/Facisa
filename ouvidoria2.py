import tkinter as tk
from tkinter import ttk

def cadastrar_ocorrencia():
    ocorrencia = ocorrencia_entry.get()
    menu.append(ocorrencia)
    ocorrencia_entry.delete(0, tk.END)
    output_text.insert(tk.END, 'Ocorrencia cadastrada com sucesso!\n\n')

def listar_ocorrencias():
    output_text.delete("1.0", tk.END)
    if menu:
        for i, ocorrencia in enumerate(menu, start=1):
            output_text.insert(tk.END, f'Ocorrencia Numero {i}: {ocorrencia}\n')
    else:
        output_text.insert(tk.END, 'Não há ocorrências.\n\n')

def apagar_ocorrencia():
    output_text.delete("1.0", tk.END)
    if menu:
        for i, ocorrencia in enumerate(menu, start=1):
            output_text.insert(tk.END, f'Ocorrencia Numero {i}: {ocorrencia}\n')
        try:
            apagarOcorrencia = int(apagar_entry.get())
            if apagarOcorrencia > 0 and apagarOcorrencia <= len(menu):
                ocorrencia_apagada = menu.pop(apagarOcorrencia-1)
                output_text.insert(tk.END, 'Ocorrencia apagada com sucesso!\n\n')
            else:
                output_text.insert(tk.END, 'Código inválido.\n\n')
        except ValueError:
            output_text.insert(tk.END, 'Digite um número válido para apagar.\n\n')
    else:
        output_text.insert(tk.END, 'Não há ocorrências.\n\n')

def consultar_ocorrencia():
    output_text.delete("1.0", tk.END)
    if menu:
        try:
            codigo = int(consulta_entry.get())
            if codigo > 0 and codigo <= len(menu):
                ocorrencia = menu[codigo-1]
                output_text.insert(tk.END, f'Ocorrência encontrada:\nCódigo: {codigo}\nOcorrência: {ocorrencia}\n\n')
            else:
                output_text.insert(tk.END, 'Código inválido.\n\n')
        except ValueError:
            output_text.insert(tk.END, 'Digite um número válido para consultar.\n\n')
    else:
        output_text.insert(tk.END, 'Não há ocorrências.\n\n')

root = tk.Tk()
root.title("Menu de Ocorrências")

# Criar os widgets da interface
ocorrencia_label = ttk.Label(root, text="Digite a ocorrência:")
ocorrencia_entry = ttk.Entry(root)
cadastrar_button = ttk.Button(root, text="Cadastrar", command=cadastrar_ocorrencia)

listar_button = ttk.Button(root, text="Listar Ocorrências", command=listar_ocorrencias)

apagar_label = ttk.Label(root, text="Digite o número da ocorrência a apagar:")
apagar_entry = ttk.Entry(root)
apagar_button = ttk.Button(root, text="Apagar", command=apagar_ocorrencia)

consulta_label = ttk.Label(root, text="Digite o código da ocorrência:")
consulta_entry = ttk.Entry(root)
consultar_button = ttk.Button(root, text="Consultar", command=consultar_ocorrencia)

output_text = tk.Text(root, height=10, width=50)

# Posicionar os widgets na interface
ocorrencia_label.pack()
ocorrencia_entry.pack()
cadastrar_button.pack()

listar_button.pack()

apagar_label.pack()
apagar_entry.pack()
apagar_button.pack()

consulta_label.pack()
consulta_entry.pack()
consultar_button.pack()

output_text.pack()

menu = []

root.mainloop()
