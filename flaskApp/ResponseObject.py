
class ResponseObject():
    objekat = None
    error = None

    def __init__(self,objekat,error):
        self.objekat=objekat
        self.error = error

    def json(self):
        return{
            'objekat' : self.objekat,
            'error' : self.error
        } 