import re

def match_floors(address1, address2):
    #Tuned for the case of hk employment agencies only at the moment

    def find_floor_number(address_component, prefix):
        #To be expanded later, but if we are only looking at employment agencies
        #then this is sufficient
        if "ground" in address_component:
            return 'g'

        if 'podium' in address_component:
            return 'p'

        if 'basement' in address_component:
            return 'b'

        elif "floor" in address_component:
            try:
                return int(re.sub('[^0-9]', '', address_component))
            except:
                print address_component
                return -1
        elif prefix == '/f':
            if 'g' in address_component:
                return 'g'
            if 'b' in address_component:
                return 'b'
            if 'p' in address_component:
                return 'p'
            else:
                try:
                    floor = int(re.sub('[^0-9]', '', address_component))
                    if floor > 100:
                        floor = floor % 100
                    return floor
                except:
                    print address_component
                    return -1
        else:
            return -1


    address1, address2 = address1.lower(), address2.lower()
    found1, found2 = False, False
    prefix1, prefix2 = None, None
    floor_prefixes = ['lvl', 'level', 'floor', '/f']
    segment1=''
    segment2=''

    for component1 in address1.split(','):
        if found1: break
        for prefix in floor_prefixes:
            if prefix in component1:
                prefix1 = prefix
                found1 = True
                segment1=component1

    for component2 in address2.split(','):
        if found2: break
        for prefix in floor_prefixes:
            if prefix in component2:
                prefix2 = prefix
                found2 = True
                segment2=component2


    if not found1 and not found2:
        return True

    if (not found1 and found2) or (found1 and not found2):
        return False

    floor1 = find_floor_number(segment1, prefix1)
    floor2 = find_floor_number(segment2, prefix2)

    return floor1==floor2


    vals= {0:'', 1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten', 20:'Twenty', 30:'Thirty', 40:'Forty',
            50:'Fifty', 60:'Sixty', 70:'Seventy', 80:'Eighty', 90:'Ninety'}
