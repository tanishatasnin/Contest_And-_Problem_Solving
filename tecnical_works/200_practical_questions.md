# 200 Practical Questions for Technical Support Engineer

## Instructions
- Questions are numbered 1–200, ordered from easy to hard within each section.
- Each question includes context, task, and Windows-compatible steps where applicable.
- Solutions are intentionally omitted — practice solving them yourself.
- Tools referenced: VS Code, Postman, MySQL Command Line / MySQL Workbench.

---

## Section 1: API and Postman (Questions 1–40)

### Easy (1–15)

**1.** What HTTP status code indicates a successful GET request? What does 404 mean?

**2.** In Postman, how do you send a simple GET request to `https://jsonplaceholder.typicode.com/users`? List the steps.

**3.** What is the difference between a query parameter and a path parameter? Give one example of each.

**4.** In Postman, where do you add headers to a request? Add a header `Content-Type: application/json` to a POST request.

**5.** What does the HTTP method POST do? How is it different from PUT?

**6.** A customer says their API call returns `401 Unauthorized`. What are three possible causes?

**7.** In Postman, how do you save a request to a collection? List the steps.

**8.** What is a JSON body? Write a minimal JSON body for creating a user with fields `name` and `email`.

**9.** In Postman, how do you view the response time and response size of a request?

**10.** What is the purpose of the `Accept` header in an HTTP request?

**11.** A GET request to `/api/products?category=electronics&limit=10` — what are the query parameters and their values?

**12.** In Postman, how do you create a new environment variable? Set a variable `baseUrl` to `https://api.example.com`.

**13.** What does HTTP status code `400 Bad Request` indicate? Give a common cause.

**14.** In Postman, how do you import a cURL command? List the steps.

**15.** What is the difference between `200 OK` and `201 Created`?

### Medium (16–30)

**16.** You have a Postman collection with 10 requests. How do you run all of them sequentially using the Collection Runner? List the steps.

**17.** A customer's API returns `500 Internal Server Error`. What are the first three things you would check?

**18.** In Postman, write a pre-request script that sets a variable `timestamp` to the current Unix epoch time.

**19.** What is an API endpoint? Given `https://api.example.com/v2/orders/123`, identify the base URL, version, resource, and resource ID.

**20.** In Postman, how do you extract a value from a JSON response and use it in the next request? Use `id` from the response of Request A as a path parameter in Request B.

**21.** What is the difference between authentication and authorization? Give an API example of each.

**22.** A customer sends a POST request with a JSON body but gets `415 Unsupported Media Type`. What is the likely cause and fix?

**23.** In Postman, how do you write a test that checks if the response status code is 200? Write the test script.

**24.** What is pagination in an API? Given a response with `page`, `limit`, and `total` fields, how would you fetch all records?

**25.** In Postman, how do you use environment variables in a request URL? Show an example using `{{baseUrl}}/users`.

**26.** A customer reports that their API response is slow (takes 10+ seconds). What are five possible causes you would investigate?

**27.** What is idempotency? Which HTTP methods are idempotent? Why does it matter for retries?

**28.** In Postman, how do you set up Basic Authentication for a request? List the steps.

**29.** A customer's API call works in Postman but fails in their application. What are four possible reasons?

**30.** In Postman, how do you generate a random value (e.g., random email) for each request iteration? Use dynamic variables.

### Hard (31–40)

**31.** Design a Postman collection for a simple e-commerce API with endpoints: create product, get product, update product, delete product. Include tests for each. Describe the collection structure.

**32.** A customer reports intermittent `502 Bad Gateway` errors. Walk through your troubleshooting process step by step.

**33.** In Postman, write a test script that validates the response JSON schema — check that `id` is a number, `name` is a string, and `email` contains `@`.

**34.** Explain CORS. A customer gets a CORS error when calling your API from a browser. What is the likely cause and how do you fix it?

**35.** In Postman, how do you chain three requests where each depends on the previous response? Describe the full workflow using environment variables.

**36.** A customer needs to upload a file via API using `multipart/form-data`. How do you configure this in Postman? List the steps.

**37.** What is rate limiting? A customer gets `429 Too Many Requests`. Explain what this means and three strategies to handle it.

**38.** In Postman, how do you mock an API server? Create a mock for `GET /api/users` that returns a list of 3 users. List the steps.

**39.** A customer's OAuth 2.0 token keeps expiring. Explain the token refresh flow. How would you configure token refresh in Postman?

**40.** You discover an API endpoint returns sensitive data (passwords) in the response. What security issue is this, and what are the steps to fix it?

