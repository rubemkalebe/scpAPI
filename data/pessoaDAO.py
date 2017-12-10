import data.data_helper

from model.pessoa import Pessoa

class PessoaDAO(object):

    def insert(self, p):
        # connect to the database
        connection = data.data_helper.create_connection()

        try:
            with connection.cursor() as cursor:
                # create a new record
                sql = '''
                    INSERT INTO Pessoa (nome, departamento, email)
                    VALUES (%s, %s, %s)
                '''
                cursor.execute(sql, (
                    p.nome,
                    p.departamento,
                    p.email
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
                    FROM Pessoa
                '''
                cursor.execute(sql)
                result = cursor.fetchall()

                pessoas = []
                for r in result:
                    p = Pessoa(r[0], r[1], r[2], r[3], None)
                    pessoas.append(p.__dict__)

                return pessoas
        finally:
            connection.close()

    def retrieve_by_email(self, email):
        #connect to the database
        connection = data.data_helper.create_connection()

        try:
            with connection.cursor() as cursor:
                sql = '''
                    SELECT idPessoa, nome, departamento, email
                    FROM Pessoa
                    WHERE email=%s
                '''
                cursor.execute(sql, (email,))
                result = cursor.fetchone()

                p = Pessoa(result[0], result[1], result[2], result[3], None)
                return p.__dict__
        finally:
            connection.close()