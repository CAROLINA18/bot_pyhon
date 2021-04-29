from bs4 import BeautifulSoup
import requests
import schedule

def bot_send_text(bot_message):
    
    bot_token = '1748277961:AAEURksLU6ZO0rFpjvSz8qABFVXJA4as7vc'
    bot_chatID = '1258060322'
    bot_idivan = '1541466528'
    bot_idbran = '1661690591'
    send_text = 'https://api.telegram.org/bot'+ bot_token + '/sendPhoto  chat_id=' + bot_chatID + 'photo=' + bot_message
                
    #response = requests.post(send_text)
    response = requests.post('https://api.telegram.org/bot1748277961:AAEURksLU6ZO0rFpjvSz8qABFVXJA4as7vc/sendPhoto',
              data={'chat_id': bot_idbran, 'photo': bot_message, 'caption': 'prueba'})

    return response

test_bot = bot_send_text('https://pbs.twimg.com/media/D1GAuPpX0AE1dBw.jpg')