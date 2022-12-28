class Partecipazione:
    
    def __init__(self, **kwargs):
        if kwargs.get('id_giocatore') != None:
            self._id_giocatore = kwargs.get('id_giocatore')
        if kwargs.get('anno') != None:
            self._anno = kwargs.get('anno')
        if kwargs.get('nazione') != None:
            self._nazione = kwargs.get('nazione')
        if kwargs.get('ruolo') != None:
            self._ruolo = kwargs.get('ruolo')
        if kwargs.get('goal_segnati') != None:
            self._goal_segnati = kwargs.get('goal_segnati')
            
        self.string = ''
        for key in kwargs:
            if list(kwargs)[-1] == key:
                self.string += f'{key} = {kwargs[key]}.'
            else:
                self.string += f'{key} = {kwargs[key]}, '
        
    @property
    def id_giocatore(self):
        return self._id_giocatore
    
    @property
    def anno(self):
        return self._anno
    
    @property
    def nazione(self):
        return self._nazione
    
    @property
    def ruolo(self):
        return self._ruolo
    
    @property
    def goal_segnati(self):
        return self._goal_segnati
    
    @id_giocatore.setter
    def id_giocatore(self, id_giocatore):
        self._id_giocatore = id_giocatore
    
    @anno.setter
    def anno(self, anno):
        self._anno = anno
        
    @nazione.setter
    def nazione(self, nazione):
        self._nazione = nazione
        
    @ruolo.setter
    def ruolo(self, ruolo):
        self._ruolo = ruolo
        
    @goal_segnati.setter
    def goal_segnati(self, goal_segnati):
        self._goal_segnati = goal_segnati
        
    def __str__(self):
        return self.string