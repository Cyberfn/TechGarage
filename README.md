# **TechGarage**

TechGarage é um sistema desktop desenvolvido para oficinas automotivas, com foco na gestão de clientes, serviços realizados e emissão de Notas Fiscais Eletrônicas (NFe). O sistema utiliza Python, MariaDB e integra a tecnologia com a mecânica para oferecer uma solução robusta e eficiente para o gerenciamento do dia a dia das oficinas.

## **Funcionalidades**

- **Cadastro de Clientes**: Armazene informações essenciais sobre seus clientes, como nome, telefone e endereço.
- **Cadastro de Serviços**: Registre os serviços realizados, como trocas de óleo, reparos, etc.
- **Emissão de NFe**: Geração e envio de Notas Fiscais Eletrônicas diretamente pela SEFAZ.
- **Gestão de Estoque**: Controle o estoque de peças e materiais utilizados.
- **Relatórios**: Geração de relatórios sobre serviços realizados, faturamento e estoque.

---

## **Tecnologias Utilizadas**

- **Python**: Linguagem de programação principal para o desenvolvimento do sistema.
- **Tkinter**: Biblioteca para criação de interfaces gráficas (GUIs).
- **MariaDB**: Banco de dados utilizado para armazenamento de informações.
- **PyNFe**: Biblioteca para emissão de Notas Fiscais Eletrônicas (NFe).
- **requests/zeep**: Bibliotecas para comunicação com os webservices da SEFAZ.

---

## **Estrutura do Projeto**

A organização do projeto segue a seguinte estrutura de diretórios:

```
sistema_oficina/
├── assets/                 # Arquivos de mídia (ícones, imagens, etc.)
│   ├── icons/
│   └── images/
├── database/               # Scripts e lógica relacionados ao banco de dados
│   ├── init_db.sql         # Script para inicializar o banco de dados
│   ├── connection.py       # Arquivo para gerenciar a conexão com o banco
│   └── models.py           # Classes ou funções para interagir com as tabelas
├── gui/                    # Arquivos da interface gráfica
│   ├── main_window.py      # Janela principal
│   ├── cliente_view.py     # Interface para cadastro de clientes
│   ├── veiculo_view.py     # Interface para cadastro de veículos
│   ├── servico_view.py     # Interface para cadastro de serviços
│   └── ordem_servico_view.py  # Interface para ordens de serviço
├── reports/                # Geração de relatórios
│   └── report_generator.py # Lógica para criar relatórios (PDF, Excel, etc.)
├── tests/                  # Scripts de teste para o sistema
│   └── test_database.py    # Testes para as funções do banco de dados
├── utils/                  # Funções e helpers reutilizáveis
│   ├── validators.py       # Validações gerais (e.g., CPF, placa de veículo)
│   └── helpers.py          # Funções auxiliares
├── requirements.txt        # Dependências do projeto
├── README.md               # Documentação básica do projeto
└── main.py                 # Arquivo principal para executar o sistema
```

---

## **Instalação**

### **1. Clonar o repositório**

```bash
git clone https://github.com/seu_usuario/TechGarage.git
cd TechGarage
```

### **2. Instalar dependências**

Antes de executar o projeto, instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

### **3. Configuração do Certificado Digital (para emissão de NFe)**

Para emissão de NFe, será necessário um certificado digital (A1 ou A3) configurado corretamente. Coloque o arquivo do certificado na pasta `assets/certificados/` e ajuste o código para apontar para ele.

---

## **Execução**

Após a instalação das dependências e configuração do banco de dados, execute o sistema com:

```bash
python main.py
```

A interface gráfica será iniciada, permitindo o uso do sistema para cadastro de clientes, serviços e emissão de NFe.

---

## **Contribuição**

Contribuições são bem-vindas! Para contribuir com o projeto:

1. Fork o repositório.
2. Crie uma branch para a sua modificação (`git checkout -b minha-modificacao`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`).
4. Push para a branch (`git push origin minha-modificacao`).
5. Abra um Pull Request.

---

## **Licença**

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## **Agradecimentos**

- **PyNFe**: Para a integração com a SEFAZ e emissão de NFe.
- **MariaDB**: Banco de dados de alto desempenho.
- **Tkinter**: Para a criação da interface gráfica simples e eficaz.