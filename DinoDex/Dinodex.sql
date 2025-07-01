CREATE DATABASE dinodex;

CREATE TABLE familias(
	id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT
);

CREATE TABLE dinossauros(
	id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    periodo VARCHAR(50),
    dieta VARCHAR(50),
    tamanho_metros NUMERIC(5,2),
    familia_id INTEGER REFERENCES familias(id) ON DELETE CASCADE,
    imagem_url TEXT
);

INSERT INTO familias(nome, descricao) VALUES
('Tyrannosauridae', 'Família de grandes dinossauros carnívoros, como o Tyrannosaurus.'),
('Hadrosauridae', 'Dinossauros herbívoros conhecidos como “dinossauros de bico de pato”.'),
('Dromaeosauridae', 'Família dos raptors, pequenos carnívoros rápidos e inteligentes.');

INSERT INTO dinossauros (nome, periodo, dieta, tamanho_metros, familia_id, imagem_url) VALUES
('Tyrannosaurus Rex', 'Cretáceo', 'Carnívoro', 12.3, 1, 'https://s2-umsoplaneta.glbimg.com/RSoqStVcUOA8aPwb7PmALyPS6aI=/0x0:2190x1369/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_7d5b9b5029304d27b7ef8a7f28b4d70f/internal_photos/bs/2022/h/7/YlKvgERrGcE47KUHP5MQ/gettyimages-99311107.jpg'),
('Edmontosaurus', 'Cretáceo', 'Herbívoro', 10.0, 2, 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlbYPAv5yT6hcxvKBngjX60x4o6SWfrQW8qUrPZ2FPCRaaGxzG6BRO6VKJdFmGI9p0nou9O7yTDeKehoDX3soRgxffnqGelJm_kGHv5zoXOOYsqxgwJ8UhaqFSVNgQIKnb-WYJeH8t5XQ6/s1600/Edmontosaurus+-+Michael+W.+Skrepnick.jpg'),
('Velociraptor', 'Cretáceo', 'Carnívoro', 2.0, 3, 'https://play-lh.googleusercontent.com/n1Bxkn-afxfStE90s5iukBja6HRzqU8PEP70pATjL7DLd28ddHETSgnDbaDXT-Q8q1M');

SELECT 
