import schedule, time,subprocess,os
from colorama import Fore
from colorama import Style

def job():
    print(f"{Fore.BLUE}Job is running to clean the staging area after decided configured time")
    #subprocess.call("sudo ./CronJob.py -h", shell=True)
    print(f"{Fore.GREEN}")
    os.system("python3 ./CronJob.py /home/esyekas/test f +10")
    print(f"{Style.RESET_ALL}")

#schedule.every(5).seconds.do(job)
#schedule.every(10).minutes.do(job)
schedule.every(1).hour.do(job)
#schedule.every().day.at("10:37").do(job)
#schedule.every(5).to(10).days.do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(2)