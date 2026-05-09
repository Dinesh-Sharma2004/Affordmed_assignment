def success_response(message):
    return {"success":True,"message":message}

def error_response(message):
    return {"success":False,"message":message}