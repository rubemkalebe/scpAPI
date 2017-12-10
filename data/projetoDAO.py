import data.data_helper

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
                return result
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
                return result
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
                return result
        finally:
            connection.close()