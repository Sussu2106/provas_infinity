CREATE DATABASE Infinity_School;

USE Infinity_School;

CREATE TABLE Estudantes (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(255),
    Idade INT,
    Curso VARCHAR(50)
);

INSERT INTO Estudantes (Nome, Idade, Curso) VALUES
('João', 28, 'Engenharia'),
('Maria', 33, 'Ciência da Computação'),
('Pedro', 19, 'ADS');
