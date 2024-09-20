import schedule
import time
from wecom_rss.rss_handler import run_rss_checker

# 定时任务：每1分钟检查一次 RSS 更新
schedule.every(1).minutes.do(run_rss_checker)

def main():
    print("WeCom RSS bot is running...")
    while True:
        schedule.run_pending()
        time.sleep(1)
