
# coding: utf-8

# In[12]:

import urllib.request, urllib.parse, urllib.error
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


# In[13]:


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    #print("Request:")
    #print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


# In[14]:

def processRequest(req):
    
    #baseurl = "https://query.yahooapis.com/v1/public/yql?"
    #yql_query = makeYqlQuery(req)
    #if yql_query is None:
    #    return {}
    #yql_url = baseurl + urllib.parse.urlencode({'q': yql_query}) + "&format=json"
    #result = urllib.request.urlopen(yql_url).read()
    data = "A cock was once strutting up and down the farmyard among the hens when suddenly he espied something shinning amid the straw. "
    #data = json.loads(result)
    res = makeWebhookResult(data)
    return res


# In[ ]:




# In[ ]:


def makeWebhookResult(data):
    
    return {
            "speech": data,
            "displayText": data,
            # "data": data,
            # "contextOut": [],
            "source": "apiai-weather-webhook-sample"
        }


# In[ ]:

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    #app.run(debug=False, port=port, host='0.0.0.0')
    app.run()
    #while(1): print('hello')

