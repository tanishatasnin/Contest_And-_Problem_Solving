

# try, timeout, raise_for_status(), response.json(), and  except
 # -------------------------------------------------------------------
# Error	কখন হয়?
# Timeout	Request-এর response পেতে বেশি সময় লাগলে
# ConnectionError	Network connection ব্যর্থ হলে
# HTTPError	HTTP status error হলে
# RequestException	অন্যান্য request-related error হলে
# JSONDecodeError	JSON decode করতে ব্যর্থ হলে
# FileNotFoundError	File পাওয়া না গেলে
# PermissionError	প্রয়োজনীয় permission না থাকলে
# ZeroDivisionError	শূন্য দিয়ে ভাগ করলে
# ValueError	সঠিক type হলেও value গ্রহণযোগ্য না হলে
# TypeError	ভুল type-এর operation করলে
# KeyError	Dictionary key না থাকলে
# IndexError	-List বা sequence-এর index না থাকলে
# AttributeError	Object-এ চাওয়া attribute না থাকলে
# NameError	Variable বা name খুঁজে না পেলে
# ImportError	Import করতে সমস্যা হলে
# OverflowError	কোনো operation-এর ফল represent করা না গেলে
# RuntimeError	অন্য কোনো নির্দিষ্ট শ্রেণিতে না পড়া runtime সমস্যা হলে
# MemoryError	পর্যাপ্ত memory না থাকলে
# Exception	অন্য unhandled সাধারণ exception
# ---
# try — যে code-এ error হতে পারে, সেটি রাখবে।
# except requests.exceptions.ConnectionError — Internet বা server connection failure handle করবে।
# except requests.exceptions.Timeout — Request-এর response পেতে বেশি সময় লাগলে handle করবে।
# timeout=10 — Request অনির্দিষ্টকাল অপেক্ষা করা থেকে বিরত রাখতে ব্যবহার করবে।
# response.raise_for_status() — HTTP error status, যেমন 404 বা 500, হলে exception তৈরি করবে।
# except requests.exceptions.HTTPError — HTTP status error handle করবে।
# response.json() — JSON response-কে Python data-তে convert করবে।
# except requests.exceptions.JSONDecodeError — Response invalid JSON হলে handle করবে।
# except requests.exceptions.RequestException as e — অন্যান্য request-related error-এর জন্য general fallback হিসেবে ব্যবহার করবে।
# as e — Error-এর message e variable-এ রাখবে; print(e) দিয়ে message দেখতে পারবে।

# 1. example 

import requests
try:
    response = requests.get("https://api.example.com/users")
    response.raise_for_status()
    data = response.json()
    for user in data:
        print(user["name"])
except requests.exceptions.RequestException as e:  
    print("Request failed!")
    print(e)