# Application qui change un montant en monnaie
# Test de récursivité

change = [[100, '100$'], [50, '50$'], [20, '20$'], [10, '10$'], [5, '5$'], [2, '2$'], [1, '1$'], [0.25, '25¢'], [0.10, '10¢'], [0.05, '0.5¢'], [0.01, '1¢']]

def changeur(index, argent):
    x = int(argent / change[index][0])
    if x != 0:
        print (str(x) + " X " + str(change[index][1]))
    argent -= change[index][0] * x
    if index != (len(change) - 1):
        changeur(index + 1, argent)

print ("Quel montant souhaitez-vous changer: ")
montant = float(input())

changeur(0, montant)




