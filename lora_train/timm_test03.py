from pprint import pprint

import timm

model_names = timm.list_models("*resne*t*")
pprint(model_names)
