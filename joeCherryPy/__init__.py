import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    num = int(req.params.get('number'))
    exp = int(req.params.get('exponent'))
    value = 0
    if not (num and exp):
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            num = int(req_body.get('number'))
            exp = int(req_body.get('exponent'))
            value = num**exp;
    else:
        value = num**exp

    if value:
        return func.HttpResponse(f"Answer: {value}")
    else:
        return func.HttpResponse(
             "Please pass a number and exponent on the query string or in the request body",
             status_code=400
        )
