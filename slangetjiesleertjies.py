#%%
import numpy as np
import random
import matplotlib.pyplot as plt
  

#%%
# Gewone bord:
# Stel bord en spel op
bord = np.linspace(0,100,101)
print(bord)

#%%
# Bord met Leertjies:
# Definieer slangetjies en leertjies
leertjies = np.array([1, 4, 9, 21, 28, 36, 51, 71, 80])
leerspringna = np.array([38, 14, 31, 42, 97, 57, 67, 91, 100])

np.put(bord, leertjies, leerspringna)


#%%
# Bord met slangetjies:
slangetjies = np.array([34,  49, 56, 62, 64, 87, 93, 95, 98])
slangsluk = np.array([15, 11, 53, 19, 60, 17, 74, 75, 78])
np.put(bord, slangetjies, slangsluk)

#%%
print(bord)
# %%


def dobbelsteen():
    # Kies lukraak waarde uit dobbelsteen
    dobbel = [1, 2, 3, 4, 5, 6]
    return random.choice(dobbel)

def speelbeurt(posisie):
    nuweposisie = posisie + dobbelsteen()

    return  nuweposisie

def speelpot(bord, wysresultaat = False):
    # Inisialiseer aantal gooie
    aantalgooie = 0

    # Begin spel van die bord af
    posisie = 0

    while posisie < 100:
        posisie += dobbelsteen()
        # Stel die posisie met slangetjies of leertjies 
        if posisie < 100:
            posisie = bord[int(posisie)]

        aantalgooie += 1
        
        if wysresultaat:
            print(str(aantalgooie) + ' ' + str(posisie))

    return aantalgooie

def speelstel(bord, aantalstelle = 1000):
    # Inisialiseer die resultaatskikking 
    gooiskikking = np.zeros(aantalstelle)

    # Speel die aantal speletjies
    for i in range(aantalstelle):
        gooiskikking[i] = speelpot(bord)

    return gooiskikking



# %%

x = np.array([1, 1, 3, 5, 10, 1, 1, 7])
x = speelstel(bord, 10000)
aantalhokke = 10

plt.hist(x, bins = aantalhokke)
plt.xlabel('Aantal gooie')
plt.ylabel('Aantal verskynsels')
plt.show()

# %%
# Gevolgtrekkings:
# 1.  Bord met geen slangetjies of leertjies is normaal versprei rondom 30
# 2.  Bord met slangetjies en leertjies verkort spel en maak dit 'n Weibull met minder aantal gooie as die normaal verspreide 
# 3.  Bord met net leertjies maak die spel vinniger, maar verspreiding is nog amper normaal
# 4.  Bord met net slangetjies maak spel baie langer, maar verspreiding is Weibull

# Teenspoed veroorsaak Weibull verspreiding.
# Mengsel van voorspoed en teenspoed is Weibull verspreiding.
# Met mengsel van voorspoed en teenspoed is spel geneig om nog steeds vinniger te gaan meestal.  Dit mag verduidelik hoekom vooruitgang in die algemeen plaasvind.
# Teenspoed veroorsaak lang sterte

# Kan loopbaan vordering modelleer (lere is bevordering, slange is terugslae)
# Kan ruimtereise met lukrake plasing van wurmgate modelleer
# Kan ekstreme onverwagse toestande modelleer (soos met aandelepryse) en die effek op portefeuljes
