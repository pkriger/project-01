import os
import json



key_dict = {}
keys_json_path = os.path.expanduser(os.path.join("~", ".api_keys.json"))
if os.path.exists(keys_json_path):
    with open(keys_json_path, 'r') as keys_file:
        key_dict = json.load(keys_file)
else:
    print(f"Could not find {keys_json_path}")


#In your jupyter notebook add this
# Google API Key
#from config import key_dict
#gkey = key_dict['KEY NAME GOES HERE']
