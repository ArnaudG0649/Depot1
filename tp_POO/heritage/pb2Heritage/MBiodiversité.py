import Biodiversité as bio 

Cocotte=bio.Autruche('Cocotte')
print(Cocotte)
Cocotte.Fuite()


parcKruger = bio.Territoire()
parcKruger += bio.Autruche("Polux")
parcKruger += bio.Autruche("Cheetah")
parcKruger += bio.Chat("Zouzou")

print(parcKruger)

str(Cocotte)

parcKruger.alerte()
