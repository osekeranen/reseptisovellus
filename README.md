# Reseptisovellus

## Yleistä

Reseptisovellus on tällä hetkellä vielä hieman alkukantainen ja käyttöliittymältään karu reseptien hallintasovellus. [Herokussa](https://retsept-app.herokuapp.com/) sovellukseen voi lisätä reseptejä käyttämällä uusi resepti nappia. Huomaa että sovellukseen ei ole vielä tehty virheenhallintaa vaan ainekset tulee luetella muodossa "määrä mittayksikkö ainesosa" ja mittayksiköiden ja ainesosien tulee olla jo ennalta luotuja. Lisäksi mittayksiköitä käyttäessä tulee käyttää lyhenteitä, jotka löydät sivun alalaidasta ja ainesosia määritellessä partitiivia, jotka löytyy myös sivun alalaidasta.

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
