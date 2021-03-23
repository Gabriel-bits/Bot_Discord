import os

temple_folder = "./templeites"
nomes = []
for root, subFold, fileName in os.walk(temple_folder):
    for NomeFiles in fileName:
        nomes.append(NomeFiles)
        
print(nomes)