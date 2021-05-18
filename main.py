# import browserhistory as bh

# dict_obj = bh.get_browserhistory()

# print(dict_obj)
import os
import sqlite3
import shutil
from datetime import datetime

data_path = os.path.expanduser('~') + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
files = os.listdir(data_path)
history_db = os.path.join(data_path, 'history')
history_db_temp = os.path.join(data_path, 'historytemp')
shutil.copyfile(history_db,os.path.join(data_path,'historytemp'))

c = sqlite3.connect(history_db_temp)
cursor = c.cursor()
select_statement = """SELECT 
                            urls.title, urls.url,
                            datetime(urls.last_visit_time / 1000000 + (strftime('%s', '1601-01-01')), 'unixepoch', 'localtime') 
                      FROM urls, visits 
                      WHERE urls.id = visits.url
                            and urls.url like '%meet.google%';"""

cursor.execute(select_statement)

results = cursor.fetchall()     

horario=results[0][2]

horario2=datetime.strptime(horario, '%Y-%m-%d %H:%M:%S')
agora=datetime.now())

tempo_meet_acessado=(agora - horario2).total_seconds() / 60.0

if tempo_meet_acessado>15:
    EnviarMensagemWpp()

def EnviarMensagemWpp():
    
    pass    