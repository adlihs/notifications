import http.client, urllib
conn = http.client.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.parse.urlencode({
    "token": "ao4owdr5mze34jks1pt3iryrn26z5a",
    "user": "ucz4hngocjn2zub71upf89ir3ho7z8",
    "message": "hello world",
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()