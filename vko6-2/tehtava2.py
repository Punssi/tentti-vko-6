from azure.storage.blob import BlobClient




def lataa_blobista():
    blob = BlobClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=taavistorage20;AccountKey=1GTeymAe2t7vgQDBoaN4Xk/Lmz97ZLD278M1tTgP6+nuUH6Y9ROxxGInY1en/OmZH4tF6B/HSl0pNS9hir+5eg==;EndpointSuffix=core.windows.net", container_name="taaviblobtentti06", blob_name="checkpoint1.txt")

    with open("./checkpoint1.txt", "wb") as my_blob:
        blob_data = blob.download_blob()
        blob_data.readinto(my_blob)

def main():
    lataa_blobista()

main()

""" 
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("rivit", help="Syötä lukuna, kuinka monta riviä haluat tulostaa", type=int)
args = parser.parse_args()

print(args.rivit)"""