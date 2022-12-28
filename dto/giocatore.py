class Giocatore:
    
    def __init__(self, **kwargs):
        if kwargs.get('id') != None:
            self._id = kwargs.get('id')
        if kwargs.get('nome') != None:
            self._nome = kwargs.get('nome')
            
        self.string = ''
        for key in kwargs:
            if list(kwargs)[-1] == key:
                self.string += f'{key} = {kwargs[key]}.'
            else:
                self.string += f'{key} = {kwargs[key]}, '
        
    @property
    def id(self):
        return self._id
    
    @property
    def nome(self):
        return self._nome
    
    @id.setter
    def id(self, id):
        self._id = id
        
    @nome.setter
    def nome(self, nome):
        self._nome = nome
        
    def __str__(self):
        return self.string