---

## Section 2: SQL and MySQL (Questions 41–80)

### Easy (41–55)

**41.** What SQL command retrieves all columns from a table called `customers`?

**42.** What is the difference between `WHERE` and `HAVING`?

**43.** Write a SQL query to select all customers from the `customers` table where `city` is 'New York'.

**44.** What does the `INSERT INTO` statement do? Write a query to insert a new row into a `products` table with columns `name` and `price`.

**45.** What is a primary key? Can a primary key be NULL?

**46.** Write a SQL query to update the `email` column for a customer with `id = 5`.

**47.** What does `DELETE FROM customers WHERE id = 10` do? What happens if you omit the `WHERE` clause?

**48.** What is the difference between `INNER JOIN` and `LEFT JOIN`?

**49.** Write a SQL query to count the number of rows in the `orders` table.

**50.** What does the `ORDER BY` clause do? Write a query to sort products by `price` in descending order.

**51.** What is the `LIKE` operator? Write a query to find all customers whose name starts with 'A'.

**52.** What is the difference between `COUNT(*)` and `COUNT(column_name)`?

**53.** Write a SQL query to select distinct values from the `country` column in the `customers` table.

**54.** What does the `LIMIT` clause do? Write a query to get the first 10 rows from a `logs` table.

**55.** On Windows, how do you open MySQL Command Line Client and connect to a database? List the steps.

### Medium (56–70)

**56.** Write a SQL query to join `orders` and `customers` tables to get order IDs with customer names.

**57.** What is a foreign key? How does it enforce referential integrity?

**58.** Write a SQL query to find the total sales amount per customer using `orders` and `order_items` tables.

**59.** What is the difference between `UNION` and `UNION ALL`?

**60.** Write a SQL query to find customers who have not placed any orders (use `LEFT JOIN` and `IS NULL`).

**61.** What is an index? Write a SQL statement to create an index on the `email` column of the `customers` table.

**62.** Write a SQL query to find the second highest salary from an `employees` table.

**63.** What is a `GROUP BY` clause? Write a query to count orders per status from an `orders` table.

**64.** On Windows, how do you create a new MySQL database using MySQL Workbench? List the steps.

**65.** Write a SQL query to delete duplicate rows from a `users` table (keep one copy of each duplicate based on `email`).

**66.** What is a `CASE` statement? Write a query to categorize products as 'Expensive' or 'Cheap' based on price > 100.

**67.** Write a SQL query to find all orders placed in the last 7 days.

**68.** What is the difference between `CHAR` and `VARCHAR`?

**69.** On Windows, how do you export a MySQL table to a CSV file using MySQL Workbench? List the steps.

**70.** Write a SQL query to calculate the average order value per month for the current year.

### Hard (71–80)

**71.** Write a SQL query to find the top 3 customers by total spending. Use `orders` and `order_items` tables.

**72.** What is a transaction? Write a SQL transaction that transfers money between two accounts. Include rollback on error.

**73.** Explain the difference between `TRUNCATE`, `DELETE`, and `DROP`.

**74.** Write a SQL query to find consecutive login streaks for users from a `user_logins` table (columns: `user_id`, `login_date`).

**75.** What is a subquery? Write a query to find employees whose salary is above the average salary.

**76.** On Windows, how do you set up a MySQL user with read-only access to a specific database? List the steps using MySQL Workbench or command line.

**77.** Write a SQL query to pivot rows into columns — transform `sales` data (columns: `product`, `quarter`, `amount`) so each product has columns Q1, Q2, Q3, Q4.

**78.** What is a deadlock in MySQL? How would you detect and resolve it?

**79.** Write a recursive CTE query to find all subordinates of a manager in an `employees` table (columns: `id`, `name`, `manager_id`).

**80.** A customer reports their MySQL query is slow. Walk through your optimization process: how do you identify the slow query, analyze it, and fix it?

---

## Section 3: Python Debugging with Buggy Code (Questions 81–120)

### Easy (81–95)

**81.** Find the bug:
```python
def greet(name)
    print("Hello, " + name)
```
What is wrong and how do you fix it?

**82.** Find the bug:
```python
numbers = [1, 2, 3, 4, 5]
print(numbers[5])
```
What error occurs and why?

**83.** Find the bug:
```python
x = 10
if x = 10:
    print("x is 10")
```
What is wrong and how do you fix it?

**84.** Find the bug:
```python
def add(a, b):
    return a - b

result = add(5, 3)
print(result)
```
What is the logical error?

