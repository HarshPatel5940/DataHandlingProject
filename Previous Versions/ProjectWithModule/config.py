import logging

app_data_path = "data/"
user_file_path = "data_user.csv"
admin_file_path = "data_admin.csv"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')

file_handler = logging.FileHandler('Audit.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
