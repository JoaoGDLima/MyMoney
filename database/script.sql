CREATE TABLE IF NOT EXISTS usuario(
 id INT NOT NULL, 
 usuario VARCHAR(100) NOT NULL,
 senha VARCHAR(100) NOT NULL,
 PRIMARY KEY(id),
 CONSTRAINT uk_email UNIQUE(usuario)
);

CREATE TABLE IF NOT EXISTS categoria(
 id INT NOT NULL, 
 usuario_id INT NOT NULL, 
 nome VARCHAR(100) NOT NULL,
 tipo CHAR(1) NOT NULL,
 created_at DATETIME NOT NULL,
 updated_at DATETIME NOT NULL,
 PRIMARY KEY (id),
 CONSTRAINT fk_categoria_usuario FOREIGN KEY (usuario_id) REFERENCES usuario(id)
);


CREATE TABLE IF NOT EXISTS lancamento(
 id INT NOT NULL, 
 usuario_id INT NOT NULL, 
 categoria_id INT NOT NULL,
 datahora DATETIME NOT NULL, 
 valor DECIMAL(10,2) NOT NULL,
 tipo CHAR(1) NOT NULL,
 observacao VARCHAR(100) NOT NULL, 
 created_at DATETIME NOT NULL,
 updated_at DATETIME NOT NULL,
 PRIMARY KEY (id),
 CONSTRAINT fk_lancamento_usuario FOREIGN KEY (usuario_id) REFERENCES usuario(id),
 CONSTRAINT fk_lancamento_categoria FOREIGN KEY (categoria_id) REFERENCES categoria(id)
);
