import logging

import azure.functions as func

from getpower import load_current_value

async def main(req: func.HttpRequest, cosmos: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    val = await load_current_value()
    cosmos.set(func.Document.from_json(val))

    return func.HttpResponse(val, mimetype='text/json')

