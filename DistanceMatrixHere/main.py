import herepy
from ast import literal_eval

app_id='insert id here'
app_code='insert code here'
routingApi = herepy.RoutingApi(app_id, app_code)

response = routingApi.car_route([-41.30598, -73.4529],
                                [-41.38933, -73.46485],
                                [herepy.RouteMode.car, herepy.RouteMode.fastest])




data=literal_eval(str(response))
#print(data)
data=literal_eval(str(data["response"].get("route")[0]))
data=literal_eval(str(data["leg"][0]))
distance=data["length"]/1000

print("distancia",distance,"km")
      




