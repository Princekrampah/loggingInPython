from decimal import DivisionByZero
import logging

# logging exception


try:
    5 / 0
except ZeroDivisionError as dbze:
    logging.error("Division by zero exception...", exc_info=True)
    logging.exception("Division by zero exception...")
    
