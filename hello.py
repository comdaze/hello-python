import os
import uuid
import redis
import json
import urlparse
import pwd
import newrelic-admin
from flask import Flask


app = Flask(__name__)
my_uuid = str(uuid.uuid1())
BLUE = "#0099FF"
GREEN = "#33CC33"

COLOR = GREEN
count = 0
@app.route('/')
def hello():
    
    global count
    global value
    count += 1
    
    rediscloud_service = json.loads(os.environ['VCAP_SERVICES'])['rediscloud'][0]
    credentials = rediscloud_service['credentials']
    r = redis.Redis(host=credentials['hostname'], port=credentials['port'], password=credentials['password'])
    r.set('foo','bar')
    value = r.get('foo')
   
   #newrelic_service = json.loads(os.environ['VCAP_SERVICES'])['newrelic'][0]
   #credentials = newrelic_service['credentials']
   #lic = credentials['licenseKey']

    return """
    <html>
    <body bgcolor="{}">

    <center><h1><font color="white">Hi, I'm GUID:<br/>
    {}</br>
   <h2><font color="red">Count is: {}  
   <h3><font color="pink">Redis get value is: {}  

    </center>

    </body>
    </html>
    """.format(COLOR,my_uuid,count,value,)

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
