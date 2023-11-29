--Script feito para criar todas as tabelas da tabela de origem (tb_locacao)
--depois excluir a tabela de origem para deixar apenas as novas tabelas

-- Cria a tabela e colunas
CREATE TABLE tb_Cliente (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR,
    cidadeCliente VARCHAR,
    estadoCliente VARCHAR,
    paisCliente VARCHAR
);
-- Insere na tabela criada sem valores duplicados e ordenados pelo id
INSERT INTO tb_Cliente
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao
ORDER BY idCliente;

--cria a tabela carro sem o km, pois o mesmo tem valores diferentes para o mesmo id
CREATE TABLE tb_Carro (
	idCarro INT PRIMARY KEY,
	classiCarro VARCHAR,
	marcaCarro VARCHAR,
	modeloCarro VARCHAR,
	anoCarro INT,
	idCombustivel INT,
	tipoCombustivel VARCHAR
);

--insere na tabela apenas IDs diferentes
INSERT INTO tb_Carro
SELECT idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel, tipoCombustivel
FROM tb_locacao
GROUP BY idCarro
ORDER BY idCarro;

CREATE TABLE tb_Vendedor (
	idVendedor INT PRIMARY KEY,
	nomeVendedor VARCHAR,
	sexoVendedor SMALLINT,
	estadoVendedor VARCHAR
);
-- mesma coisa dos anteriores
INSERT INTO tb_Vendedor
SELECT  DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao;

--tabela principal que permite a conexão com todas as outras tabelas
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
	idVendedor INT
);

INSERT INTO tb_Locacao2
SELECT  idLocacao, idCliente, idCarro, kmCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor
FROM tb_locacao;