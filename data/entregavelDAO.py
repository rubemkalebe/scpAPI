import data.data_helper

from model.entregavel import Entregavel

class EntregavelDAO(object):

    def insert(self, projeto_id, e):
        # connect to the database
        connection = data.data_helper.create_connection()

        try:
            with connection.cursor() as cursor:
                # create a new record
                sql = '''
                    INSERT INTO Entregavel (nome, Projeto_idProjeto, descricao, data_inicio, data_fim_prev, data_fim)
                    VALUES (%s, %s, %s, %s, %s, %s)
                '''
                cursor.execute(sql, (
                    e.nome,
                    projeto_id,
                    e.descricao,
                    e.data_inicio,
                    e.data_fim_prev,
                    e.data_fim
                ))

            # commit changes
            connection.commit()
        finally:
            connection.close()

    def retrieve_by_projeto(self, projeto_id):
        # connect to the database
        connection = data.data_helper.create_connection()

        try:
            with connection.cursor() as cursor:
                sql = '''
                            SELECT *
                            FROM Entregavel
                            WHERE Projeto_idProjeto=%s
                        '''
                cursor.execute(sql, (projeto_id,))
                result = cursor.fetchall()

                entregaveis = []
                for r in result:
                    e = Entregavel(r[2], r[0], r[1], r[3], r[4], r[5], r[6])
                    entregaveis.append(e.__dict__)

                return entregaveis
        finally:
            connection.close()
