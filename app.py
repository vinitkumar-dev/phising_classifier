from src.exception import CustomEXception
import sys

try:
    a = 10/0

except Exception as e:
    raise CustomEXception(e,sys)