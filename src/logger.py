# In your main script or module

from logger import setup_logger, log_info, log_warning, log_error, log_exception
from exception import MLProjectException, raise_custom_exception

# Set up the logger
setup_logger()

try:
    # Your ML project code here
    log_info('ML project started')

    # ... rest of your code ...

    log_info('ML project completed successfully')

except MLProjectException as ex:
    log_error(f'Custom exception: {str(ex)}')
    # Handle the exception as needed

except Exception as ex:
    log_exception(ex, 'An unexpected exception occurred')
    # Handle the exception as needed

# ... rest of your code ...
