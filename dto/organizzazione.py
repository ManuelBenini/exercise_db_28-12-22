class Organizzazione:
    
    def __init__(self, **kwargs):
        if kwargs.get('anno') != None:
            self._anno = kwargs.get('anno')
        if kwargs.get('nazione') != None:
            self._nazione = kwargs.get('nazione')
            
        self.string = ''
        for key in kwargs:
            if list(kwargs)[-1] == key:
                self.string += f'{key} = {kwargs[key]}.'
            else:
                self.string += f'{key} = {kwargs[key]}, '
        
    @property
    def anno(self):
        return self._anno
    
    @property
    def nazione(self):
        return self._nazione
    
    @anno.setter
    def anno(self, anno):
        self._anno = anno
        
    @nazione.setter
    def nazione(self, nazione):
        self._nazione = nazione
        
    def __str__(self):
        return self.string