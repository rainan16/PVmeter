import datetime
import logging
import requests

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    powerurl = "https://pvmeter.azurewebsites.net/api/get-power"
    requests.get(powerurl)

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
