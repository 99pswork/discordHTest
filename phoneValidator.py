from onlinesimru import GetFree, GetRent, GetProxy, GetUser, GetNumbers, Driver

def main():
    client = GetUser('ade127c7b242f2aec2d6d93c5464d520')
    balance = client.balance()
    print(balance)
    
    numbers = GetNumbers('ade127c7b242f2aec2d6d93c5464d520')
    
    tzid = numbers.get("service")
    
    mynum = numbers.stateOne(tzid)
    
    print(mynum['number'])
    
    input("Press Enter")
    code = numbers.wait_code(tzid)
    print(code)

main()
