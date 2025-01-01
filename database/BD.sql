CREATE DATABASE techgarage;
USE techgarage;

CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    endereco VARCHAR(255),
    telefone VARCHAR(20),
    email VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE veiculos (
    id_veiculo INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    marca VARCHAR(50),
    modelo VARCHAR(50),
    ano YEAR,
    placa VARCHAR(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

CREATE TABLE ordens_servico (
    id_ordem_servico INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_veiculo INT NOT NULL,
    data_abertura TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_fechamento TIMESTAMP NULL,
    status VARCHAR(50),
    descricao_problemas TEXT,
    descricao_servicos TEXT,
    valor_total DECIMAL(10, 2),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_veiculo) REFERENCES veiculos(id_veiculo)
);

CREATE TABLE pecas_servicos (
    id_item INT AUTO_INCREMENT PRIMARY KEY,
    id_ordem_servico INT NOT NULL,
    tipo VARCHAR(50),
    descricao VARCHAR(255),
    quantidade INT,
    valor_unitario DECIMAL(10, 2),
    FOREIGN KEY (id_ordem_servico) REFERENCES ordens_servico(id_ordem_servico)
);

CREATE TABLE nfes (
    id_nfe INT AUTO_INCREMENT PRIMARY KEY,
    id_ordem_servico INT NOT NULL,
    numero_nfe VARCHAR(50),
    xml TEXT,
    status VARCHAR(50),
    data_emissao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_ordem_servico) REFERENCES ordens_servico(id_ordem_servico)
);

CREATE TABLE historico_servicos (
    id_historico INT AUTO_INCREMENT PRIMARY KEY,
    id_ordem_servico INT NOT NULL,
    descricao_servicos TEXT,
    data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_ordem_servico) REFERENCES ordens_servico(id_ordem_servico)
);

CREATE TABLE estoque (
    id_estoque INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(255) NOT NULL,
    quantidade INT NOT NULL,
    valor_unitario DECIMAL(10, 2) NOT NULL,
    data_entrada TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE pecas_estoque (
    id_peca_estoque INT AUTO_INCREMENT PRIMARY KEY,
    id_estoque INT NOT NULL,
    id_ordem_servico INT NOT NULL,
    quantidade_utilizada INT NOT NULL,
    FOREIGN KEY (id_estoque) REFERENCES estoque(id_estoque),
    FOREIGN KEY (id_ordem_servico) REFERENCES ordens_servico(id_ordem_servico)
);-- Script para inicializar o banco de dados 
