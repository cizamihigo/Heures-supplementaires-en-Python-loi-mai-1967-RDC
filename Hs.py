#Un travailleur doit avoir un salaire horaire
Sal_H = int(input("Entrer le salaire Horaire du travailleur: "))
#les heure de travail selon la legislation etant de 8h par jour, 48h par semaine...
H_Uno_Semaine =int(input("entrer les heures de travail durant la premiere semaine: "))
H_Duo_Semaine =int(input("entrer les heures de travail durant la deuxieme semaine: "))
H_Tir_semaine =int(input("entrer les heures de travail durant la troisieme semaine: "))
H_Quatro_semaine =int(input("entrer les heures de travail durant la quatrieme semaine: "))

H_Cumul = H_Uno_Semaine + H_Duo_Semaine + H_Tir_semaine + H_Quatro_semaine

print(H_Cumul)

if H_Cumul < 192:
    print("le travailleur a travaille moins d'heures que prevu. son salaire ne peux qu'en dependre")
    print("son salaire sera de {0}".format(Sal_H * H_Cumul))
    Sal_Hs = 0
    Tot_salaire = (Sal_H * H_Cumul) + Sal_Hs
elif H_Cumul == 192:
    print("le travailleur a acco;pli un travail au identique a son contract. ")
    Sal_Hs = 0
    Tot_salaire = (Sal_H * H_Cumul) + Sal_Hs
    print("le travailleur aura comme salaire: {0}".format(Tot_salaire))
elif H_Cumul > 192 :
    if H_Uno_Semaine > 48:
        H_non_prestes = 0
        salairebrut = Sal_H * 48
        Tot_salaire = salairebrut
        H_Uno_Semaine -= 48
        print("Salaire Brut 1ere semaine: {0}".format(salairebrut))
        H_repos_dimanche = int(input("pendant la premiere semaine a-t-il travaillé les dimanche si oui indiqez les heures: "))
        augmentation_J_repos = Sal_H *100 * H_repos_dimanche /100
        print("augmentation jour des repos, conges payes et dimanche: {0}".format(augmentation_J_repos))
        H_Uno_Semaine -= H_repos_dimanche
        
        Tot_salaire += augmentation_J_repos
        print("Salaire apres augmanetation des conges payes: {0}".format(Tot_salaire))
        print("Heure de travail restant: {0}".format(H_Uno_Semaine))
        #les autres heures restantes sont supplemetaires
        H_sup = H_Uno_Semaine
        if H_sup >= 6 :
            augmentaion_H_6 = (Sal_H * 30 *6) / 100
            H_sup -= 6
            print("\tHeures supplementaires restant: {0} apres 6 Premieres Heures".format(H_sup))
            Tot_salaire += augmentaion_H_6
            print("6 Premiere Heures: {0} salaire total {1}".format(augmentaion_H_6,Tot_salaire))
        if 0 < H_sup :
            augmentaion_H_6 = 0
            augmentaion_H_6 += (Sal_H * 60 * H_sup) /100
            print("augmentation de salaire = {0}".format(augmentaion_H_6))

            Tot_salaire += augmentaion_H_6
            print("Les Heures allant au delà de 6 heures de travail supplementaire: {0}".format(Tot_salaire))
    elif H_Uno_Semaine < 48 :
        H_non_prestes = 48 - H_Uno_Semaine
        print("ces Heures affecterons la semaine prochaine")
        print("Heures non-Prestées prémière semaine: {0}".format(H_non_prestes))
        #sachant que les heures nons prestees serons compenses par les semaines a venir il convient de remarquer
        # que les heures non prestées vont se repercuter sur les semaines à venir jusqu'à la derniere
        # semaine puisque le cumul lui même étant déjà superieur à 192. Donc elle va se repercuter jusqu'à la se
        # -maine qui aura le plus de jours de compasation prestée.
        Tot_salaire = Sal_H * 48 #connaisant que ces heures seront compensées tot ou tard dans le meme mois.
        print("Le salaire Total pour cette semaine est de: {0}".format(Tot_salaire)) 
    elif H_Uno_Semaine == 48 :
        H_non_prestes = 0
        Tot_salaire = (Sal_H * 8 * 6) # salare horaire * 48 heure par semaine
        print("son salaire est de: " + str(Tot_salaire))
    # =========================================================================== #
    #                               DEUXIEME SEMAINE                              #
    #============================================================================ #
    if H_Duo_Semaine < 48 :
        H_non_prestes += (48 - H_Duo_Semaine)
        print("les heures non prestees sont  maintenant de: {0}".format(H_non_prestes))
        Tot_salaire = Sal_H * 48
        print("Le salaire de cette semaine est de: {0}".format(Tot_salaire))
    elif H_Duo_Semaine == 48:
        H_non_prestes += H_non_prestes
        print("Les heures non prestées sont toujours de {0}".format(H_non_prestes))
        Tot_salaire += Sal_H * 48
        print("Le salaire de cette semaine est de: {0}".format(Tot_salaire))
    elif H_Duo_Semaine > 48:
        H_sup = H_Duo_Semaine - 48
        if H_sup >= H_non_prestes:
            H_sup = H_sup - H_non_prestes
            print("Les heures supplementaires restant: {0}".format(H_sup))
            salairebrut = 48 * Sal_H
            print("le salaire brut est de: {0}".format(salairebrut)) 
            H_repos_dimanche = 0
            H_repos_dimanche = int(input("pendant la deuxieme semaine a-t-il travaillé les dimanche. indiqez les heures ou 0: "))
            augmentation_J_repos = 0
            augmentation_J_repos = Sal_H *100 * H_repos_dimanche /100
            print("augmentation jour des repos, conges payes et dimanche: {0}".format(augmentation_J_repos))
            sous_tot2s = salairebrut + augmentation_J_repos
            print("sous total deuxieme semaine " + str(sous_tot2s))
            s2 = sous_tot2s
            Tot_salaire += sous_tot2s


            
            if H_sup >= 6 :
                augmentaion_H_6 = 0
                augmentaion_H_6 = (Sal_H * 30 *6) / 100
                H_sup -= 6
                print("\tHeures supplementaires restant: {0} apres 6 Premieres Heures deuxieme semaine".format(H_sup))
                sous_tot2s += augmentaion_H_6
                print("6 Premiere Heures: {0} salaire sous total {1}".format(augmentaion_H_6,sous_tot2s))
            
            if 0 < H_sup :
                augmentaion_H_6 = 0
                augmentaion_H_6 += (Sal_H * 60 * H_sup) /100
                print("augmentation de salaire deuxieme semaine = {0}".format(augmentaion_H_6))

                s2 += augmentaion_H_6
                print("Les Heures allant au delà de 6 heures de travail supplementaire: {0}".format(s2))
                Tot_salaire += s2
                print("Le total devient alors  "+ str(Tot_salaire))
                            

        if H_sup < H_non_prestes :
            H_non_prestes = H_non_prestes - H_sup
            H_sup = 0
            Tot_salaire += (Sal_H * 48)
            print("Heures non prestees alors: {0}".format(H_non_prestes))
            print("Le salaire Total sera de: {0}".format(Tot_salaire))
    #text
    # =========================================================================== #
    #                              TROISIEME SEMAINE                              #
    #============================================================================ #

