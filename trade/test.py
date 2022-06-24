from operator import mul
import pyautogui
import MetaTrader5 as mt
import trade
import psql

# list = ['CHFJPY', 'SELL', '136.35', 'TP', '136.15',
#         'TP', '135.85', 'TP', '135.35', 'SL', '137.85']

# psql.save_order(41201381, list)

print(mt.positions_get())

# request = {
#     'action': mt.TRADE_ACTION_SLTP,
#     'position': 9451540,
#     'tp': float(0.834),
# }

# result = mt.order_send(request)
# print(result)

# try:
#     if(len(list[0]) == 6 and (len(list[1]) == 3 or len(list[1]) == 4) and float(list[2]) and len(list[3]) == 2 and float(list[4]) and len(list[5]) == 2 and float(list[6]) and len(list[7]) == 2 and float(list[8]) and len(list[9]) == 2 and float(list[10]) ):
#         order = trade.trade(list)


#     else:
#         print("false")
# except Exception as err:
#     print("not valid ",err)


"""
"""

var = "Gold sell now @ 1831.60 TP:1833.10/1834.60/1837.60 asdfd SI: 1826.60 © 9527 edited 5:03 A"
varray = ["XAUUSD"]
varType = var.find("Gold") + 5
varTP = var.find("TP") + 3
varSL = var.find("SI") + 4
varCur = var.find("@") + 2
valueType = var[varType:varType+4].replace(" ","")
valueSL = var[varSL:varSL+7]
varTParray = var[varTP:varTP+23].replace("/", " ").split()
valueCur = var[varCur:varCur+7]

varray.append(valueType)
varray.append(valueCur)
varray.extend(varTParray)
varray.append(valueSL)
varray.insert(3,"TP")
varray.insert(5,"TP")
varray.insert(7,"TP")
varray.insert(9,"SL")


print(varray)
print(valueCur)