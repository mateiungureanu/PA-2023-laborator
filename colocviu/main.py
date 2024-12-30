# problema 1
# def citire_numere(fisier):
#     f = open(fisier, "r")
#     lista = [[int(x) for x in linie.split()] for linie in f.readlines()]
#     f.close()
#     return lista
#
#
# def prelucrare_liste(lista):
#     for linie in lista:
#         s = linie[:]
#         for i in range(len(s)):
#             if s[i] == min(s):
#                 linie.remove(s[i])
#     lmin = min(len(linie) for linie in lista)
#     rez = [linie[:lmin] for linie in lista]
#     return rez
#
#
# L = prelucrare_liste((citire_numere("numere.in")))
# for i in L:
#     print(*i)
#
# k = int(input("k="))
# g = open("cifre.out", "w")
# ok = 0
# for i in L:
#     for j in i:
#         if len(str(j)) == k:
#             g.write(str(j))
#             g.write(" ")
#             ok = 1
# if ok == 0:
#     g.write("Imposibil!")
# g.close()

# problema 2
# def sterge_ore(dic, cinema, film, *ore):
#     for o in ore:
#         dic[cinema][dic[cinema].index(film)+1].remove(o)
#     return dic
#
#
# def cinema_film(dic, ora_minima, ora_maxima, *cinema):
#     lista = []
#     for i in cinema:
#         for j in range(1, len(dic[i]), 2):
#             lista_ore = []
#             for ora in dic[i][j]:
#                 if int(ora_minima[:2] + ora_minima[3:]) <= int(ora[:2] + ora[3:]) < int(ora_maxima[:2] + ora_maxima[3:]):
#                     lista_ore += [ora]
#             if lista_ore:
#                 lista += [(dic[i][j-1], i, lista_ore)]
#     lista = sorted(lista, key=lambda x: (x[0][0], -len(x[2])))
#     return lista
#
#
# f = open("cinema.in", "r")
# d = {}
# for i in f.readlines():
#     if i.split('%')[0].strip() in d.keys():
#         d[i.split('%')[0].strip()] += [i.split('%')[1].strip(), i.split('%')[2].strip().split()]
#     else:
#         d[i.split('%')[0].strip()] = [i.split('%')[1].strip(), i.split('%')[2].strip().split()]
# f.close()
# print(d)
# print(sterge_ore(d, "Cinema 1", "Minionii 2", "18:30", "12:30"))
# print(cinema_film(d, "14:00", "22:00", "Cinema 1", "Cinema 2"))
