
import urllib.parse
import requests
from datetime import datetime
current_time = datetime.now()

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "wyiPWP2qNO0QYU2mzDjrzvRJFbAPXyTY"
while True:
    print("=================================")
    print("Bienvenido a Mapquest")
    print("Fecha y Hora Local\n:",current_time)
    print("=================================")
    orig = input("Ciudad de Origen: ")
    if orig == "e" or orig == "E":
        break
    dest = input("Ciudad de Destino: ")
    if dest == "e" or dest == "E":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    json_data = requests.get(url).json()
    print("URL: " + url)
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("Estado API : " + str(json_status) + " = Correcto.\n")
        print("=============================================")
        print("Ciudad de Origen " + (orig) + " Hasta " + (dest))
        print("Kilometros: " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Duracion de Viaje: " + (json_data["route"]["formattedTime"]))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
             print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Locacion invalida.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; No alcanzable las locaciones.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")