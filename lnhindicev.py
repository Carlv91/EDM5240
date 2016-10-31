# coding utf-8

import csv
import requests
from bs4 import BeautifulSoup

url = "http://stats.nhlnumbers.com/players"

fichier = "contrats-lnh-2016-2017.csv"
# fichier1 = "joueurs1.html"
# fichier2 = "joueurs2.html"
# fichier3 = "joueurs3.html"
# fichier4 = "joueurs4.html"
# fichier5 = "joueurs5.html"
# fichier6 = "joueurs6.html"
# fichier7 = "joueurs7.html"

entetes = {
    "User-agent":"Carl Vaillancourt - Requête pour travail universitaire dans le cadre du cours EDM5240",
    "From":"carl.vaillancourt.journaliste@gmail.com"
}
i = 0
for nb in range(1,8):
    # print("fichier{}".format(nb))
    contenu = open("joueurs{}.html".format(nb))
    page = BeautifulSoup(contenu,"html.parser")
    #print(page)

    # contenu = requests.get(fichier1, headers=entetes)

    # i = 0

    for a in page.find_all("a"):
        # if i != 0: 
        #print(a)
        lien = a.get("href")
        #print(lien)
        if lien[0:41] == "http://stats.nhlnumbers.com/player_stats/":
            # print(lien[42:47])
            if lien[40:46] != "/year/":
                if lien[40:50] != "/position/":
                    #print(i,lien)
                    i += 1
                    codejoueur = lien[41:]
                    #print(codejoueur)
                    
                    url = "http://stats.nhlnumbers.com/player_stats/" + codejoueur
                    print(url)
                    joueur = requests.get(url,headers=entetes)
                    p = BeautifulSoup(joueur.text,"html.parser")
                    # print(p)
                    
                    salaire = p.find("table",id="salary-data")
                    # print(salaire)
                    salaire2016 = salaire.find_all("td")
                    if len(salaire2016) > 9:
                        #print(salaire2016[13].text)
                        sal2016 = float(salaire2016[13].text)
                    
                        stat = p.find("table", id="stats-data")
                        #print(stat)
                        stat2016 = stat.find_all("td")
                        if len(stat2016) > 17:
                            #print(stat2016[22].text)
                            st2016 = float(stat2016[22].text)
                            
                            indice = st2016/sal2016
                            #print(indice)
                            
                            indice2 = (sal2016/st2016) * 1000000
                            #print(indice2)
                        
                    
                            fiche =[]   
                            fiche.append(codejoueur)
                            #print(fiche)
                            
                            datafiche = open(contenu,"r")
                            donneeraffinee = csv.writer(datafiche)
                            donneeraffinee.writerow(fiche)
                            
                            i =+ 1
