import json

def json_response(action, out ,out1):
    global acceptActionUnique,acceptRequestResponse, finalListRequest, finalListResponse
    acceptRequestResponse, acceptActionUnique=out , out1
    openRequest=acceptRequestResponse[acceptActionUnique[action]][0].index('{')
    closeRequest=acceptRequestResponse[acceptActionUnique[action]][0].rindex('}')
    openResponse=acceptRequestResponse[acceptActionUnique[action]][1].index('{')
    closeResponse=acceptRequestResponse[acceptActionUnique[action]][1].rindex('}')
    finalListRequest=json.loads(acceptRequestResponse[acceptActionUnique[action]][0][openRequest:closeRequest+1])
    finalListResponse=json.loads(acceptRequestResponse[acceptActionUnique[action]][1][openResponse:closeResponse+1])
    data = { 
        'Request' : finalListRequest,
        'Response': finalListResponse
    }

    return json.dumps(data)
