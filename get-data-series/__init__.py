import logging

import azure.functions as func
import json

def main(req: func.HttpRequest, cosmositems: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    if not cosmositems:
        return func.HttpResponse("nothing found")
    else:
        res = []
        for val in cosmositems:
            v = {}
            v['timestamp'] = val['timestamp']
            v['power'] = val['power']
            res.append(v)
            
        return func.HttpResponse(json.dumps(res), mimetype='text/json')