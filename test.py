from modules import convert_to_dict
brewery_list = convert_to_dict("brewapp/b.csv")

def index():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list[:100]:
        logo_list.append(brewery['url'])
        name_list.append(brewery['brewery'])
        type_list.append(brewery['type'])
        address_list.append(brewery['address'])
        city_list.append(brewery['city'])
    info_list = zip(logo_list, name_list, type_list, address_list, city_list)
    for info in info_list:
        if ' AL' in list(info_list[4]):
            return k
        else:
            print("no")
index()
