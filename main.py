from dao.giocatoreDao import GiocatoreDao
from dao.organizzazioneDao import OrganizzazioneDao


# 1
nazioni = OrganizzazioneDao.getNationWhoNeverWonAWorldCompetitionHostedInTheirNation()

print("\nNazioni che non hanno mai vinto un mondiale organizzato da loro:")
for nazione in nazioni:
    
    print(nazione)


# 2
organizzazioni = OrganizzazioneDao.getNationWithMorePlayersByYear()

print("\nNazioni che hanno convocato il numero più elevato di giocatori in ogni campionato:")
for nazione in organizzazioni:
    
    print(nazione)
    
    
# 3
giocatori = GiocatoreDao.getPlayersNameWith3DifferentPartecipationORwithMoreNationality()

print("\nGiocatori che hanno giocato in almeno 3 edizioni diverse dei mondiali o con 2 nazioni differenti:")
for giocatore in giocatori:
    
    print(giocatore)