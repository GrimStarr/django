from asyncio.windows_events import NULL
from telethon import TelegramClient, events, sync
import trade
import tele
import time
import pyautogui
import psql
import dchat

# Remember to use your own values from my.telegram.org!
api_id = 17856666
api_hash = '139ee5db22e1758937cd314ac05d7390'
client = TelegramClient('anon', api_id, api_hash)


@client.on(events.NewMessage)
async def my_event_handler(event):
    pyautogui.click(790, 950)
    pyautogui.press('enter')
    time.sleep(2)
    tel_event = tele.screenshot()
    str1 = " "
    var = str1.join(tel_event)
    msg = "null"
    print(tel_event)
    try:
        if(len(tel_event[0]) == 6 and (len(tel_event[1]) == 3 or len(tel_event[1]) == 4) and float(tel_event[2]) and len(tel_event[3]) == 2 and float(tel_event[4]) and len(tel_event[5]) == 2 and float(tel_event[6]) and len(tel_event[7]) == 2 and float(tel_event[8]) and len(tel_event[9]) == 2 and float(tel_event[10])):
            order = trade.trade(tel_event)
            msg = "order is null"
            if(order != None and order != 0):
                psql.save_order(order, tel_event)
                msg = "trade success"
        else:
            
            print("okey not buy signal")
            msg = "not buy signal "
    except Exception as err:

        print("not buy, err: ", err)
       
    if tel_event[1] == "buy" or tel_event[1] == "sell":
        dchat.send_discord(var)
        
        dchat.send_discord(msg)
    # await client.send_file("Test", 'telegram.png')
    # await client.send_file("Test", 'telegram2.png')
    # await client.send_message("Test", var)
    # await client.send_message("Test", msg)

print("starting . . .")
client.start()
client.run_until_disconnected()
