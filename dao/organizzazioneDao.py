from dao.utility.db import MySql
from dto.organizzazione import Organizzazione

class OrganizzazioneDao:
    @classmethod
    def getAllOrganizations(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM organizzazione")
        results = MySql.getResults()
        organizzazioni = []
        for organizzazione in results:
            organizzazioni.append(Organizzazione(anno = organizzazione[0], nazione = organizzazione[1]))
        MySql.closeConnection()
        return organizzazioni
    
    @classmethod
    def getOrganizationByYear(cls, year):
        MySql.openConnection()
        MySql.query(f"SELECT * FROM organizzazione WHERE anno = {year}")
        results = MySql.getResults()
        organizzazione = Organizzazione(anno = results[0][0], nazione = results[0][1])
        MySql.closeConnection()
        return organizzazione
    
    @classmethod
    def getNationWhoNeverWonAWorldCompetitionHostedInTheirNation(cls):
        MySql.openConnection()
        MySql.query(f"SELECT s.Nazione \
                        FROM squadra s \
                        INNER JOIN organizzazione o ON s.Anno = o.Anno \
                        WHERE s.PosizioneInClassifica <> 1 AND o.Nazione = s.Nazione;")
        results = MySql.getResults()
        organizzazioni = []
        for organizzazione in results:
            organizzazioni.append(Organizzazione(nazione = organizzazione[0]))
        MySql.closeConnection()
        return organizzazioni
    
    @classmethod
    def getNationWithMorePlayersByYear(cls):
        MySql.openConnection()
        MySql.query(f"SELECT Anno, Nazione, COUNT(*) as NumeroConvocazioni \
                        FROM Partecipazione p \
                        GROUP BY Anno, Nazione \
                        HAVING COUNT(*) >= ALL (SELECT COUNT(*) \
                                                FROM Partecipazione \
                                                WHERE Anno = p.Anno \
                                                GROUP BY Nazione);")
        results = MySql.getResults()
        organizzazioni = []
        for organizzazione in results:
            organizzazioni.append(Organizzazione(anno = organizzazione[0], nazione = organizzazione[1]))
        MySql.closeConnection()
        return organizzazioni