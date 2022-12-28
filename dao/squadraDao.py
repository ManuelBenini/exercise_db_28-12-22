from dao.utility.db import MySql
from dto.squadra import Squadra

class SquadraDao:
    @classmethod
    def getAllTeams(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM squadra")
        results = MySql.getResults()
        squadre = []
        for squadra in results:
            squadre.append(Squadra(nazione = squadra[0], anno = squadra[1], allenatore = squadra[2], posizioneInClassifica = squadra[3]))
        MySql.closeConnection()
        return squadre
    
    @classmethod
    def getTeamsByNationalityAndYear(cls, nation, year):
        MySql.openConnection()
        MySql.query(f"SELECT * FROM squadra WHERE nazione = '{nation}' AND anno = {year}")
        results = MySql.getResults()
        squadra = Squadra(nazione = results[0][0], anno = results[0][1], allenatore = results[0][2], posizioneInClassifica = results[0][3])
        MySql.closeConnection()
        return squadra