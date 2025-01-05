import tkinter as tk
from tkinter import Toplevel, ttk, messagebox
from database.models import consultar_clientes, cadastro_cliente

def abrir_modal_cadastro():
    
    def salvar_cliente():
        nome = nome_entry.get()
        endereco = endereco_entry.get()
        telefone = telefone_entry.get()
        email = email_entry.get()

        if not nome:
            messagebox.showwarning("Atenção", "O nome é obrigatório!")
            return

        cadastro_cliente(nome, endereco, telefone, email)
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        modal.destroy()
        listar_clientes()

    modal = Toplevel()
    modal.title("Cadastrar Cliente")
    modal.geometry("300x300")
    modal.configure(bg="#2c2c2c")  # Altera o fundo da janela modal

    tk.Label(modal, text="Nome:", bg="#2c2c2c", fg="white").grid(row=0, column=0, padx=10, pady=15)
    tk.Label(modal, text="Endereço:", bg="#2c2c2c", fg="white").grid(row=1, column=0, padx=10, pady=15)
    tk.Label(modal, text="Telefone:", bg="#2c2c2c", fg="white").grid(row=2, column=0, padx=10, pady=15)
    tk.Label(modal, text="Email:", bg="#2c2c2c", fg="white").grid(row=3, column=0, padx=10, pady=15)

    nome_entry = tk.Entry(modal)
    endereco_entry = tk.Entry(modal)
    telefone_entry = tk.Entry(modal)
    email_entry = tk.Entry(modal)

    nome_entry.grid(row=0, column=1, padx=20, pady=15)
    endereco_entry.grid(row=1, column=1, padx=20, pady=15)
    telefone_entry.grid(row=2, column=1, padx=20, pady=15)
    email_entry.grid(row=3, column=1, padx=20, pady=15)

    tk.Button(modal, text="Salvar", command=salvar_cliente).grid(row=4, column=0, columnspan=2, pady=20)

def listar_clientes(filtro_nome=""):
    clientes = consultar_clientes(filtro_nome)
    for row in treeview.get_children():
        treeview.delete(row)
    for cliente in clientes:
        treeview.insert("", "end", values=cliente)

def buscar_clientes(filtro_nome_entry):
    filtro = filtro_nome_entry.get()
    listar_clientes(filtro)

def abrir_interface_cliente():
    global treeview

    root = tk.Tk()
    root.title("Clientes")
    root.geometry("1000x300")
    root.configure(bg="#2c2c2c")  # Altera o fundo da janela principal

    frame_filtros = tk.Frame(root, bg="#2c2c2c")
    frame_filtros.pack(pady=10, fill=tk.X)

    filtro_nome_label = tk.Label(frame_filtros, text="Filtrar por nome:", bg="#2c2c2c", fg="white")
    filtro_nome_label.pack(side=tk.LEFT, padx=10)

    filtro_nome_entry = tk.Entry(frame_filtros)
    filtro_nome_entry.pack(side=tk.LEFT, padx=20)

    buscar_button = tk.Button(frame_filtros, text="Buscar", command=lambda: buscar_clientes(filtro_nome_entry))
    buscar_button.pack(side=tk.LEFT, padx=10)

    adicionar_button = tk.Button(frame_filtros, text="Adicionar Cliente", command=abrir_modal_cadastro)
    adicionar_button.pack(side=tk.LEFT, padx=10)

    treeview = ttk.Treeview(root, columns=("ID", "Nome", "Endereço", "Telefone", "Email"), show="headings")
    treeview.heading("ID", text="ID")
    treeview.heading("Nome", text="Nome")
    treeview.heading("Endereço", text="Endereço")
    treeview.heading("Telefone", text="Telefone")
    treeview.heading("Email", text="Email")

    treeview.column("ID", width=50, anchor="center")
    treeview.column("Nome", width=200, anchor="w")
    treeview.column("Endereço", width=300, anchor="w")
    treeview.column("Telefone", width=150, anchor="center")
    treeview.column("Email", width=200, anchor="w")

    treeview.pack(pady=10)

    listar_clientes()

    root.mainloop()