**85.** Find the bug:
```python
my_list = [1, 2, 3]
for i in range(len(my_list)):
    print(my_list[i])
    my_list.append(i)
```
What problem does this code cause?

**86.** Find the bug:
```python
age = input("Enter your age: ")
if age >= 18:
    print("Adult")
```
What error occurs and how do you fix it?

**87.** Find the bug:
```python
def divide(a, b):
    return a / b

print(divide(10, 0))
```
What error occurs and how would you handle it?

**88.** Find the bug:
```python
text = "Hello World"
print(text[10])
```
What error occurs and why?

**89.** Find the bug:
```python
my_dict = {"name": "Alice", "age": 25}
print(my_dict["email"])
```
What error occurs and how do you fix it?

**90.** Find the bug:
```python
import math

result = math.sqrt(-1)
print(result)
```
What error occurs and how would you handle it?

**91.** Find the bug:
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n)

print(factorial(5))
```
What problem does this code cause?

**92.** Find the bug:
```python
x = 5
y = "10"
print(x + y)
```
What error occurs and how do you fix it?

**93.** Find the bug:
```python
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers
    total += num
print(total)
```
What is wrong and how do you fix it?

**94.** Find the bug:
```python
def is_even(n):
    if n % 2 = 0:
        return True
    else:
        return False
```
What is wrong and how do you fix it?

**95.** Find the bug:
```python
file = open("data.txt", "r")
content = file.read()
print(content)
```
What is the potential issue and how do you fix it?

### Medium (96–110)

**96.** Find the bug:
```python
def append_to_list(item, my_list=[]):
    my_list.append(item)
    return my_list

print(append_to_list(1))
print(append_to_list(2))
```
What is the unexpected behavior and how do you fix it?

**97.** Find the bug:
```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance

account = BankAccount(100)
print(account.withdraw(150))
print(account.balance)
```
What is the logical error?

**98.** Find the bug:
```python
import json

data = '{"name": "Alice", "age": 25}'
parsed = json.loads(data)
print(parsed["name"])
print(parsed["email"])
```
What error occurs and how do you handle it?

**99.** Find the bug:
```python
def get_average(numbers):
    if not numbers:
        return 0 
    else
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

print(get_average([]))
```
What error occurs and how do you fix it?

**100.** Find the bug:
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
    result = None
finally:
    print("Result is: " + result)
```
What error occurs and how do you fix it?

**101.** Find the bug:
```python
def process_data(data):
    result = []
    for item in data:
        if item > 0:
            result.append(item * 2)
    return result

numbers = [1, -2, 3, -4, 5]
result = process_data(numbers)
print(len(result))
```
What error occurs and why?

**102.** Find the bug:
```python
import requests

response = requests.get("https://api.example.com/users")
data = response.json()
for user in data:
    print(user.get("name"))
```
What could go wrong? Add proper error handling.

**103.** Find the bug:
```python
def find_duplicates(lst):
    duplicates = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] == lst[j]:
                duplicates.append(lst[i])
    return duplicates

print(find_duplicates([1, 2, 3, 2, 4, 3]))
```
What is the logical error and how do you fix it?

**104.** Find the bug:
```python
my_tuple = (1, 2, 3)
my_tuple[0] = 10
print(my_tuple)
```
What error occurs and why?

**105.** Find the bug:
```python
def countdown(n):
    while n > 0:
        print(n)
        n = n - 1

countdown(5)
print("Done!")
```
What is the issue with this code? (Hint: think about what happens with negative input)

**106.** Find the bug:
```python
text = "hello world"
print(text.upper())
print(text)
```
What is the unexpected behavior and how do you fix it?

**107.** Find the bug:
```python
def merge_lists(list1, list2):
    return list1 + list2

a = [1, 2, 3]
b = [4, 5, 6]
c = merge_lists(a, b)
a.append(7)
print(c)
```
What is the unexpected behavior?

**108.** Find the bug:
```python
import os

files = os.listdir(".")
for file in files:
    if file.endswith(".txt"):
        os.remove(file)
        print(f"Deleted {file}")
```
What is the potential danger and how do you make it safer?

**109.** Find the bug:
```python
def validate_password(password):
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    return True

print(validate_password("Password1"))
print(validate_password("password1"))
print(validate_password("PASSWORD1"))
print(validate_password("Password"))
```
What is missing from this validation?

**110.** Find the bug:
```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

stack = Stack()
print(stack.pop())
```
What error occurs and how do you handle it?

