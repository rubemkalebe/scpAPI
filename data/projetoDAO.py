import data.data_helper

from model.projeto import Projeto

class ProjetoDAO(object):

    def insert(self, p):
        # connect to the database
        connection = data.data_helper.create_connection()

        try:
            with connection.cursor() as cursor:
                # create a new record
                sql = '''
                    INSERT INTO Projeto (nome, descricao, idPatrocinador, idGerente, equipe)
                    VALUES (%s, %s, %s, %s, %s)
                '''
                cursor.execute(sql, (
                    p.nome,
                    p.descricao,
                    p.patrocinador.pessoa_id,
                    p.gerente.pessoa_id,
                    p.equipe
                ))

            # commit changes
            connection.commit()
        finally:
            connection.close()


    def fetchall(self):
        # connect to the database
        connection = data.data_helper.create_connection()

        try:
            with connection.cursor() as cursor:
                sql = '''
                    SELECT *
                    FROM Projeto
                '''
                cursor.execute(sql)
                result = cursor.fetchall()

                projetos = []
                for r in result:
                    p = Projeto(r[0], r[1], r[2], r[3], r[4], r[5], None, None)
                    projetos.append(p.__dict__)

                return projetos
        finally:
            connection.close()

    def retrieve_by_gerente(self, gerente_id):
        #connect to the database
        connection = data.data_helper.create_connection()

        try:
            with connection.cursor() as cursor:
                sql = '''
                    SELECT nome
                    FROM Projeto
                    WHERE idGerente=%s
                '''
                cursor.execute(sql, (gerente_id,))
                result = cursor.fetchall()

                projetos = []
                for r in result:
                    p = Projeto(r[0], r[1], r[2], r[3], r[4], r[5], None, None)
                    projetos.append(p.__dict__)

                return projetos
        finally:
            connection.close()

    def retrieve_by_patrocinador(self, patrocinador_id):
        #connect to the database
        connection = data.data_helper.create_connection()

        try:
            with connection.cursor() as cursor:
                sql = '''
                    SELECT nome
                    FROM Projeto
                    WHERE idPatrocinador=%s
                '''
                cursor.execute(sql, (patrocinador_id,))
                result = cursor.fetchall()

                projetos = []
                for r in result:
                    p = Projeto(r[0], r[1], r[2], r[3], r[4], r[5], None, None)
                    projetos.append(p.__dict__)

                return projetos
        finally:
            connection.close()


'''
SELECT *
FROM Projeto JOIN Pessoa
ON Projeto.idPatrocinador=Pessoa.idPessoa
WHERE Pessoa.email='rubem@email.com'
UNION
SELECT *
FROM Projeto JOIN Pessoa
ON Projeto.idGerente=Pessoa.idPessoa
WHERE Pessoa.email='rubem@email.com';
'''