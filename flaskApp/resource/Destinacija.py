from flaskApp.models.Destinacija import Destinacija
from geopy.geocoders import Nominatim


class ResourceDestinacija:

    @classmethod
    def unesiDestinaciju(cls,data):
        try:
            destinacija = Destinacija(data['naziv'],ResourceDestinacija.vratiKoordinate(data['naziv'])[0],ResourceDestinacija.vratiKoordinate(data['naziv'])[1])
            destinacija.add()
            return {'Odgovor':'Uspesno je kreirana destinacija '+destinacija.naziv}
        except Exception as e:
            return {'Greska': e.args[0]}

    @classmethod
    def vratiKoordinate(cls,drzava):
        try:
            geolocator = Nominatim(user_agent="my_app")
            location = geolocator.geocode(drzava)
            return [location.latitude,location.longitude]
        except:
            return [0,0]

# print(ResourceDestinacija.vratiKoordinate('Beograd'))