### Hard (111–120)

**111.** Find the bug:
```python
import threading

counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1

threads = []
for _ in range(10):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(counter)
```
What is the issue and how do you fix it?

**112.** Find the bug:
```python
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(100))
```
What is the problem and how do you fix it?

**113.** Find the bug:
```python
import json

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_json(self):
        return json.dumps(self)

user = User("Alice", 25)
print(user.to_json())
```
What error occurs and how do you fix it?

**114.** Find the bug:
```python
def read_file_lines(filename):
    lines = []
    with open(filename, "r") as f:
        for line in f:
            lines.append(line)
    return lines

def process_lines(lines):
    results = []
    for line in lines:
        results.append(line.strip().upper())
    return results

lines = read_file_lines("data.txt")
processed = process_lines(lines)
print(processed[100])
```
What could go wrong? Add proper error handling.

**115.** Find the bug:
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove(self, value):
        current = self.head
        if current.value == value:
            self.head = current.next
            return
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.remove(1)
```
What error occurs and how do you fix it?

**116.** Find the bug:
```python
import re

def extract_emails(text):
    pattern = r"[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+"
    return re.findall(pattern, text)

text = "Contact us at support@example.com or sales@company.org"
emails = extract_emails(text)
print(emails)
```
What is the issue with the regex pattern? How do you improve it?

**117.** Find the bug:
```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(arr, 7))
print(binary_search(arr, 10))
```
What is the potential issue with this implementation? (Hint: think about very large arrays)

**118.** Find the bug:
```python
import sqlite3

def get_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return result

print(get_user(1))
print(get_user("1 OR 1=1"))
```
What is the critical security issue and how do you fix it?

**119.** Find the bug:
```python
def retry(func, max_retries=3):
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
    raise Exception("All retries failed")

def unstable_operation():
    import random
    if random.random() < 0.7:
        raise ValueError("Random failure")
    return "Success"

result = retry(unstable_operation)
print(result)
```
What is the issue with this retry logic? How do you improve it?

**120.** Find the bug:
```python
import asyncio

async def fetch_data(url):
    await asyncio.sleep(1)
    return f"Data from {url}"

async def main():
    urls = ["url1", "url2", "url3", "url4", "url5"]
    results = []
    for url in urls:
        result = await fetch_data(url)
        results.append(result)
    return results

