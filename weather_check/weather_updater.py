from apscheduler.schedulers.background import BackgroundScheduler
from .alert import check_conditions


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_conditions, 'interval', minutes=1)
    scheduler.start()
