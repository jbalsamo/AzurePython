import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    num = req.params.get('number')
    exp = req.params.get('exponent')
    if not (num and exp):
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            num = req_body.get('number')
            exp = req_body.get('exponent')
            value = num**exp;

    if value:
        return func.HttpResponse("Answer: {value}")
    else:
        return func.HttpResponse(
             "Please pass a number and exponent on the query string or in the request body",
             status_code=400
        )
