fiat_2013 = int(input())
fiat_2014 = int(input())
fiat_2015 = int(input())
fiat_2016 = int(input())
fiat_2017 = int(input())
fiat_2018 = int(input())

ford_2013 = int(input())
ford_2014 = int(input())
ford_2015 = int(input())
ford_2016 = int(input())
ford_2017 = int(input())
ford_2018 = int(input())

gm_2013 = int(input())
gm_2014 = int(input())
gm_2015 = int(input())
gm_2016 = int(input())
gm_2017 = int(input())
gm_2018 = int(input())

vw_2013 = int(input())
vw_2014 = int(input())
vw_2015 = int(input())
vw_2016 = int(input())
vw_2017 = int(input())
vw_2018 = int(input())

ano = int(input())

if ano == 2013:
    if fiat_2013 > ford_2013 and fiat_2013 > gm_2013 and fiat_2013 > vw_2013:
        print("A fabricante que mais vendeu em 2013 foi a Fiat com {} mil unidades.".format(fiat_2013))
    elif ford_2013 > gm_2013 and ford_2013 > vw_2013:
        print("A fabricante que mais vendeu em 2013 foi a Ford com {} mil unidades.".format(ford_2013))
    elif gm_2013 > vw_2013:
        print("A fabricante que mais vendeu em 2013 foi a GM com {} mil unidades.".format(gm_2013))
    else:
        print("A fabricante que mais vendeu em 2013 foi a Volkswagen com {} mil unidades.".format(vw_2013))

elif ano == 2014:
    if fiat_2014 > ford_2014 and fiat_2014 > gm_2014 and fiat_2014 > vw_2014:
        print("A fabricante que mais vendeu em 2014 foi a Fiat com {} milvunidades.".format(fiat_2014))
    elif ford_2014 > gm_2014 and ford_2014 > vw_2014:
        print("A fabricante que mais vendeu em 2014 foi a Ford com {} mil unidades.".format(ford_2014))
    elif gm_2014 > vw_2014:
        print("A fabricante que mais vendeu em 2014 foi a GM com {} mil unidades.".format(gm_2014))
    else:
        print("A fabricante que mais vendeu em 2014 foi a Volkswagen com {} mil unidades.".format(vw_2014))

elif ano == 2015:
    if fiat_2015 > ford_2015 and fiat_2015 > gm_2015 and fiat_2015 > vw_2015:
        print("A fabricante que mais vendeu em 2015 foi a Fiat com {} mil unidades.".format(fiat_2015))
    elif ford_2015 > gm_2015 and ford_2015 > vw_2015:
        print("A fabricante que mais vendeu em 2015 foi a Ford com {} mil unidades.".format(ford_2015))
    elif gm_2015 > vw_2015:
        print("A fabricante que mais vendeu em 2015 foi a GM com {} mil unidades.".format(gm_2015))
    else:
        print("A fabricante que mais vendeu em 2015 foi a Volkswagen com {} mil unidades.".format(vw_2015))
        
elif ano == 2016:
    if fiat_2016 > ford_2016 and fiat_2016 > gm_2016 and fiat_2016 > vw_2016:
        print("A fabricante que mais vendeu em 2016 foi a Fiat com {} mil unidades.".format(fiat_2016))
    elif ford_2016 > gm_2016 and ford_2016 > vw_2016:
        print("A fabricante que mais vendeu em 2016 foi a Ford com {} mil unidades.".format(ford_2016))
    elif gm_2016 > vw_2016:
        print("A fabricante que mais vendeu em 2016 foi a GM com {} mil unidades.".format(gm_2016))
    else:
        print("A fabricante que mais vendeu em 2016 foi a Volkswagen com {} mil unidades.".format(vw_2016))

elif ano == 2017:
    if fiat_2017 > ford_2017 and fiat_2017 > gm_2017 and fiat_2017 > vw_2017:
        print("A fabricante que mais vendeu em 2017 foi a Fiat com {} mil unidades.".format(fiat_2017))
    elif ford_2017 > gm_2017 and ford_2017 > vw_2017:
        print("A fabricante que mais vendeu em 2017 foi a Ford com {} mil unidades.".format(ford_2017))
    elif gm_2017 > vw_2017:
        print("A fabricante que mais vendeu em 2017 foi a GM com {} mil unidades.".format(gm_2017))
    else:
        print("A fabricante que mais vendeu em 2017 foi a Volkswagen com {} mil unidades.".format(vw_2017))

elif ano == 2018:
    if fiat_2018 > ford_2018 and fiat_2018 > gm_2018 and fiat_2018 > vw_2018:
        print("A fabricante que mais vendeu em 2018 foi a Fiat com {} mil unidades.".format(fiat_2018))
    elif ford_2018 > gm_2018 and ford_2018 > vw_2018:
        print("A fabricante que mais vendeu em 2018 foi a Ford com {} mil unidades.".format(ford_2018))
    elif gm_2018 > vw_2018:
        print("A fabricante que mais vendeu em 2018 foi a GM com {} mil unidades.".format(gm_2018))
    else:
        print("A fabricante que mais vendeu em 2018 foi a Volkswagen com {} mil unidades.".format(vw_2018))

#total_2013 = fiat_2013 + ford_2013 + gm_2013 + vw_2013
#total_2014 = fiat_2014 + ford_2014 + gm_2014 + vw_2014
#total_2015 = fiat_2015 + ford_2015 + gm_2015 + vw_2015
#total_2016 = fiat_2016 + ford_2016 + gm_2016 + vw_2016
#total_2017 = fiat_2017 + ford_2017 + gm_2017 + vw_2017
#total_2018 = fiat_2018 + ford_2018 + gm_2018 + vw_2018

#print(total_2013)
#print(total_2014)
#print(total_2015)
#print(total_2016)
#print(total_2017)
#print(total_2018)

#criando a lista de vendas por ano para cada fabricante
fiat = list(map(int, input("Digite as vendas da Fiat para cada ano separadas por espaços: ").split()))
ford = list(map(int, input("Digite as vendas da Ford para cada ano separadas por espaços: ").split()))
gm = list(map(int, input("Digite as vendas da GM para cada ano separadas por espaços: ").split()))
volkswagen = list(map(int, input("Digite as vendas da Volkswagen para cada ano separadas por espaços: ").split()))

#criando a lista de vendas totais por ano
vendas_totais = []
for i in range(len(fiat)):
  soma = fiat[i] + ford[i] + gm[i] + volkswagen[i]
  vendas_totais.append(soma)

#encontrando o ano com a maior soma
maior_ano = vendas_totais.index(max(vendas_totais)) + 2013

print("O ano de maior volume geral de vendas foi", maior_ano, "com", soma, "mil unidades.")

import statistics

#criando uma lista de listas com as vendas por ano para cada fabricante
vendas_fabricantes = [fiat, ford, gm, volkswagen]

print("A média anual de vendas de cada fabricante entre 2013 e 2018 foi:")

#calculando a média anual para cada fabricante
for i in range(len(vendas_fabricantes)):
  media = statistics.mean(vendas_fabricantes[i])
  print("A Fiat vendeu em média", [][i], round(media, 2), "unidades por ano.")
  print("A Ford vendeu em média", [][i], round(media, 2), "unidades por ano.")
  print("A GM vendeu em média", [][i], round(media, 2), "unidades por ano.")
  print("A Wolkswagen vendeu em média", [][i], round(media, 2), "unidades por ano.")
