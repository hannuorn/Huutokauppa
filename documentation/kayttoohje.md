# Käyttöohje

### Asennus

Sovellus löytyy [Herokusta](https://hhuutokauppa.herokuapp.com).

Asennus paikallisesti:

Kloonaa repositorio ja aja terminaalissa repositorion kansiossa:

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python3 run.py

Avaa tämän jälkeen nettiselaimella osoite

    http://localhost:5000


### Kirjautuminen ja tunnuksen luonti

Klikkaa **Login** etusivun oikeassa yläkulmassa. 
Syötä tunnus ja salasana, tai klikkaa **Sign up** luodaksesi uuden tunnuksen.


### Huutokaupan luonti

Valitse yläpalkista **Create an auction**. Syötä otsikko (**Title**) ja tarkempi kuvaus (**Description**).
Määrittele lähtöhinta kenttään **Minimum bid**. Valitse huutokaupan päättymispäivä.
Huutokaupat päättyvät aina klo 23.59 määriteltynä päättymispäivänä.

### Huutokauppojen listaus

Lista huutokaupoista tulostuu heti kirjautumisen jälkeen.
Listaan voi palata muilta sivuilta klikkaamlla yläpalkista **Active auctions**.
Huutokaupan tarkemman tiedot saa esiin klikkaamalla listasta huutokaupan nimeä.
Päättyneet huutokaupat löytyy kohdasta **Ended auctions**


### Huutokaupan katselusivu

Huutokaupan sivulla on kolme osaa: 
* **Auction details**, jossa kerrotaan kaupan perustiedot.
* **Bidding**, jossa näkyy lista huudoista, sekä mahdollisuus luoda uusi huuto.
* **Messages**, viestipalsta.

Huutokaupan tiedoissa huomionarvoisia kohtia ovat **Minimum bid** eli
lähtöhinta ja **Winning bid** eli tämänhetkinen korkein huuto ja huutaja.

Kohdassa **Ends** näkyy, milloin huutokauppa päättyy, ja montako päivää
päättymiseen on vielä jäljellä. Jos huutokauppa on jo päättynyt, rivillä
lukee **ended**.

Voit huutaa syöttämällä luvun kenttään **Bid amount** ja klikkaamalla
nappulaa **Place bid**. Huutosi tulee olla vähintään lähtöhinnan suuruinen
ja suurempi kuin korkein aiemmista huudoista. 

Voit kirjoittaa viestipalstalle viestin kenttään **Message** ja painamalla
nappulaa **Post message**. Alapuolella näkyy lista kaikista viesteistä
uusimmasta vanhimpaan. Huutokaupan myyjän kirjoittamat viestit näkyvät
lihavoituina. Omien viestiesi kohdalla näkyy nappula **Delete**, josta
voit poistaa kirjoittamasi viestin. Viestejä voi myös muokata nappulalla
**Edit**.

Jos huutokauppa on päättynyt, uusia huutoja tai viestejä ei voi enää luoda.
Sulkeutuneen huutokaupan myyjä näkee ostajan sähköpostiosoiteen kohdassa
**Winning bid**, ja vastaavasti ostaja näkee myyjän sähköpostiosoiteen
kohdassa **Seller**. Näin ostaja ja myyjä voivat ottaa toisiinsa yhteyttä
kaupantekoa varten.


### Käyttäjän tiedot ja uloskirjautuminen

Sisäänkirjautumisen jälkeen oikeassa yläreunassa on nyt Loginin sijasta
uloskirjautumislinkki **Logout** ja sen vasemmalla puolella käyttäjän nimi,
jota klikkaamalla avautuu valikko. Valitsemalla **My account** pääsee
käyttäjän omalle sivulle. Sivu listaa käyttäjän perustiedot, ne huutokaupat
joissa käyttäjä on myyjänä (My auctions), sekä huutokaupat,
joissa huutamiseen käyttäjä on osallistunut (My bids).

Käyttäjä voi muokata nimeään ja sähköpostiosoitettaan painamalla **Edit account**.
Käyttäjätunnusta tai salasanaa ei voi vaihtaa.

Kohdassa **My auctions** pääsee muokkaamaan omien huutokauppojensa tietoja (**Edit auction**),
tai poistamaan huutokaupan (**Delete auction**).
