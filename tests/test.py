import sys
sys.path.append("")
from main import *

client = DisPy()
client.request_logging = True

client.auth("scraggjoshua@gmail.com", "Cooljs123")