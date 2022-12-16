# -*- coding: utf-8 -*-
import re

def is_currency(money):
    regex = r"^\d+(\.\d{2})?€"
    match = re.search(regex, money)
    if match: return True
    return False