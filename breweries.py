from flask import Flask, render_template
from modules import convert_to_dict

app = Flask(__name__)

brewery_list = convert_to_dict("b.csv")


@app.route('/')
def index():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' FL ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Florida")
# your code here

@app.route('/AL')
def AL():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' AL ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Alabama")

@app.route('/AK')
def AK():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' AK ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Alaska")

@app.route('/AZ')
def AZ():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' AZ ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Arizona")

@app.route('/AR')
def AR():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' AR ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Arkansas")


@app.route('/CA')
def CA():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' CA ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="California")

@app.route('/CO')
def CO():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' CO ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Colorado")

@app.route('/CT')
def CT():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' CT ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Connecticut")

@app.route('/DE')
def DE():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' DE ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Delaware")

@app.route('/FL')
def FL():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' FL ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Florida")

@app.route('/GA')
def GA():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' GA ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Georgia")

@app.route('/HI')
def HI():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' HI ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Hawaii")

@app.route('/ID')
def ID():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' ID ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Idaho")

@app.route('/IL')
def IL():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' IL ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Illinois")

@app.route('/IN')
def IN():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' IN ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Indiana")

@app.route('/IA')
def IA():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' IA ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Iowa")

@app.route('/KS')
def KS():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' KS ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Kansas")

@app.route('/KY')
def KY():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' KY ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Kentucky")

@app.route('/LA')
def LA():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' LA ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Louisiana")

@app.route('/ME')
def ME():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' ME ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Maine")

@app.route('/MD')
def MD():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' MD ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Maryland")

@app.route('/MA')
def MA():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' MA ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Massachusetts")

@app.route('/MI')
def MI():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' MI ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Michigan")

@app.route('/MN')
def MN():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' MN ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Minnesota")

@app.route('/MS')
def MS():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' MS ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Mississippi")

@app.route('/MO')
def MO():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' MO ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Missouri")

@app.route('/MT')
def MT():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' MT ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Montana")

@app.route('/NE')
def NE():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' NE ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Nebraska")

@app.route('/NV')
def NV():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' NV ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Nevada")

@app.route('/NH')
def NH():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' NH ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="New Hampshire")

@app.route('/NJ')
def NJ():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' NJ ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="New Jersey")

@app.route('/NM')
def NM():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' NM ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="New Mexico")

@app.route('/NY')
def NY():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' NY ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="New York")

@app.route('/NC')
def NC():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' NC ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="North Carolina")

@app.route('/ND')
def ND():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' ND ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="North Dakota")

@app.route('/OH')
def OH():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' OH ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Ohio")

@app.route('/OK')
def OK():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' OK ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Oklahoma")

@app.route('/OR')
def OR():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' OR ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Oregon")

@app.route('/PA')
def PA():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' PA ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Pennsylvania")

@app.route('/RI')
def RI():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' RI ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Rhode Island")

@app.route('/SC')
def SC():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' SC ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="South Carolina")

@app.route('/SD')
def SD():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' SD ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="South Dakota")

@app.route('/TN')
def TN():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' TN ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Tennessee")

@app.route('/TX')
def TX():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' TX ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Texas")

@app.route('/UT')
def UT():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' UT ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Utah")

@app.route('/VT')
def VT():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' VT ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Vermont")

@app.route('/VA')
def VA():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' VA ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Virginia")

@app.route('/WA')
def WA():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' WA ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Washington")

@app.route('/WV')
def WV():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' WV ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="West Virginia")

@app.route('/WI')
def WI():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' WI ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Wisconsin")

@app.route('/WY')
def WY():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' WY ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="Wyoming")

@app.route('/DC')
def DC():
    logo_list = []
    name_list = []
    type_list = []
    address_list = []
    city_list = []
    for brewery in brewery_list:
        if ' DC ' in brewery['city']:
            logo_list.append(brewery['url'])
            name_list.append(brewery['brewery'])
            type_list.append(brewery['type'])
            city_list.append(brewery['city'])
            address_list.append(brewery['address'])
        else:
            pass
    info_list = zip(logo_list, name_list, type_list, address_list,city_list)
    return render_template('index.html', infos=info_list, title="D.C.")

# keep this as is
if __name__ == '__main__':
    app.run(debug=True)
