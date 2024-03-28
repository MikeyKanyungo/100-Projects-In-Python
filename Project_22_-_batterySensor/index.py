import psutil 
from plyer import motification 
import time

while(True):
    battery = psutil.sensors_battery()
    percentage = battery.percent 

    motification.motify(
        title = "Battery Percentag",
        message = str(percentage) + "% Battery remaining",
        timeout=10
    )
    time.sleep(60 * 60)

    continue 