# Käyttöohje

### Asennus

Sovellus löytyy [Herokusta](https://hhuutokauppa.herokuapp.com).


### Kirjautuminen ja tunnuksen luonti

Klikkaa **Login** etusivun oikeassa yläkulmassa. 
Syötä tunnus ja salasana, tai klikkaa **Sign up** luodaksesi uuden tunnuksen.


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

Voit huutaa syöttämällä luvun kenttään **Bid amount** ja klikkaamalla
nappulaa **Place bid**. Huutosi tulee olla vähintään lähtöhinnan suuruinen
ja suurempi kuin korkein aiemmista huudoista. 

Voit kirjoittaa viestipalstalle viestin kenttään **Message** ja painamalla
nappulaa **Post message**. Alapuolella näkyy lista kaikista viesteistä
uusimmasta vanhimpaan. Huutokaupan myyjän kirjoittamat viestit näkyvät
lihavoituina. Omien viestiesi kohdalla näkyy nappula **Delete**, josta
voit poistaa kirjoittamasi viestin.

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
