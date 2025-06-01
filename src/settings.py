import os 
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))

# Hotpepper (Ref: https://webservice.recruit.co.jp/doc/hotpepper/reference.html)
RECRUIT_API_KEY = os.environ.get("RECRUIT_API_KEY")
HOTPEPPER_ENDPOINT_SEARCH = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"