asyncio.run(main())
```
What is the performance issue and how do you fix it?

---

## Section 4: Troubleshooting and Root Cause (Questions 121–150)

### Easy (121–130)

**121.** A customer reports the website is not loading. 
What are the first five things you check?

**122.** A customer says "the API is down." What questions do you ask to narrow down the issue?

**123.** A customer reports their application crashes on startup. What are the first three things you investigate?

**124.** What is the difference between troubleshooting and root cause analysis?

**125.** A customer reports slow page load times. What are four possible causes?

**126.** A customer says their data is missing. What are the first steps you take?

**127.** What is a log file? Where would you find application logs on Windows? (Give the typical path)

**128.** A customer reports an error message "Connection refused." What does this mean and what do you check?

**129.** What is the "5 Whys" technique? Give an example of using it for a slow database query.

**130.** A customer reports their email notifications stopped working. What are three possible causes?

### Medium (131–140)

**131.** A web application works in Chrome but not in Firefox. What are the possible causes and how do you troubleshoot?

**132.** A customer reports their database is running out of disk space. Walk through your investigation and resolution steps.

**133.** An API endpoint returns correct data for small requests but fails for large requests. What are the possible causes?

**134.** A customer reports intermittent connectivity issues. How do you diagnose the root cause?

**135.** A deployment caused a production outage. Walk through your incident response process.

**136.** A customer reports their application memory usage keeps growing over time. What is the likely issue and how do you investigate?

**137.** A website works fine internally but is slow for external users. What are the possible causes?

**138.** A customer reports their SSL certificate expired. What are the steps to resolve this?

**139.** A microservice is failing intermittently. How do you determine if the issue is in the service itself, the network, or a dependency?

**140.** A customer reports their backup job failed. What are the first five things you check?

### Hard (141–150)

**141.** A production database is experiencing deadlocks under high load. Walk through your analysis and resolution process.

**142.** A customer reports their application is slow only during business hours (9 AM – 5 PM). What are the likely causes and how do you investigate?

**143.** A distributed system has intermittent failures across multiple services. How do you identify the root cause using logs, metrics, and traces?

**144.** A customer reports data inconsistency between two systems that should be in sync. Walk through your troubleshooting process.

**145.** A memory leak is suspected in a Python application running in production. How do you confirm and identify the leaking code?

**146.** A customer reports their API response time increased from 200ms to 5s after a recent deployment. Walk through your investigation.

**147.** A load balancer is distributing traffic unevenly across servers. What are the possible causes and how do you fix it?

**148.** A customer reports their application works in staging but fails in production. What are the key differences to investigate?

**149.** A database query that used to take 1 second now takes 30 seconds. Walk through your step-by-step optimization process.

**150.** A customer reports their system is experiencing cascading failures. What is a cascading failure, how do you identify the root cause, and how do you prevent it?

---

## Section 5: Customer Support and Communication (Questions 151–175)

### Easy (151–160)

**151.** A customer is angry and frustrated. What are the first three things you do?

**152.** What is the difference between a bug and a feature request?

**153.** A customer reports an issue but provides no details. What questions do you ask?

**154.** How do you explain a technical issue to a non-technical customer? Give an example.

**155.** A customer asks you to fix something that is not a bug but a design limitation. How do you respond?

**156.** What is SLA? Why is it important in customer support?

**157.** A customer sends a vague email: "It doesn't work." What is your response?

**158.** How do you handle a customer who is asking for a feature that is not on the roadmap?

**159.** What is the best way to communicate a known issue to customers?

**160.** A customer reports an issue you cannot reproduce. What do you do?

### Medium (161–170)

**161.** A customer reports a critical issue but is unavailable for follow-up questions. How do you proceed?

**162.** How do you prioritize multiple customer issues? What factors do you consider?

**163.** A customer is escalating their issue to management. How do you handle this professionally?

**164.** You discover a customer is using your product incorrectly, causing their issue. How do you communicate this?

**165.** A customer reports a data loss issue. What are the immediate steps you take and how do you communicate with the customer?

**166.** How do you write a clear and effective bug report? What are the essential elements?

**167.** A customer is unhappy with the resolution you provided. What do you do?

**168.** How do you handle a situation where you don't know the answer to a customer's question?

**169.** A customer reports an issue that affects multiple users. How do you communicate this to all affected customers?

**170.** How do you document a resolved issue for future reference? What information do you include?

### Hard (171–175)

**171.** A major outage affects all customers. Walk through your communication plan: what do you communicate, when, and through which channels?

**172.** A customer threatens to cancel their subscription due to ongoing issues. How do you handle this situation?

**173.** You need to inform customers about a breaking API change. How do you craft the communication and timeline?

**174.** A customer reports a security vulnerability. What are the steps you take and how do you communicate with the customer?

**175.** A customer provides feedback that your product is too complex. How do you handle this feedback and what actions do you take?

---

## Section 6: JavaScript Basics (Questions 176–200)

### Easy (176–185)

**176.** What is the difference between `let`, `const`, and `var`?

**177.** Find the bug:
```javascript
function add(a, b) {
    return a - b;
}
console.log(add(5, 3));
```
What is the logical error?

**178.** What is the difference between `==` and `===`? Give an example where they produce different results.

**179.** Find the bug:
```javascript
const numbers = [1, 2, 3, 4, 5];
console.log(numbers[5]);
```
What is the output and why?

**180.** What is a callback function? Give a simple example.

**181.** Find the bug:
```javascript
let x = 10;
if (x = 5) {
    console.log("x is 5");
}
```
What is wrong and how do you fix it?

**182.** What is the difference between `null` and `undefined`?

**183.** Find the bug:
```javascript
const user = {
    name: "Alice",
    age: 25
};
console.log(user.email);
```
What is the output and how do you handle it safely?

**184.** What does `JSON.parse()` do? What happens if you pass invalid JSON?

**185.** Find the bug:
```javascript
for (var i = 0; i < 5; i++) {
    setTimeout(function() {
        console.log(i);
    }, 1000);
}
```
What is the unexpected output and how do you fix it?

### Medium (186–195)

**186.** Find the bug:
```javascript
const arr = [1, 2, 3, 4, 5];
const result = arr.map(function(num) {
    num * 2;
});
console.log(result);
```
What is the issue and how do you fix it?

**187.** What is a Promise? Write a simple example of creating and using a Promise.

**188.** Find the bug:
```javascript
async function fetchUser(id) {
    const response = await fetch(`/api/users/${id}`);
    const data = response.json();
    return data;
}
```
What is the issue and how do you fix it?

**189.** What is the difference between `forEach` and `map`? When would you use each?

**190.** Find the bug:
```javascript
const obj = {
    name: "Alice",
    greet: function() {
        console.log("Hello, " + this.name);
    }
};
const greet = obj.greet;
greet();
```
What is the output and how do you fix it?

**191.** What is event delegation? Give an example of when you would use it.

**192.** Find the bug:
```javascript
console.log(typeof null);
console.log(null instanceof Object);
```
What are the outputs and why are they surprising?

**193.** What is the spread operator? Give an example of using it with arrays and objects.

**194.** Find the bug:
```javascript
const numbers = [1, 2, 3, 4, 5];
const [a, b, c] = numbers;
console.log(a, b, c, d);
```
What error occurs and why?

**195.** What is the difference between `localStorage` and `sessionStorage`?

### Hard (196–200)

**196.** Find the bug:
```javascript
function createCounter() {
    let count = 0;
    return {
        increment: function() {
            count++;
        },
        getCount: function() {
            return count;
        }
    };
}

