from datetime import datetime
now = datetime.today().strftime('%d%m%y_%H%M')


ANIMEHEAVEN_ABUSE_MSG = 'You have triggered abuse protection'
BLOCKED_TIMEOUT = 120
DEFAULT_DOWNLOAD_PATH = f'{now} downloads'
LOG_PATH = 'logs'
