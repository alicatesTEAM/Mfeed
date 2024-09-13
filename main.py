import requests
import csv

ott_url = "https://ottcache.dof6.com/movistarplus/webplayer/OTT/contents/epg"
ott_csv_filepath = "ott.csv"
difusion_url = "https://ottcache.dof6.com/movistarplus/webplayer/DIFUSION/contents/epg"
difusion_csv_filepath = "difusion.csv"

def export_movistarEPG_to_csv(epg_url, filepath):

    response = requests.get(epg_url)
    if response.status_code == 200:
        movistarEPG = response.json()
    else:
        print("ERROR: movistarEPG no disponible")
        return

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
    with open(filepath, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers, delimiter=',')
        writer.writeheader()
        writer.writerows(csv_data)

    print(f"movistarEPG exported to {filepath}")


def flujo_vaginal():

    export_movistarEPG_to_csv(ott_url, ott_csv_filepath)
    export_movistarEPG_to_csv(difusion_url, difusion_csv_filepath)


flujo_vaginal()