# etant donné qu'on ne devrait pas avoir d'heures non prestés pendant la derniere semaine; 
# il est donc important de comparer avant tout la 3e semaine mais cela devrait aussi 
# etre fait avec la deuxieme semaine: dans la logique des heures non prestées on devrait commencer par 
# comparer les heures non prestées puis par la suite executer les semaines à la suite des autres en tenant compte des heures les moins prestés.

    ret4 =H_Quatro_semaine - 48
    ret3 = H_Tir_semaine - 48
    if ret4 > ret3:
        H_non_prestes += ret4
        if H_Tir_semaine > 48:
            H_sup= H_Tir_semaine - 48
            if H_sup > H_non_prestes:
                H_sup -= H_non_prestes
                sous_tot2s = 0
                if H_sup >= 6 :
                    augmentaion_H_6 = 0 
                    augmentaion_H_6 = (Sal_H * 30 *6) / 100
                    H_sup -= 6
                    print("\tHeures supplementaires restant: {0} apres 6 Premieres Heures".format(H_sup))
                    sous_tot2s += augmentaion_H_6
                    print("6 Premiere Heures: {0} salaire total {1}".format(augmentaion_H_6,sous_tot2s))
                if 0 < H_sup :
                    augmentaion_H_6 = 0
                    augmentaion_H_6 += (Sal_H * 60 * H_sup) /100
                    print("augmentation de salaire = {0}".format(augmentaion_H_6))
                    s2 =0
                    s2 = sous_tot2s

                    s2 += augmentaion_H_6
                    print("Les Heures allant au delà de 6 heures de travail supplementaire: {0}".format(s2))

                    Tot_salaire += s2
                    print("SALAIRE TOTAL A CE NIVEAU: " + str(Tot_salaire))

            else:
                #implement your own code for this case
                pass
    ###########################################################################################
    # WHATS REMAINING:
    # CALCULATE THE 4th WEEK SALAIRE SUPPLEMENTAIRE
    # AND THEN IMPLEMENT THE TOTAL SALARY .......THATS IT.
    ###########################################################################################
            

                
            


