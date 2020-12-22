from django.shortcuts import render
from .models import Gouvernorat,Statistique
import requests
from bs4 import BeautifulSoup as bs

# Create your views here.





def date_stat(text,mois):
  date = ''
  for m in mois.keys():
          if  text.split() [-2] == mois[m]:
              l = text.replace(')','').split()[7:]
              l[1] = m
              for c in l:
                  date += c
                  if len(c)< 3:
                      date += '/'
  return date


def statis_date(key,date,dicti,dic):
    i=0
    metaData = ['cas_positif','deces','guerison','cas_actif','datest','gouvernorat_FK']
    s = Statistique(cas_positif = dic[key.nom][0],deces=dic[key.nom][1],guerison=dic[key.nom][2],cas_actif=dic[key.nom][3],datest=date,gouvernorat_FK=key )
    s.save()


def getStatistique():

        url = "https://fr.wikipedia.org/wiki/Pand%C3%A9mie_de_Covid-19_en_Tunisie"

        mois = {'01':'janvier',	'02':'février',	'03':'mars',	'04':'avril',	'05':'mai',	'06':'juin',	'07':'juillet',	'08':'août',	'09':'septembre','10':	'octobre','11':	'novembre',	'12':'décembre'}

        response = requests.get(url)
        if response:
            soup = bs(response.text,'html.parser')
            script = soup.findAll('table',{'class':'wikitable'})
            dic = {}
            compt = 0
            c = ""
            k = ''
            for tr in script:
                t = tr.findAll('td')
                for g in t[:-2]:
                    c = str(compt)
                    if c[-1] == '0' or c[-1] == '5':
                        k=g.text.replace('\n',"")
                        dic[k] = []
                    else:
                        val = g.text.replace('\n',"")
                        dic[k].append(val.replace(u'\xa0', u' '))
                    compt +=1
            t1 = tr.find('caption').text
            date = date_stat(t1,mois)
                        
            i = 0
            Gouv = [v for v in dic][:-1]
            dicti = {}
            for e in Gouvernorat.objects.all():
                statis_date(e,date,dicti,dic)


            