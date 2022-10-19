from woocommerce import API

wcapi = API(
    url="http://localhost:10004",
    consumer_key="ck_9834e91f26bcc34e11c10b46750eebb4b609b6fd",
    consumer_secret="cs_593dff8b16afb0baeca19f2d2fb1d553e91f9c5f",
    version="wc/v3"
)

r = wcapi.get("products")

import pprint
pprint.pprint(r.json())