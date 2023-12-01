import sqlite3

conn =  sqlite3.connect('registro.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pessoas(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        nome_completo TEXT UNIQUE NOT NULL,
        idade NUMERIC NOT NULL,
        genero TEXT NOT NULL,
        nacionalidade TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        estado_civil TEXT NOT NULL,
        nome_do_pai TEXT NOT NULL,
        nome_da_mae TEXT NOT NULL
    )
''')

cursor.execute('''
    INSERT INTO pessoas (nome_completo, idade, genero, nacionalidade, email, estado_civil, nome_do_pai, nome_da_mae) VALUES
    ('francisco pereira souza','55','M','mexicano','mechico@hotmail.com','casado','jose pereira', 'maria souza'),
    ('cintia soares alves','52','F','grega','cicialves@gmail.com','casada','clotilde soares','izaias fonseca'),
    ('victor hugo','30','M','brasileiro','victin2009@google.com.br','solteiro','francisco santos','cintia soares')
''')

#RETIRE AS HASHTAGS E RODE PARA REALIZAR AS ALTERAÇOES DESEJADAS!

# cursor.execute('''
#     UPDATE pessoas
#     SET idade = '60', genero = 'F', email = 'novo_email@gmail.com'
#     WHERE id = 1
# ''')
# cursor.execute('''
#     DELETE FROM pessoas
#     WHERE id = 3
# ''')
# cursor.execute('''UPDATE pessoas
#     SET nome_completo = 'Clayton Afonso',
#         idade = '39',
#         genero = 'M',
#         nacionalidade = 'Brasileiro',
#         email = 'cleitin@example.com',
#         estado_civil = 'Solteiro',
#         nome_do_pai = 'Josefino Afonso',
#         nome_da_mae = 'Geralda Claudia'
#     WHERE id = 2
# ''')
conn.commit()
conn.close()