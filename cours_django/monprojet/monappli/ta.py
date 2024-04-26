 #!/bin/env python3

import pandas as pds
import numpy as np

tableau=pds.DataFrame({'maman':[4,1],'papa':[7,9],'enfant':["issou","lol"]},index=[47,13])
tableau.columns
tableau.index[1]
M=np.asmatrix(tableau)
for i in range(M.shape[0]):
    for j in range(M.shape[1]):
        print(M[i,j])
        