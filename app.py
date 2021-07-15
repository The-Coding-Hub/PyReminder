import pandas as pd
from datetime import datetime
import time
from plyer import notification
from playsound import playsound

df = pd.read_csv('data_main.csv')

times = list(df['Timing'])

titles = list(df['Task'])

dict = {}
i = 0
while i <= (len(titles)-1):
  dict[times[i]] = titles[i]
  i += 1

while True:
  time_now = datetime.now().strftime("%H:%M")
  for item in times:
    if item == time_now:
      notification.notify(
        title = dict[item],
        message = f"Reminder for the Task '{dict[item]}'...",
        app_icon = "D:\\Programming\\5 Python Projects\\P3. Reminder Application\\icon.ico",
        timeout = 10
      )
      playsound("D:\\Programming\\5 Python Projects\\P3. Reminder Application\\alarm.mp3")

      time.sleep(60)
