import argparse
from azure.storage.blob import BlobClient

parser = argparse.ArgumentParser()
parser.add_argument("rivit", help="Syötä lukuna, kuinka monta riviä haluat tulostaa", type=int)
args = parser.parse_args()

blob = BlobClient.from_connection_string(conn_str="<connectionstring>", container_name="<container>", blob_name="<blob>")

with open("./checkpoint1.txt", "wb") as my_blob:
    blob_data = blob.download_blob()
    blob_data.readinto(my_blob)

i = 0

with open("./checkpoint1.txt") as file:
    tiedosto = sorted(file)
    for rivi in tiedosto:
        if i < args.rivit:
            i += 1
            print(rivi)
