import data.data_helper

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
                return result
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
                return result
        finally:
            connection.close()