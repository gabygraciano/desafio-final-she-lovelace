import csv
from datetime import datetime
from collections import Counter
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox

# Paleta de cores
cor_fundo = "#ffb6c1"  
cor_botao = "#dda0dd"  
cor_texto = "#ffffff"  

# Como registrar uma venda
def registrar_venda(produto, quantidade, valor_total):
    data_venda = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Captura a data e hora da venda
    with open('registro_vendas.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([data_venda, produto, quantidade, valor_total])  # Salva no CSV
    messagebox.showinfo("Sucesso", "Venda registrada com sucesso!")

# Carregar as vendas do arquivo CSV
def carregar_vendas():
    vendas = []
    try:
        with open('registro_vendas.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                vendas.append(row)
    except FileNotFoundError:
        messagebox.showinfo("Erro", "Nenhuma venda registrada ainda.")
    return vendas

# Exibir gráficos (produto)
def grafico_vendas_por_produto():
    vendas = carregar_vendas()
    if not vendas:
        return
    
    produtos = [venda[1] for venda in vendas]  # nome dos produtos vendidos
    contagem_produtos = Counter(produtos)  # quantidade de vendas por produto
    
    produtos = list(contagem_produtos.keys())
    quantidades = list(contagem_produtos.values())

    plt.pie(quantidades, labels=produtos, autopct='%1.1f%%', startangle=90, colors=["#ffb6c1", "#dda0dd", "#ffffff", "#ff69b4", "#db7093"])
    plt.title('Vendas por Produto', color="#ffb6c1")
    plt.gcf().set_facecolor("#ffffff")  
    plt.axis('equal') 
    plt.show()

# exibir gráfico (data)
def grafico_vendas_por_data():
    vendas = carregar_vendas()
    if not vendas:
        return
    
    datas = [venda[0].split(' ')[0] for venda in vendas]  # pega apenas a data
    contagem_datas = Counter(datas)  # quantas vendas ocorreram por data
    
    datas = list(contagem_datas.keys())
    quantidades = list(contagem_datas.values())

    plt.pie(quantidades, labels=datas, autopct='%1.1f%%', startangle=90, colors=["#ffb6c1", "#dda0dd", "#ffffff", "#ff69b4", "#db7093"])
    plt.title('Vendas por Data', color="#ffb6c1")
    plt.gcf().set_facecolor("#ffffff")  
    plt.axis('equal')  
    plt.show()

# exibir o gráfico  (produto mais vendido)
def produto_mais_vendido():
    vendas = carregar_vendas()
    if not vendas:
        return
    
    produtos = [venda[1] for venda in vendas]
    contagem_produtos = Counter(produtos)
    produto_mais_vendido = contagem_produtos.most_common(1)[0]

    plt.pie([produto_mais_vendido[1]], labels=[produto_mais_vendido[0]], autopct='%1.1f%%', startangle=90, colors=["#ffb6c1"])
    plt.title(f'Produto Mais Vendido: {produto_mais_vendido[0]}', color="#dda0dd")
    plt.gcf().set_facecolor("#ffffff")  
    plt.axis('equal')  
    plt.show()

# Interface visual
def abrir_janela_principal():
    root = Tk()
    root.title("Sistema de Registro de Vendas")
    root.geometry("600x400")
    root.configure(bg=cor_fundo)

    
    frame_esquerda = Frame(root, bg=cor_fundo)
    frame_esquerda.grid(row=0, column=0, padx=10, pady=10, sticky="n")

    
    Label(frame_esquerda, text="Registre seu produto", font=("Helvetica", 16, "bold"), bg=cor_fundo, fg=cor_texto).grid(row=0, column=0, padx=10, pady=10)

    
    Label(frame_esquerda, text="Produto:", bg=cor_fundo, fg=cor_texto).grid(row=1, column=0, padx=10, pady=10, sticky="w")
    produto_entry = Entry(frame_esquerda)
    produto_entry.grid(row=1, column=1, padx=10, pady=10)

    Label(frame_esquerda, text="Quantidade:", bg=cor_fundo, fg=cor_texto).grid(row=2, column=0, padx=10, pady=10, sticky="w")
    quantidade_entry = Entry(frame_esquerda)
    quantidade_entry.grid(row=2, column=1, padx=10, pady=10)

    Label(frame_esquerda, text="Valor Total:", bg=cor_fundo, fg=cor_texto).grid(row=3, column=0, padx=10, pady=10, sticky="w")
    valor_total_entry = Entry(frame_esquerda)
    valor_total_entry.grid(row=3, column=1, padx=10, pady=10)

    Button(frame_esquerda, text="Registrar Venda", command=lambda: registrar_venda(
        produto_entry.get(), quantidade_entry.get(), valor_total_entry.get()), bg=cor_botao, fg=cor_texto).grid(row=4, column=1, pady=10)

    
    frame_direita = Frame(root, bg=cor_fundo)
    frame_direita.grid(row=0, column=1, padx=10, pady=10, sticky="n")

   
    Button(frame_direita, text="Gráfico de Vendas por Produto", command=grafico_vendas_por_produto, bg=cor_botao, fg=cor_texto).grid(row=0, column=0, pady=10)
    Button(frame_direita, text="Gráfico de Vendas por Data", command=grafico_vendas_por_data, bg=cor_botao, fg=cor_texto).grid(row=1, column=0, pady=10)
    Button(frame_direita, text="Produto Mais Vendido", command=produto_mais_vendido, bg=cor_botao, fg=cor_texto).grid(row=2, column=0, pady=10)

    root.mainloop()

# Inicia a interface
if __name__ == "__main__":
    abrir_janela_principal()