-- Cria a tabela e colunas
CREATE TABLE tb_Cliente (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR,
    cidadeCliente VARCHAR,
    estadoCliente VARCHAR,
    paisCliente VARCHAR,
    FOREIGN KEY (idCliente) REFERENCES tb_Locacao2(idCliente)
);

-- Insere na tabela criada sem valores duplicados e ordenados pelo id
INSERT INTO tb_Cliente
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao
ORDER BY idCliente;

-- Cria a tabela carro sem o km, pois o mesmo tem valores diferentes para o mesmo id
CREATE TABLE tb_Carro (
    idCarro INT PRIMARY KEY,
    classiCarro VARCHAR,
    marcaCarro VARCHAR,
    modeloCarro VARCHAR,
    anoCarro INT,
    idCombustivel INT,
    tipoCombustivel VARCHAR,
    FOREIGN KEY (idCarro) REFERENCES tb_Locacao2(idCarro)
);

-- Insere na tabela apenas IDs diferentes
INSERT INTO tb_Carro
SELECT idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel, tipoCombustivel
FROM tb_locacao
GROUP BY idCarro
ORDER BY idCarro;

-- Cria a tabela tb_Vendedor
CREATE TABLE tb_Vendedor (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR,
    sexoVendedor SMALLINT,
    estadoVendedor VARCHAR,
    FOREIGN KEY (idVendedor) REFERENCES tb_Locacao2(idVendedor)
);

-- Insere na tabela tb_Vendedor
INSERT INTO tb_Vendedor
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao;

-- Cria a tabela principal tb_Locacao2
CREATE TABLE tb_Locacao2 (
    idLocacao INT PRIMARY KEY,
    idCliente INT,
    idCarro INT,
    kmCarro INT,
    dataLocacao DATETIME,
    horaLocacao TIME,
    qtdDiaria INT,
    vlrDiaria DECIMAL,
    dataEntrega DATE,
    horaEntrega TIME,
    idVendedor INT,
    FOREIGN KEY (idCliente) REFERENCES tb_Cliente(idCliente),
    FOREIGN KEY (idCarro) REFERENCES tb_Carro(idCarro),
    FOREIGN KEY (idVendedor) REFERENCES tb_Vendedor(idVendedor)
);

-- Insere na tabela tb_Locacao2
INSERT INTO tb_Locacao2
SELECT  idLocacao, idCliente, idCarro, kmCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor
FROM tb_locacao;

DROP TABLE tb_locacao 
