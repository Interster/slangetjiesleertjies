# Slangetjies en leertjies

Die betekenis van hierdie eenvoudige spel vir verskeie alledaagse sake.

Die spel van slangetjies en leertjies is interessant omdat die byvoeging van onverwagse bevordering en vernedering 'n 2D spel verander in 'n meerdimensionele spel.

![](/Prente/1_Bord.jpg)

Hier die bostaande bord is kodeer in 'n python script om dit met 'n Monte Carlo-tipe simulasie te evalueer.

# Aannames

Die dobbelsteen wat gebruik word se uitkoms vir die spel is normaal versprei.

# Toepassings van die model

Die spel kan loopbaan vordering modelleer.  Lere verteenwoordig bevordering waar slange terugslae verteenwoordig.

Ruimtereise met lukrake plasing van wurmgate kan modelleer word die bord uitleg.

Uiterste en onverwagse toestande kan modelleer word.  Voorbeelde sluit in aandelepryse of die vooruitgang van die mensdom.  

Aandelepryse is 'n spesifiek interessante toepassing aangesien portefeulje bestuur meestal die normaalverdeling aanvaar.  Dit sou dus net die gooi van 'n dobbelsteen wees wat die daaglikse prysskommeling met 'n normaalverdeling modelleer.  Indien die model van onverwagse stygings (lere) en onverwagse dalings (slangetjies) in die model bygevoeg word, het dit die gevolg dat die resultaat nie meer normaal verdeel is nie.

# Resultate

Die simulasie van 10000 speletjies vir elke geval lewer die volgende resultate op:

Die resultate word vertoon in 'n grafiek waar die aantal gooie van die dobbelsteen om die speletjie klaar te maak op die x-as is.  Die aantal kere wat 'n sekere aantal gooie voorkom in die 10000 simulasies is op die y-as van die histogram.

Indien daar geen slangetjies en leertjies is op die bord nie:

![](/Prente/2_BordAlleenResultaat.png)

Indien daar net lere op die bord is:

![](/Prente/3_ResultaatMetLere.png)

Indien daar net slangetjies op die bord is:

![](/Prente/4_ResultaatMetSlange.png)

Indien daar beide slangetjies en leertjies op die bord is:

![](/Prente/5_ResultaatSlangetjiesLeertjies.png)


## Gevolgtrekkings:

1.  Bord met geen slangetjies of leertjies is normaal versprei rondom 30 gooie
2.  Bord met slangetjies en leertjies verkort spel en maak dit 'n Weibull met minder aantal gooie as die normaal verspreide 
3.  Bord met net leertjies maak die spel vinniger, maar verspreiding is nog amper normaal
4.  Bord met net slangetjies maak spel baie langer, maar verspreiding is Weibull

Teenspoed veroorsaak Weibull of Rayleigh tipe verspreiding.

'n Mengsel van voorspoed en teenspoed is Weibull verspreiding.

Met 'n mengsel van voorspoed en teenspoed is spel geneig om nog steeds vinniger te gaan in meeste gevalle.  Dit mag verduidelik hoekom vooruitgang in die algemeen plaasvind, ten spyte van groot terugslae.

Teenspoed veroorsaak lang sterte in die verdeling.


