def match(status:int)->str:
    match status:
        case 200:
            return "ok"
        case 400:
            return "not found"
        case 600:
            return "Poor connection"
        case 700:
            return "403 error"
        case _:
            return "Unknown error"
        
print(match(200))
print(match(500))
    