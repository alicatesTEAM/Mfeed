import requests
import csv

movistarEPG_file_path = "movistarEPG.csv"
epg_url = "https://ottcache.dof6.com/movistarplus/webplayer/OTT/contents/epg"


def export_movistarEPG_to_csv():

    response = requests.get(epg_url)
    if response.status_code == 200:
        movistarEPG = response.json()
    else:
        print("ERROR: movistarEPG no disponible")
        exit(1)

    csv_data = []
    for indice, grupo in enumerate(movistarEPG):
        csv_data.append({
            "Nombre": grupo.get("Nombre", "").replace("\t", "").replace("\n", ""),
            "FormatoVideo": grupo.get("FormatoVideo", ""),
            "CodCadenaTv": grupo.get("CodCadenaTv", ""),
            "CasId": grupo.get("CasId", ""),
            "PuntoReproduccion": grupo.get("PuntoReproduccion", ""),

        })

    # Define CSV headers
    headers = ["Nombre", "FormatoVideo", "CodCadenaTv", "CasId", "PuntoReproduccion"]

    # Write CSV data to file
    with open(movistarEPG_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers, delimiter=',')
        writer.writeheader()
        writer.writerows(csv_data)

    print("movistarEPG se ha descargado")


export_movistarEPG_to_csv()
