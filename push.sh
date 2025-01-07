#!/usr/bin/bash

gcloud functions deploy python-finalize-function --gen2 --runtime=python312 --region=us-central1 --source=. --entry-point=move_file_gcs --trigger-event-filters="type=google.cloud.storage.object.v1.finalized" --trigger-event-filters="bucket=clean-ashmore-green"

