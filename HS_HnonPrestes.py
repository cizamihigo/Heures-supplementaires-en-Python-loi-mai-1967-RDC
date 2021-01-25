#Behing this
print("Heures supplementaires en RDC")
print()
H1 = int(input("Entrer les heures de travail premiere semaine: "))
H2 = int(input("Entrer les heures de travail deuxieme semaine: "))
H3 = int(input("Entrer les heures de travail troisieme semaine: "))
H4 = int(input("Entrer les heures de travail Quatrieme semaine: "))

#differnces

Dh1 = H1 - 48
Dh2 = H2 - 48
Dh3 = H3 - 48
Dh4 = H4 - 48

#cumul
Cheures = H1 + H2 + H3 + H4
Cdifferences = Dh1 + Dh2 + Dh3 + Dh4 
print("Cumul des heures : " + str(Cheures))
print("Cumul des diffrences : " + str(Cdifferences))

#LES VARIABLES
Sal_Final = 0
Sal_Horaire = int(input("Entrer le salaire Horaire: "))
Hsup1 = 0
salhs1 = 0
SalTotal = 0
HNonPrestees = 0

#TEST

if int(Cheures) < 192 :
    print("Vous n'avez pas travailler la durée prévue dans le contrat. votre salaire doit en patir")
    Sal_Final = Cheures * Sal_Horaire
    print("Salaire Mensuel {0}".format(Sal_Final))
    print("Heures non prestées {0} ".format(Cdifferences))
if int(Cheures) == 192 :
    print("Vous avez Avez accompli votre travail sans encombre votre salaire est comme stipulé dans le contrat")
    Sal_Final = Cheures * Sal_Final
    print("Salaire Mensuel {0}".format(Sal_Final))
