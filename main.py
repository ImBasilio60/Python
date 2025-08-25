from Models.Tourist import Tourist

tourist = Tourist()

stoped = False
while not stoped:
    print("\nQu'est ce que vous voulez faire: \n\t1- Gerer les touristes \n\t2- Gerer les Groupes \n\t3- Quitter")
    res = input("\nVotre choix ?: ")

    if res == "1":
        print("\nVous voulez: \n\t1- créer \n\t2- modifier \n\t3- supprimer \n\t4- lister")
        action = input("\nVotre choix ?: ")

        if action == "1":
            nom = input("\nInserez le nom?: ")
            tourist.create_tourist(nom)
            print('Création...')
        elif action == "2":
            numero = input("\nInserez le numero?: ")
            if numero:
                nom = input("\nInserez le nom?: ")
                tourist.update_tourist(numero, nom)
                print('Update...')
        elif action == "3":
            numero = input("\nInserez le numero?: ")
            if numero:
                tourist.delete_tourist(numero)
                print('Delete...')
        elif action == "4":
            print(tourist.list_tourists())
        else:
            print("Option invalide")

    elif res == "2":
        print("\nVous voulez gérer les groupes ?")
        # Ici tu peux mettre le code pour gérer les groupes
    elif res == "3":
        stoped = True
        print("Processus terminé")
    else:
        print("Option invalide")
