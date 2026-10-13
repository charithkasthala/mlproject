import logging 
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
'''krish naik code '''
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)


'''basically the difference between the code is , above code is creating 
the logs directory and then creating the log file inside it and not printing
the log file path whereas the below code is creating the log file directly inside,
 whereas the below code is creating the log file directly inside
 the logs directory without creating a separate directory for each log file.'''

'''chatgpt code

# Create only the logs directory
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

'''

# Create the full log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
