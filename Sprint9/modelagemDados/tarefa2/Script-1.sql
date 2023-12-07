--dimensão Vendedor
CREATE VIEW dim_Vendedor AS
SELECT idVendedor,
	nomeVendedor AS nome,
	sexoVendedor AS sexo,
	estadoVendedor AS estado
FROM tb_Vendedor tv;

--fato Locacao
CREATE VIEW fato_Locacao AS
SELECT qtdDiaria AS quantDiaria,
	vlrDiaria,
	idVendedor
FROM tb_Locacao2 tl;

--Saber qual vendedor mais faturou com as locações
SELECT 	fl.idVendedor, dv.nome, dv.sexo, dv.estado, 
		SUM(fl.quantDiaria  * fl.vlrDiaria) AS "totalLocacao R$", 
		SUM(fl.quantDiaria) AS quantDiarias
FROM fato_Locacao fl
LEFT JOIN dim_Vendedor dv on fl.idVendedor = dv.idVendedor
GROUP BY fl.idVendedor 
ORDER BY "totalLocacao R$" DESC