const counter1 = createCounter();
const counter2 = createCounter();
counter1.increment();
counter1.increment();
console.log(counter1.getCount());
console.log(counter2.getCount());
```
What is the output? Explain how closures work in this example.

**197.** Find the bug:
```javascript
const promise1 = new Promise((resolve) => {
    setTimeout(() => resolve(1), 1000);
});
const promise2 = new Promise((resolve) => {
    setTimeout(() => resolve(2), 500);
});
const promise3 = new Promise((resolve) => {
    setTimeout(() => resolve(3), 1500);
});

Promise.all([promise1, promise2, promise3]).then((results) => {
    console.log(results);
});
```
What is the output and how long does it take? What happens if one promise rejects?

**198.** Find the bug:
```javascript
class Animal {
    constructor(name) {
        this.name = name;
    }
    speak() {
        return `${this.name} makes a sound`;
    }
}

class Dog extends Animal {
    speak() {
        return `${this.name} barks`;
    }
}

const dog = new Dog("Rex");
console.log(dog.speak());
delete dog.speak;
console.log(dog.speak());
```
What is the output and why?

**199.** Find the bug:
```javascript
const obj = {
    a: 1,
    b: 2,
    c: 3
};

for (let key in obj) {
    console.log(key, obj[key]);
}

Object.prototype.d = 4;

for (let key in obj) {
    console.log(key, obj[key]);
}
```
What is the issue and how do you fix it?

**200.** Find the bug:
```javascript
function debounce(func, delay) {
    let timeout;
    return function(...args) {
        clearTimeout(timeout);
        timeout = setTimeout(() => {
            func.apply(this, args);
        }, delay);
    };
}

const expensiveOperation = debounce(() => {
    console.log("Operation executed");
}, 1000);

expensiveOperation();
expensiveOperation();
expensiveOperation();
```
What is the output? Explain how debouncing works. What is the difference between debouncing and throttling?

---

## Windows-Compatible Quick Reference

### VS Code
- **Open VS Code:** Press `Win + R`, type `code`, press Enter
- **Open folder:** `File > Open Folder` or `Ctrl + K, Ctrl + O`
- **Integrated terminal:** `` Ctrl + ` `` (backtick)
- **Run Python file:** Right-click in editor > `Run Python File in Terminal`
- **Install extension:** `Ctrl + Shift + X`, search for extension name
- **Format document:** `Shift + Alt + F`
- **Find in files:** `Ctrl + Shift + F`

### Postman
- **Open Postman:** Press `Win + R`, type `postman`, press Enter
- **Create new request:** `Ctrl + N`
- **Send request:** `Ctrl + Enter`
- **Save request:** `Ctrl + S`
- **Open Collection Runner:** Click `...` on collection > `Run collection`
- **Import cURL:** Click `Import` > `Raw text` > paste cURL
- **Open Environments:** Click gear icon (top right) > `Manage Environments`

### MySQL on Windows
- **Open MySQL Command Line:** Press `Win + R`, type `mysql -u root -p`, press Enter
- **Open MySQL Workbench:** Press `Win + R`, type `mysqlworkbench`, press Enter
- **Create database:** `CREATE DATABASE dbname;`
- **Show databases:** `SHOW DATABASES;`
- **Use database:** `USE dbname;`
- **Show tables:** `SHOW TABLES;`
- **Describe table:** `DESCRIBE tablename;`
- **Export to CSV (Workbench):** Right-click table > `Table Data Export Wizard`
- **Import CSV (Workbench):** Right-click table > `Table Data Import Wizard`

---

*End of 200 Questions*
