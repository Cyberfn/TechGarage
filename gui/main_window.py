import tkinter as tk
from tkinter import messagebox
from gui.cliente_view import abrir_interface_cliente

def abrir_cliente_view():
    abrir_interface_cliente()

def abrir_orcamento_view():
    messagebox.showinfo("Orçamento", "Abrir tela de orçamentos de clientes.")

def abrir_nfe_view():
    messagebox.showinfo("NFe", "Abrir tela de NFe.")

def abrir_veiculo_view():
    messagebox.showinfo("Veículos", "Abrir tela de cadastro de veículos.")

def abrir_servico_view():
    messagebox.showinfo("Serviços", "Abrir tela de cadastro de serviços.")

def abrir_ordem_servico_view():
    messagebox.showinfo("Ordens de Serviço", "Abrir tela de ordens de serviço.")

def criar_botao_arredondado(canvas, x, y, width, height, text, command, bg="#4c4c4c", fg="white"):
    radius = 20
    x1, y1 = x, y
    x2, y2 = x + width, y + height

    canvas.create_oval(x1, y1, x1 + 2 * radius, y1 + 2 * radius, fill=bg, outline=bg)
    canvas.create_oval(x2 - 2 * radius, y1, x2, y1 + 2 * radius, fill=bg, outline=bg)
    canvas.create_oval(x1, y2 - 2 * radius, x1 + 2 * radius, y2, fill=bg, outline=bg)
    canvas.create_oval(x2 - 2 * radius, y2 - 2 * radius, x2, y2, fill=bg, outline=bg)
    canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, fill=bg, outline=bg)
    canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, fill=bg, outline=bg)

    btn_text = canvas.create_text(
        (x1 + x2) // 2, (y1 + y2) // 2,
        text=text,
        font=("Helvetica", 14),
        fill=fg
    )

    def on_click(event):
        command()

    canvas.tag_bind(btn_text, "<Button-1>", on_click)

def main_window():
    """Inicializa a janela principal do sistema."""
    root = tk.Tk()
    root.title("Sistema de Oficina")
    root.geometry("1833x975")
    root.resizable(False, False)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 1833
    window_height = 900
    position_top = (screen_height - window_height) // 2
    position_left = (screen_width - window_width) // 2
    root.geometry(f'{window_width}x{window_height}+{position_left}+{position_top}')

    root.configure(bg="#2c2c2c")

    titulo = tk.Label(root, text="Bem-vindo ao Sistema de Oficina!", font=("Helvetica", 18), bg="#2c2c2c", fg="white")
    titulo.pack(pady=20)

    canvas = tk.Canvas(root, width=1600, height=850, bg="#2c2c2c", highlightthickness=0)
    canvas.pack(pady=50)

    botoes = [
        ("Clientes", abrir_cliente_view),
        ("Orçamento", abrir_orcamento_view),
        ("Veículos", abrir_veiculo_view),
        ("Serviço", abrir_servico_view),
        ("NFe", abrir_nfe_view),
        ("Estoque", abrir_ordem_servico_view),
    ]

    button_width = 200
    button_height = 60
    padding = 20
    total_width = len(botoes) * (button_width + padding) - padding
    start_x = (1600 - total_width) // 2

    for i, (texto, comando) in enumerate(botoes):
        x = start_x + i * (button_width + padding)
        y = 50
        criar_botao_arredondado(canvas, x, y, button_width, button_height, texto, comando)

    root.mainloop()

if __name__ == "__main__":
    main_window()
