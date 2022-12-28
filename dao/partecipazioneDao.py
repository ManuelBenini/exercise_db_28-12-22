from dao.utility.db import MySql
from dto.partecipazione import Partecipazione

class PartecipazioneDao:
    @classmethod
    def getAllPartecipations(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM partecipazione")
        results = MySql.getResults()
        partecipazioni = []
        for partecipazione in results:
            partecipazioni.append(Partecipazione(id_giocatore = partecipazione[0], anno = partecipazione[1], nazione = partecipazione[2], ruolo = partecipazione[3], _goal_segnati = partecipazione[4]))
        MySql.closeConnection()
        return partecipazioni
    
    @classmethod
    def getPartecipationByPlayerIdAndYear(cls, player_id, year):
        MySql.openConnection()
        MySql.query(f"SELECT * FROM partecipazione WHERE IDGiocatore = {player_id} AND anno = {year}")
        results = MySql.getResults()
        partecipazione = Partecipazione(id_giocatore = results[0][0], anno = results[0][1], nazione = results[0][2], ruolo = results[0][3], _goal_segnati = results[0][4])
        MySql.closeConnection()
        return partecipazione