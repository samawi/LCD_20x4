import lcddriver
import time
import subprocess

lcd = lcddriver.lcd()

# lcd.lcd_display_string("antisteo on YT", 1)
# lcd.lcd_display_string("LCD runtime is", 2)
# lcd.lcd_display_string("picorder", 3)
# lcd.lcd_display_string("connect me via I2C", 4)

# for i in range(1,100):
#     lcd.lcd_display_string(str(i), 3, 1)
#     sleep (1)

while True:
    # cmd = "hostname -I | cut -d\' \' -f1"
    cmd = "hostname -I |cut -f 1 -d ' '"
    IP = subprocess.check_output(cmd, shell=True)
    # print(str(IP,'utf-8'))
    cmd = "top -bn1 | grep load | awk '{printf \"C: %.2f\", $(NF-2)}'"
    CPU = subprocess.check_output(cmd, shell = True )
    # print(str(CPU,'utf-8'))
    cmd = "free -m | awk 'NR==2{printf \"M: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
    MemUsage = subprocess.check_output(cmd, shell = True )
    # print(str(MemUsage,'utf-8'))

    cmd = "df -h | awk '$NF==\"/\"{printf \"D: %d/%dGB %s\", $3,$2,$5}'"
    Disk = subprocess.check_output(cmd, shell = True )
    # print(str(Disk,'utf-8'))

    cmd = "vcgencmd measure_temp |cut -f 2 -d '='"
    temp = subprocess.check_output(cmd, shell = True )
    # print(str(temp,'utf-8'))



    lcd.lcd_display_string("I: "+str(IP,'utf-8'), 1)
    lcd.lcd_display_string(str(CPU,'utf-8')+" "+str(temp,'utf-8'), 2)
    lcd.lcd_display_string(str(MemUsage,'utf-8'), 3)
    lcd.lcd_display_string(str(Disk,'utf-8'), 4)

    time.sleep(1)