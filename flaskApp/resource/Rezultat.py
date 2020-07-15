from flaskApp.models.Rezultat import Rezultat
from flaskApp.models.Kviz import Nagrada
from flaskApp import scores

class RezultatResource:

    @classmethod
    def unesiRezultat(cls,korisnik,kviz,vrednost):
        try:
            rezultat = Rezultat(kviz,korisnik,vrednost)
            rezultat.add()
        except Exception as e:
            print('Greska '+str(e.args[0]))
    
    @classmethod
    def unesiRezultateKviza(cls,kviz_id):
        try:
            for i in scores:
                RezultatResource.unesiRezultat(i['user'],kviz_id,i['score'])
                for i in Nagrada.vrati_sve_za_kviz(kviz_id):
                    if i.rank-1 < len(scores):
                        i.update(scores[i.rank-1]['user'])  
        except Exception as e:
            print('Greska '+str(e))