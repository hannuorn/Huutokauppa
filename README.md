# Huutokauppa

## Osan 1 etapit

* [Linkki Herokuun](http://tsoha-demo-hannu.herokuapp.com/)
* [Linkki GitHubiin](https://github.com/hannuorn/tsoha-osa1)


## Osan 0 etapit

### Aiheen valinta

Yksinkertaisen nettihuutokaupan toteuttava tietokantasovellus. Käyttäjä luo ensin
itselleen tunnuksen, minkä jälkeen hän voi ilmoittaa tavaraa myytäväksi huutokaupassa
tai osallistua huutamiseen aktiivisissa huutokaupoissa. Kun huutokauppa sulkeutuu,
ostaja (korkeimman huudon tekijä) ja myyjä saavat toistensa yhteystiedot kaupantekoa
varten.


### Toimintoja

* käyttäjän luonti
* käyttäjätietojen muokkaus
* huutokaupan luonti
* aktiivisten huutokauppojen listaus ja katselu
* huutaminen
* niiden huutokauppojen listaus, joissa käyttäjä on osallistunut huutamiseen, sekä onko oma huuto voittava vai häviävä tällä hetkellä
* toteutuneiden kauppojen listaus ja yhteenvetotiedot


### Alustava tietokantakaavio

* Kayttaja((pk) id:Integer, nimi:String, puhelin:String, sahkoposti:String)
* Huutokauppa((pk) id:Integer, otsikko:String, kuvaus:String, (fk) myyja -> Kayttaja, lahtohinta:Integer, sulkeutumisaika:Date)
* Huuto((fk) huutokauppa -> Huutokauppa, (fk) huutaja -> Kayttaja, maara:Integer)


### Mahdollisia kehittyneempiä toimintoja

* myytävien tavaroiden lajittelu kategorioihin
* kysymyspalsta huutokauppojen yhteyteen
* korotusautomaatti
