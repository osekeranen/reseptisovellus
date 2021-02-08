# Reseptisovellus

## Yleistä

Reseptisovellus on tällä hetkellä alkukantainen ja käyttöliittymältään karu reseptien hallintasovellus. [Herokussa](https://retsept-app.herokuapp.com/) sovelluksella ei tällä hetkellä juurikaan kykene leikkimään, sillä sovellukseen ei ole luotu vielä uusien reseptien luomisominaisuutta (reseptejä se kuitenkin jo tulostaa hyvin, mikäli haluat kokeilla omalla tietokoneellasi). Sovelluksen [tietokantarakenne](https://github.com/osekeranen/reseptisovellus/blob/main/database.md) on luotu siten että reseptit tallenetaan paloittain tietokantaan, eikä yksittäisenä html-tiedostona, kuten tämän kaltaisissa muissa sovelluksissa. Etuna tässä on että sovellukseen voi luoda erinomaiset hakuominaisuudet, joissa reseptejä voi hakea erinäisten ominaisuuksien, kuten yksittäisten ainesosien avulla.

## Suunnitellut ominaisuudet

### Sovelluksen välttämättömät ominaisuudet

  * käyttäjä voi tallentaa/poistaa erilaisia reseptejä
  * käyttäjä voi lukea tallennettuja reseptejä
  * käyttäjä voi antaa reseptille erilaisia tageja
  * käyttäjä voi etsiä sovelluksesta reseptejä
  * käyttäjä voi filtteröidä reseptejä erilaisten kriteerien avulla

### Muut alemman prioriteetin ominaisuudet

  * käyttäjä voi pyytää sovellusta valitsemaan jonkin reseptin hänen puolestaan
    * sovellus valitsee reseptin satunnaisesti tai joko käyttäjän antamien kriteerien perusteella
  * sovellukseen voi tallentaa oman jääkaapin sisällön ja sovellus ehdottaa käyttäjälle reseptiä, joka vaatii mahdollisimman vähän uusia aineksia
