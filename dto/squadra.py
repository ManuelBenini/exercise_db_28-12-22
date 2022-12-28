class Squadra:
    
    def __init__(self, **kwargs):
        if kwargs.get('nazione') != None:
            self.nazione = kwargs.get('nazione')
        if kwargs.get('anno') != None:
            self._anno = kwargs.get('anno')
        if kwargs.get('allenatore') != None:
            self._allenatore = kwargs.get('allenatore')
        if kwargs.get('posizioneInClassifica') != None:
            self._posizioneInClassifica = kwargs.get('posizioneInClassifica')
            
        self.string = ''
        for key in kwargs:
            if list(kwargs)[-1] == key:
                self.string += f'{key} = {kwargs[key]}.'
            else:
                self.string += f'{key} = {kwargs[key]}, '
        
    @property
    def nazione(self):
        return self._nazione
    
    @property
    def anno(self):
        return self._anno
    
    @property
    def allenatore(self):
        return self._allenatore
    
    @property
    def posizioneInClassifica(self):
        return self._posizioneInClassifica
    
    @nazione.setter
    def nazione(self, nazione):
        self._nazione = nazione
        
    @anno.setter
    def anno(self, anno):
        self._anno = anno
    
    @allenatore.setter
    def allenatore(self, allenatore):
        self._allenatore = allenatore
        
    @posizioneInClassifica.setter
    def posizioneInClassifica(self, posizioneInClassifica):
        self._posizioneInClassifica = posizioneInClassifica
        
    def __str__(self):
        return self.string