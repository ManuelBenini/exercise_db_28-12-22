from dao.utility.db import MySql
from dto.giocatore import Giocatore

class GiocatoreDao:
    @classmethod
    def getAllPlayers(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM giocatore")
        results = MySql.getResults()
        giocatori = []
        for giocatore in results:
            giocatori.append(Giocatore(id = giocatore[0], nome = giocatore[1]))
        MySql.closeConnection()
        return giocatori
    
    @classmethod
    def getPlayerById(cls, id):
        MySql.openConnection()
        MySql.query(f"SELECT * FROM giocatore WHERE ID = {id}")
        results = MySql.getResults()
        giocatore = Giocatore(id = results[0][0], nome = results[0][1])
        MySql.closeConnection()
        return giocatore
    
    @classmethod
    def getPlayersNameWith3DifferentPartecipationORwithMoreNationality(cls):
        MySql.openConnection()
        MySql.query(f"SELECT pg.Nome \
                    FROM (SELECT p.IDGiocatore, g.Nome, COUNT(*) as Partecipazioni \
                            FROM partecipazione p \
                            INNER JOIN giocatore g ON p.IDGiocatore = g.ID \
	                        GROUP BY p.IDGiocatore, g.Nome) as pg \
                    WHERE pg.Partecipazioni >= 3 OR 1 < (SELECT COUNT(*) as numero_nazioni \
                                                        FROM partecipazione p \
                                                        WHERE p.IDGiocatore = pg.IDGiocatore)")
        results = MySql.getResults()
        giocatori = []
        for giocatore in results:
            giocatori.append(Giocatore(nome = giocatore[0]))
        MySql.closeConnection()
        return giocatori