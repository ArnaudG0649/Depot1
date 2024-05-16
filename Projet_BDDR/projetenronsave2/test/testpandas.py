 #!/bin/env python3

import os
import os.path as osp 
import pandas as pds


DF=pds.read_csv("mails_jour.csv",index_col=0)
print(DF)
DF["Total"]=DF["internes_externes"]+DF["internes"]
print(DF)

print(DF.sort_values("Total",ascending=False))
