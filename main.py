
from cloudevents.http import CloudEvent
from google.cloud import storage

import functions_framework

# This fires when there is a change in the bucket

@functions_framework.cloud_event
def move_file_gcs(cloud_event: CloudEvent) -> tuple:
    data = cloud_event.data

    event_id = cloud_event["id"]
    event_type = cloud_event["type"]

    from_bucket = data["bucket"]
    name = data["name"]
    metageneration = data["metageneration"]
    timeCreated = data["timeCreated"]
    updated = data["updated"]

    to_bucket = "ashmore_green_delivery"

    storage_client = storage.Client()

    source_bucket = storage_client.bucket(from_bucket)
    source_blob = source_bucket.blob(name)
    destination_bucket = storage_client.bucket(to_bucket)
    destination_blob_name = name

    destination_generation_match_precondition = 0

    blob_copy = source_bucket.copy_blob(
        source_blob, destination_bucket, destination_blob_name, if_generation_match=destination_generation_match_precondition,
    )
    source_bucket.delete_blob(name)

    print("moved file", name, "to", to_bucket)

    return 0

