import requests
import os

from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient
from azure.storage.blob import BlobClient

def jsonkasittely():
    tiedosto = requests.get("https://2ri98gd9i4.execute-api.us-east-1.amazonaws.com/dev/academy-checkpoint2-json")
    data = tiedosto.json()

    with open("checkpoint.txt", "a") as file:
        for i in data['items']:
            file.write(f'{i["parameter"]}\n')
    print("JSON-tiedosto parsittu ja data tallennettu tiedostoon")

def uusi_blob():

    SUBSCRIPTION_ID = os.environ.get("SUBSCRIPTION_ID", None)
    GROUP_NAME = "taaviRG20"
    STORAGE_ACCOUNT = "taavistorage20"
    BLOB_CONTAINER = "taaviblobtentti06"

    # Create client
    storage_client = StorageManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id=SUBSCRIPTION_ID
    )

    # Create blob container
    storage_client.blob_containers.create(
        GROUP_NAME,
        STORAGE_ACCOUNT,
        BLOB_CONTAINER,
        {}
    )
    print("Blob container tehty")

def upload_file():
    blob = BlobClient.from_connection_string(conn_str="<connectionstring>", container_name="<container>", blob_name="<blob>")

    with open("./checkpoint.txt", "rb") as data:
        blob.upload_blob(data)
    print("File tallennettu blobiin")


def main():
    jsonkasittely()
    uusi_blob()
    upload_file()

main()
