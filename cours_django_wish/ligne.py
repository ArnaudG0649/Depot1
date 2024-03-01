from models import Page


page1 = Page()
page1.page_url = "http://recherche.math.univ-angers.fr/spip.php?article29"
page1.save()                       # ≡ SQL INSERT


page2 = Page()
page2.page_url = "http://math.univ-angers.fr/spip.php?article3"
page2.save()                       # ≡ SQL INSERT

