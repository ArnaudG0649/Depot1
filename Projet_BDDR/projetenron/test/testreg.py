#!/usr/bin/env python3

import re

string="From: legal <.hall@enron.com>"
#string="From: mike.carson@enron.com"

if re.search(r"From: (\S*@\S*)",string) : 
    result=re.search(r"From: (\S*@\S*)",string).group(1) 
elif re.search(r"From:.* <(\S*@\S*)>",string) : 
    result=re.search(r"From:.* <(\S*@\S*)>",string).group(1) 
    
print(result)

if re.search(r"From: (\S*@\S*)",string) : 
    result=re.search(r"From: (\S*@\S*)",string).group(1) 
elif re.search(r"From: (.*>)",string) : 
    result=re.search(r"From: (.*>)",string).group(1) 
    
string.endswith(('enron.com','enron.com>'))
