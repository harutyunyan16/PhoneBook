# getting phone number when seperator not ':' or '-'
def getContact(txt):
    res = ''
    for el in txt[::-1]:
        if ord(el) in range(48, 58):
            res += el
            continue
        break

    return res[::-1]


# geting filter arguments from user
def getSortOrder():
    ascOrDesc = ''
    while True:
        ascOrDesc = input('Please choose an ordering to sort: Ascending(1) or Descending(2) : ')
        if ascOrDesc != '1' and ascOrDesc != '2':
            print(f'Please, input a valid value, `{ascOrDesc}` is invalid.')
            continue
        break

    criteria = ''
    while True:
        criteria = input('Please choose criteria: Name(1), Surname(2) or PhoneNumberCode(3) : ')
        if criteria != '1' and criteria != '2' and criteria != '3':
            print(f'Please, input a valid value, `{criteria} is invalid`.')
            continue
        break

    return (ascOrDesc, criteria)


# returned already filtered contacts objects list 
def getFilteredList(contacts, ascOrDesc, criteria):
    ascOrDesc = int(ascOrDesc)
    criteria = int(criteria)

    '''
        criteria = 1 and ascOrDesc = 1 - criteria is name and the filtering by increasing
        criteria = 1 and ascOrDesc = 2 - criteria is name and the filtering is decreasing

        criteria = 2 and ascOrDesc = 1 - criteria is surname and the filtering is decreasing
        criteria = 2 and ascOrDesc = 2 - criteria is surname and the filtering is decreasing

        criteria = 3 and ascOrDesc = 1 - criteria is phoneNumber and the filtering is decreasing
        criteria = 3 and ascOrDesc = 2 - criteria is phoneNumber and the filtering is decreasing
    '''


    if criteria == 1:
        start = []
        end = []
        for el in contacts:
            if len(el.name) == 0:
                end.append(el)
            else:   
                start.append(el)
        contacts = start
        iterSize = len(contacts)
        if ascOrDesc == 1:
            for i in range(iterSize):
                for j in range(i + 1, iterSize):
                    if contacts[i].name > contacts[j].name:
                        contacts[i], contacts[j] = contacts[j], contacts[i]
        else:
            for i in range(iterSize):
                for j in range(i + 1, iterSize):
                    if contacts[i].name < contacts[j].name:
                        contacts[i], contacts[j] = contacts[j], contacts[i]
        contacts += end
    elif criteria == 2:
        start = []
        end = []
        for el in contacts:
            if len(el.surname) == 0:
                end.append(el)
            else:   
                start.append(el)
        contacts = start
        iterSize = len(contacts)
        if ascOrDesc == 1:
            for i in range(iterSize):
                for j in range(i + 1, iterSize):
                    if contacts[i].surname > contacts[j].surname:
                        contacts[i], contacts[j] = contacts[j], contacts[i]
                        break
        else:
            for i in range(iterSize):
                if not contacts[i].surname:
                    continue
                for j in range(i + 1, iterSize):
                    if contacts[i].surname < contacts[j].surname:
                        contacts[i], contacts[j] = contacts[j], contacts[i]
        contacts += end
    else:
        iterSize = len(contacts)
        if ascOrDesc == 1:
            for i in range(iterSize):
                for j in range(i + 1, iterSize):
                    try:
                        if int(contacts[i].phoneNumber[:3]) > int(contacts[j].phoneNumber[:3]):
                            contacts[i], contacts[j] = contacts[j], contacts[i]
                    except:
                        continue
        else:
            for i in range(iterSize):
                if not contacts[i].surname:
                    continue
                for j in range(i + 1, iterSize):
                    try:
                        if int(contacts[i].phoneNumber[:3]) < int(contacts[j].phoneNumber[:3]):
                            contacts[i], contacts[j] = contacts[j], contacts[i]
                    except:
                        continue

    return contacts