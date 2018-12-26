import json

def write_order2json(item,quantity,price,buyer,date):
    with open('orders.json', 'r') as f_n:
        obj_json = json.load(f_n)

    obj_json['orders'] = {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}
    dict = obj_json.values()


    obj_json['orders'] = {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}
    print(obj_json)

    #print(obj_json)

    with open('orders.json', 'w') as f_n:
        json.dump(obj_json,f_n)

    return 0

write_order2json(1,2,30,'fff',444)