if int(Cheures) > 192 :
    if Dh1 < Dh2 and Dh1 < Dh3 and Dh1 < Dh4 :
        if H1 > 48 :
            Hsup1 = H1 - 48
            print("Les heures supplémentaires sont:" + str(Hsup1))
            if int(Hsup1) >= 6 :

                salhs1 += (Sal_Horaire * 30 * 6) / 100
                Hsup1  -=6
                print("Le salaire supplementaire = {0} et les heures supplemetaires restant sont de {1} ".format(salhs1, Hsup1))
                SalTotal += (48 * Sal_Horaire) + salhs1
                salhs1 = 0
                Sal_Final = SalTotal
            elif int(Hsup1) > 0 :
                salhs1 = (Sal_Horaire * 60 * Hsup1) / 100
                Hsup1 = 0
                print("Le salaire des heures au dela de 6 heures = {0}.".format(salhs1))
                SalTotal += salhs1
                Sal_Final = SalTotal 
        elif H1 < 48 :
            HNonPrestees += 48 - H1
            SalTotal = 48 * Sal_Horaire
            Sal_Final += SalTotal
        if Dh2 < Dh3 and Dh2 < Dh4 :
            print("les heures Non Prestées sont de: " + str(HNonPrestees))
            H2 -= HNonPrestees
            HNonPrestees = 0
            if H2 > 48 :
                Hsup1 += H2 - 48
                print("Deuxieme semaine: Les heures supplémentaires sont:" + str(Hsup1))
            if int(Hsup1) >= 6 :

                salhs1 += (Sal_Horaire * 30 * 6) / 100
                Hsup1  -=6
                print("Deuxieme Semaine: Le salaire supplementaire = {0} et les heures supplemetaires restant sont de {1} ".format(salhs1, Hsup1))
                SalTotal += (48 * Sal_Horaire) + salhs1
                salhs1 = 0
                Sal_Final = SalTotal
            elif int(Hsup1) > 0 :
                salhs1 = (Sal_Horaire * 60 * Hsup1) / 100
                Hsup1 = 0
                print("2e SEMAINE: Le salaire des heures au dela de 6 heures = {0}.".format(salhs1))
                SalTotal += salhs1
                Sal_Final = SalTotal 
            elif H2 < 48 :
                HNonPrestees += 48 - H2
                SalTotal = 48 * Sal_Horaire
                Sal_Final += SalTotal
        if H3 < H4:
            print("les heures Non Prestées sont de: " + str(HNonPrestees))
            H3 -= HNonPrestees
            HNonPrestees = 0
            if H2 > 48 :
                Hsup1 += H3 - 48
                print("Troiseme semaine: Les heures supplémentaires sont:" + str(Hsup1))
            if int(Hsup1) >= 6 :

                salhs1 += (Sal_Horaire * 30 * 6) / 100
                Hsup1  -=6
                print("Troisieme Semaine: Le salaire supplementaire = {0} et les heures supplemetaires restant sont de {1} ".format(salhs1, Hsup1))
                SalTotal += (48 * Sal_Horaire) + salhs1
                salhs1 = 0
                Sal_Final = SalTotal
            elif int(Hsup1) > 0 :
                salhs1 = (Sal_Horaire * 60 * Hsup1) / 100
                Hsup1 = 0
                print("3e SEMAINE: Le salaire des heures au dela de 6 heures = {0}.".format(salhs1))
                SalTotal += salhs1
                Sal_Final = SalTotal 
            elif H3 < 48 :
                HNonPrestees += 48 - H3
                SalTotal = 48 * Sal_Horaire
                Sal_Final += SalTotal
            if H4 > 48:
                H4 -= HNonPrestees
                HNonPrestees = 0
                Hsup1 += H4 - 48
                print("4eme semaine semaine: Les heures supplémentaires sont:" + str(Hsup1))
                if int(Hsup1) >= 6 :

                    salhs1 += (Sal_Horaire * 30 * 6) / 100
                    Hsup1  -=6
                    print("Quatrieme Semaine: Le salaire supplementaire 6 premieres Heures = {0} et les heures supplemetaires restant sont de {1} ".format(salhs1, Hsup1))
                    SalTotal += (48 * Sal_Horaire) + salhs1
                    salhs1 = 0
                    Sal_Final += SalTotal
                if int(Hsup1) > 0 :
                    salhs1 = (Sal_Horaire * 60 * Hsup1) / 100
                    
                    print("4e SEMAINE: Le salaire des heures au dela de 6 heures = {0}.".format(salhs1))
                    Hsup1 = 0
                    SalTotal += salhs1
                    Sal_Final += SalTotal 
                    print("salaire Final = {0}".format(Sal_Final))

    if Dh2 < Dh1 and Dh2 < Dh3 and Dh2 < Dh4 :

        if H2 > 48 :
            Hsup1 = H2 - 48
            print("Les heures supplémentaires sont:" + str(Hsup1))
            if int(Hsup1) >= 6 :

                salhs1 += (Sal_Horaire * 30 * 6) / 100
                Hsup1  -=6
                print("Le salaire supplementaire = {0} et les heures supplemetaires restant sont de {1} ".format(salhs1, Hsup1))
                SalTotal += (48 * Sal_Horaire) + salhs1
                salhs1 = 0
                Sal_Final = SalTotal
            elif int(Hsup1) > 0 :
                salhs1 = (Sal_Horaire * 60 * Hsup1) / 100
                Hsup1 = 0
                print("Le salaire des heures au dela de 6 heures = {0}.".format(salhs1))
                SalTotal += salhs1
                Sal_Final = SalTotal 
        elif H2 < 48 :
            HNonPrestees += 48 - H1
            SalTotal = 48 * Sal_Horaire
            Sal_Final += SalTotal
        if Dh1 < Dh3 and Dh1 < Dh4 :
            print("les heures Non Prestées sont de: " + str(HNonPrestees))
            H1 -= HNonPrestees
            HNonPrestees = 0
            if H1 > 48 :
                Hsup1 += H2 - 48
                print("Deuxieme semaine: Les heures supplémentaires sont:" + str(Hsup1))
            if int(Hsup1) >= 6 :

                salhs1 += (Sal_Horaire * 30 * 6) / 100
                Hsup1  -=6
                print("Deuxieme Semaine: Le salaire supplementaire = {0} et les heures supplemetaires restant sont de {1} ".format(salhs1, Hsup1))
                SalTotal += (48 * Sal_Horaire) + salhs1
                salhs1 = 0
                Sal_Final = SalTotal
            elif int(Hsup1) > 0 :
                salhs1 = (Sal_Horaire * 60 * Hsup1) / 100
                Hsup1 = 0
                print("2e SEMAINE: Le salaire des heures au dela de 6 heures = {0}.".format(salhs1))
                SalTotal += salhs1
                Sal_Final = SalTotal 
            elif H1 < 48 :
                HNonPrestees += 48 - H2
                SalTotal = 48 * Sal_Horaire
                Sal_Final += SalTotal
        if H3 < H4:
            print("les heures Non Prestées sont de: " + str(HNonPrestees))
            H3 -= HNonPrestees
            HNonPrestees = 0
            if H2 > 48 :
                Hsup1 += H3 - 48
                print("Troiseme semaine: Les heures supplémentaires sont:" + str(Hsup1))
            if int(Hsup1) >= 6 :

                salhs1 += (Sal_Horaire * 30 * 6) / 100
                Hsup1  -=6
                print("Troisieme Semaine: Le salaire supplementaire = {0} et les heures supplemetaires restant sont de {1} ".format(salhs1, Hsup1))
                SalTotal += (48 * Sal_Horaire) + salhs1
                salhs1 = 0
                Sal_Final = SalTotal
            elif int(Hsup1) > 0 :
                salhs1 = (Sal_Horaire * 60 * Hsup1) / 100
                Hsup1 = 0
                print("3e SEMAINE: Le salaire des heures au dela de 6 heures = {0}.".format(salhs1))
                SalTotal += salhs1
                Sal_Final = SalTotal 
            elif H3 < 48 :
                HNonPrestees += 48 - H3
                SalTotal = 48 * Sal_Horaire
                Sal_Final += SalTotal
            if H4 > 48:
                H4 -= HNonPrestees
                HNonPrestees = 0
                Hsup1 += H4 - 48
                print("4eme semaine semaine: Les heures supplémentaires sont:" + str(Hsup1))
                if int(Hsup1) >= 6 :

                    salhs1 += (Sal_Horaire * 30 * 6) / 100
                    Hsup1  -=6
                    print("Quatrieme Semaine: Le salaire supplementaire 6 premieres Heures = {0} et les heures supplemetaires restant sont de {1} ".format(salhs1, Hsup1))
                    SalTotal += (48 * Sal_Horaire) + salhs1
                    salhs1 = 0
                    Sal_Final += SalTotal
                if int(Hsup1) > 0 :
                    salhs1 = (Sal_Horaire * 60 * Hsup1) / 100
                    
                    print("4e SEMAINE: Le salaire des heures au dela de 6 heures = {0}.".format(salhs1))
                    Hsup1 = 0
                    SalTotal += salhs1
                    Sal_Final += SalTotal 
                    print("salaire Final = {0}".format(Sal_Final))

    if Dh3 < Dh1 and Dh3 < Dh2 and Dh1 < Dh4 :
        if H3 > 48 :
            Hsup1 = H3 - 48
            print("Les heures supplémentaires sont:" + str(Hsup1))
            if int(Hsup1) >= 6 :

                salhs1 += (Sal_Horaire * 30 * 6) / 100
                Hsup1  -=6
                print("Le salaire supplementaire = {0} et les heures supplemetaires restant sont de {1} ".format(salhs1, Hsup1))
                SalTotal += (48 * Sal_Horaire) + salhs1
                salhs1 = 0
                Sal_Final = SalTotal
            elif int(Hsup1) > 0 :
                salhs1 = (Sal_Horaire * 60 * Hsup1) / 100
                Hsup1 = 0
                print("Le salaire des heures au dela de 6 heures = {0}.".format(salhs1))
                SalTotal += salhs1
                Sal_Final = SalTotal 
        elif H3 < 48 :
            HNonPrestees += 48 - H1
            SalTotal = 48 * Sal_Horaire
            Sal_Final += SalTotal
        if Dh1 < Dh2 and Dh1 < Dh4 :
            print("les heures Non Prestées sont de: " + str(HNonPrestees))
            H1 -= HNonPrestees
            HNonPrestees = 0
            if H1 > 48 :
                Hsup1 += H2 - 48
                print("Deuxieme semaine: Les heures supplémentaires sont:" + str(Hsup1))
            if int(Hsup1) >= 6 :

                salhs1 += (Sal_Horaire * 30 * 6) / 100
                Hsup1  -=6
                print("Deuxieme Semaine: Le salaire supplementaire = {0} et les heures supplemetaires restant sont de {1} ".format(salhs1, Hsup1))
                SalTotal += (48 * Sal_Horaire) + salhs1
                salhs1 = 0
                Sal_Final = SalTotal
            elif int(Hsup1) > 0 :
                salhs1 = (Sal_Horaire * 60 * Hsup1) / 100
                Hsup1 = 0
                print("2e SEMAINE: Le salaire des heures au dela de 6 heures = {0}.".format(salhs1))
                SalTotal += salhs1
                Sal_Final = SalTotal 
            elif H1 < 48 :
                HNonPrestees += 48 - H2
                SalTotal = 48 * Sal_Horaire
                Sal_Final += SalTotal
        if H2 < H4:
            print("les heures Non Prestées sont de: " + str(HNonPrestees))
            H3 -= HNonPrestees
            HNonPrestees = 0
            if H2 > 48 :
                Hsup1 += H3 - 48
                print("Troiseme semaine: Les heures supplémentaires sont:" + str(Hsup1))
            if int(Hsup1) >= 6 :

                salhs1 += (Sal_Horaire * 30 * 6) / 100
                Hsup1  -=6
                print("Troisieme Semaine: Le salaire supplementaire = {0} et les heures supplemetaires restant sont de {1} ".format(salhs1, Hsup1))
                SalTotal += (48 * Sal_Horaire) + salhs1
                salhs1 = 0
                Sal_Final = SalTotal
            elif int(Hsup1) > 0 :
                salhs1 = (Sal_Horaire * 60 * Hsup1) / 100
                Hsup1 = 0
                print("3e SEMAINE: Le salaire des heures au dela de 6 heures = {0}.".format(salhs1))
                SalTotal += salhs1
                Sal_Final = SalTotal 
            elif H2 < 48 :
                HNonPrestees += 48 - H3
                SalTotal = 48 * Sal_Horaire
                Sal_Final += SalTotal
            if H4 > 48:
                H4 -= HNonPrestees
                HNonPrestees = 0
                Hsup1 += H4 - 48
                print("4eme semaine semaine: Les heures supplémentaires sont:" + str(Hsup1))
                if int(Hsup1) >= 6 :

                    salhs1 += (Sal_Horaire * 30 * 6) / 100
                    Hsup1  -=6
                    print("Quatrieme Semaine: Le salaire supplementaire 6 premieres Heures = {0} et les heures supplemetaires restant sont de {1} ".format(salhs1, Hsup1))
                    SalTotal += (48 * Sal_Horaire) + salhs1
                    salhs1 = 0
                    Sal_Final += SalTotal
                if int(Hsup1) > 0 :
                    salhs1 = (Sal_Horaire * 60 * Hsup1) / 100
                    
                    print("4e SEMAINE: Le salaire des heures au dela de 6 heures = {0}.".format(salhs1))
                    Hsup1 = 0
                    SalTotal += salhs1
                    Sal_Final += SalTotal 
                    print("salaire Final = {0}".format(Sal_Final))
    
    if Dh4 < Dh1 and Dh4 < Dh2 and Dh4 < Dh3 :
        if H4 > 48 :
            Hsup1 = H3 - 48
            print("Les heures supplémentaires sont:" + str(Hsup1))
            if int(Hsup1) >= 6 :

                salhs1 += (Sal_Horaire * 30 * 6) / 100
                Hsup1  -=6
                print("Le salaire supplementaire = {0} et les heures supplemetaires restant sont de {1} ".format(salhs1, Hsup1))
                SalTotal += (48 * Sal_Horaire) + salhs1
                salhs1 = 0
                Sal_Final = SalTotal
            elif int(Hsup1) > 0 :
                salhs1 = (Sal_Horaire * 60 * Hsup1) / 100
                Hsup1 = 0
                print("Le salaire des heures au dela de 6 heures = {0}.".format(salhs1))
                SalTotal += salhs1
                Sal_Final = SalTotal 
        elif H4 < 48 :
            HNonPrestees += 48 - H1
            SalTotal = 48 * Sal_Horaire
            Sal_Final += SalTotal
        if Dh1 < Dh3 and Dh1 < Dh2 :
            print("les heures Non Prestées sont de: " + str(HNonPrestees))
            H1 -= HNonPrestees
            HNonPrestees = 0
            if H1 > 48 :
                Hsup1 += H2 - 48
                print("Deuxieme semaine: Les heures supplémentaires sont:" + str(Hsup1))
            if int(Hsup1) >= 6 :

                salhs1 += (Sal_Horaire * 30 * 6) / 100
                Hsup1  -=6
                print("Deuxieme Semaine: Le salaire supplementaire = {0} et les heures supplemetaires restant sont de {1} ".format(salhs1, Hsup1))
                SalTotal += (48 * Sal_Horaire) + salhs1
                salhs1 = 0
                Sal_Final = SalTotal
            elif int(Hsup1) > 0 :
                salhs1 = (Sal_Horaire * 60 * Hsup1) / 100
                Hsup1 = 0
                print("2e SEMAINE: Le salaire des heures au dela de 6 heures = {0}.".format(salhs1))
                SalTotal += salhs1
                Sal_Final = SalTotal 
            elif H1 < 48 :
                HNonPrestees += 48 - H2
                SalTotal = 48 * Sal_Horaire
                Sal_Final += SalTotal
        if H2 < H3:
            print("les heures Non Prestées sont de: " + str(HNonPrestees))
            H3 -= HNonPrestees
            HNonPrestees = 0
            if H2 > 48 :
                Hsup1 += H3 - 48
                print("Troiseme semaine: Les heures supplémentaires sont:" + str(Hsup1))
            if int(Hsup1) >= 6 :

                salhs1 += (Sal_Horaire * 30 * 6) / 100
                Hsup1  -=6
                print("Troisieme Semaine: Le salaire supplementaire = {0} et les heures supplemetaires restant sont de {1} ".format(salhs1, Hsup1))
                SalTotal += (48 * Sal_Horaire) + salhs1
                salhs1 = 0
                Sal_Final = SalTotal
            elif int(Hsup1) > 0 :
                salhs1 = (Sal_Horaire * 60 * Hsup1) / 100
                Hsup1 = 0
                print("3e SEMAINE: Le salaire des heures au dela de 6 heures = {0}.".format(salhs1))
                SalTotal += salhs1
                Sal_Final = SalTotal 
            elif H2 < 48 :
                HNonPrestees += 48 - H3
                SalTotal = 48 * Sal_Horaire
                Sal_Final += SalTotal
            if H3 > 48:
                H3 -= HNonPrestees
                HNonPrestees = 0
                Hsup1 += H4 - 48
                print("4eme semaine semaine: Les heures supplémentaires sont:" + str(Hsup1))
                if int(Hsup1) >= 6 :

                    salhs1 += (Sal_Horaire * 30 * 6) / 100
                    Hsup1  -=6
                    print("Quatrieme Semaine: Le salaire supplementaire 6 premieres Heures = {0} et les heures supplemetaires restant sont de {1} ".format(salhs1, Hsup1))
                    SalTotal += (48 * Sal_Horaire) + salhs1
                    salhs1 = 0
                    Sal_Final += SalTotal
                if int(Hsup1) > 0 :
                    salhs1 = (Sal_Horaire * 60 * Hsup1) / 100
                    
                    print("4e SEMAINE: Le salaire des heures au dela de 6 heures = {0}.".format(salhs1))
                    Hsup1 = 0
                    SalTotal += salhs1
                    Sal_Final += SalTotal 
                    print("salaire Final = {0}".format(Sal_Final))
    

# c'etait le code de calcul des heures supplemenataire toujours sur base de la loi  de mai 1976 en Python
# la seule difference ce qu'on prend ici completement en consideration les heures non prestées et leurs compasation
# dans la nouvelle echance. cad la semaine suivante. c'est vraiment interresant de voir comment la machine peut
# grace a python profuire ce rapport en moins de deux seconde alors que cette tache prendra  a un humain au minimum 45 minutes 
# d'apres nos text et analyses.


# from TAKE.THE.RISK
# Enjoy using this code. you can alter, add it's conten!!!!!!!
