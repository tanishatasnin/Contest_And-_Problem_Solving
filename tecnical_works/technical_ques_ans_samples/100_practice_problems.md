# 150 Practice Problems — Technical Support Engineer

## Job Requirements Coverage
- Python, JavaScript
- SQL and scripting
- API request/response debugging
- AI-assisted workflows (Claude, Claude Code)
- Production debugging & root-cause analysis
- Customer communication

---

## Section 1: Python Debugging (1–35)

**1.** Find the bug:
```python
def calculate_discount(price, discount_percent):
    return price - (price * discount_percent)

result = calculate_discount(100, 20)
print(result)
```
Expected: 80. What is the issue?

**2.** Find the bug:
```python
import requests

def get_user(user_id):
    response = requests.get(f"https://api.example.com/users/{user_id}")
    return response.json()["name"]

print(get_user(1))
```
What could go wrong? Add proper error handling.

**3.** Find the bug:
```python
def process_items(items):
    results = []
    for item in items:
        if item > 0:
            results.append(item * 2)
        return results

print(process_items([1, 2, 3]))
```
What is wrong?

**4.** Find the bug:
```python
class DatabaseConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connection = None

    def connect(self):
        self.connection = f"Connected to {self.host}:{self.port}"

    def query(self, sql):
        return f"Result of: {sql}"

db = DatabaseConnection("localhost", 5432)
print(db.query("SELECT * FROM users"))
```
What error occurs and why?

**5.** Find the bug:
```python
def read_config(filename):
    with open(filename, "r") as f:
        config = eval(f.read())
    return config

config = read_config("config.txt")
print(config["database"]["host"])
```
What is the security issue and how do you fix it?

**6.** Find the bug:
```python
import json

data = '{"users": [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]}'
parsed = json.loads(data)

for user in parsed:
    print(user["name"])
```
What error occurs and how do you fix it?

**7.** Find the bug:
```python
def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")

result = divide_numbers(10, 0)
print(result)
```
What is the issue with the return value?

**8.** Find the bug:
```python
numbers = [1, 2, 3, 4, 5]
squared = []
for num in numbers:
    squared.append(num ** 2)
    print(squared)
```
What is the indentation issue?

**9.** Find the bug:
```python
def send_email(to, subject, body):
    import smtplib
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("user@gmail.com", "password")
    server.sendmail("user@gmail.com", to, f"Subject: {subject}\n\n{body}")
    server.quit()

send_email("customer@example.com", "Test", "Hello")
```
What are three issues with this code?

**10.** Find the bug:
```python
import threading

counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1

threads = [threading.Thread(target=increment) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(counter)
```
What is the issue and how do you fix it?

**11.** Find the bug:
```python
def parse_date(date_string):
    from datetime import datetime
    return datetime.strptime(date_string, "%Y-%m-%d")

dates = ["2024-01-15", "2024-02-30", "2024-03-10"]
for date in dates:
    print(parse_date(date))
```
What error occurs and how do you handle it?

**12.** Find the bug:
```python
import subprocess

def run_command(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout

output = run_command("dir")
print(output)
```
What is the security risk and how do you mitigate it?

**13.** Find the bug:
```python
def get_nested_value(data, *keys):
    for key in keys:
        data = data[key]
    return data

config = {"database": {"host": "localhost", "port": 5432}}
print(get_nested_value(config, "database", "host"))
print(get_nested_value(config, "database", "credentials", "username"))
```
What error occurs and how do you handle it safely?

**14.** Find the bug:
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_order(order_id):
    logger.info(f"Processing order {order_id}")
    result = order_id / 0
    logger.info(f"Order {order_id} processed successfully")
    return result

process_order(123)
```
What is wrong with the error handling?

**15.** Find the bug:
```python
from functools import wraps

def retry(max_attempts=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
            raise Exception("All retries failed")
        return wrapper
    return decorator

@retry(max_attempts=3)
def unstable_function():
    import random
    if random.random() < 0.8:
        raise ValueError("Random failure")
    return "Success"

print(unstable_function())
```
What is missing from this retry logic?

**16.** Find the bug:
```python
import asyncio

async def fetch_data(url, delay):
    await asyncio.sleep(delay)
    return f"Data from {url}"

async def main():
    urls = [("url1", 2), ("url2", 1), ("url3", 3)]
    results = []
    for url, delay in urls:
        result = await fetch_data(url, delay)
        results.append(result)
    return results

asyncio.run(main())
```
What is the performance issue and how do you fix it?

**17.** Find the bug:
```python
class Cache:
    def __init__(self):
        self._cache = {}

    def get(self, key):
        return self._cache.get(key)

    def set(self, key, value):
        self._cache[key] = value

    def clear(self):
        self._cache = {}

cache = Cache()
cache.set("user:1", {"name": "Alice"})
print(cache.get("user:1"))
cache.set("user:1", {"name": "Bob"})
print(cache.get("user:1"))
```
What is missing from this cache implementation for production use?

**18.** Find the bug:
```python
import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+$"
    return bool(re.match(pattern, email))

print(validate_email("user@example.com"))
print(validate_email("user.name+tag@example.co.uk"))
print(validate_email("user@subdomain.example.com"))
```
What is the issue with the regex?

**19.** Find the bug:
```python
def flatten_list(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

nested = [1, [2, [3, [4, 5]]], 6]
print(flatten_list(nested))
```
What is the potential issue with deeply nested lists?

**20.** Find the bug:
```python
import json
from datetime import datetime

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

data = {
    "name": "Alice",
    "created_at": datetime.now()
}
print(json.dumps(data, cls=CustomEncoder))
```
What is missing to make this work correctly?

**21.** Find the bug:
```python
def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        else:
            print(i)

fizzbuzz(15)
```
What is the logical error?

**22.** Find the bug:
```python
def remove_vowels(text):
    vowels = "aeiou"
    for vowel in vowels:
        text.replace(vowel, "")
    return text

print(remove_vowels("hello world"))
```
What is wrong and how do you fix it?

**23.** Find the bug:
```python
def is_palindrome(text):
    return text == text[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("Racecar"))
print(is_palindrome("A man a plan a canal Panama"))
```
What are the issues with this implementation?

**24.** Find the bug:
```python
def get_max(numbers):
    max_val = 0
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

print(get_max([1, 5, 3, 9, 2]))
print(get_max([-1, -5, -3, -9, -2]))
```
What is the issue and how do you fix it?

**25.** Find the bug:
```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return self.items.count()

stack = Stack()
stack.push(1)
stack.push(2)
print(stack.size())
```
What error occurs and how do you fix it?

**26.** Find the bug:
```python
def word_count(text):
    words = text.split(" ")
    count = {}
    for word in words:
        count[word] += 1
    return count

print(word_count("hello world hello"))
```
What error occurs and how do you fix it?

**27.** Find the bug:
```python
import copy

original = [[1, 2], [3, 4]]
duplicate = copy.copy(original)
duplicate[0][0] = 99

print(original)
print(duplicate)
```
What is the issue and how do you fix it?

**28.** Find the bug:
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(35))
```
What is the performance issue and how do you fix it?

**29.** Find the bug:
```python
def average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

data = []
print(average(data))
```
What error occurs and how do you handle it?

**30.** Find the bug:
```python
try:
    file = open("data.txt", "r")
    data = file.read()
    print(data)
finally:
    file.close()
```
What error occurs if the file doesn't exist and how do you fix it?

**31.** Find the bug:
```python
def merge_dicts(dict1, dict2):
    result = dict1
    for key, value in dict2.items():
        result[key] = value
    return result

d1 = {"a": 1}
d2 = {"b": 2}
result = merge_dicts(d1, d2)
print(d1)
print(result)
```
What is the unexpected behavior and how do you fix it?

**32.** Find the bug:
```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 == s2)
print(s1 is s2)
```
What is the issue with this implementation?

**33.** Find the bug:
```python
def sum_args(*args):
    total = 0
    for arg in args:
        total += arg
    return total

numbers = [1, 2, 3, 4, 5]
print(sum_args(numbers))
```
What is the issue and how do you fix it?

**34.** Find the bug:
```python
def capitalize_words(sentence):
    words = sentence.split()
    capitalized = []
    for word in words:
        capitalized.append(word[0].upper() + word[1:])
    return " ".join(capitalized)

print(capitalize_words("hello world"))
print(capitalize_words(""))
```
What error occurs and how do you handle it?

**35.** Find the bug:
```python
def group_by_length(words):
    result = {}
    for word in words:
        length = len(word)
        if length not in result:
            result[length] = word
    return result

words = ["a", "bb", "ccc", "dd", "eee"]
print(group_by_length(words))
```
What is the logical error and how do you fix it?

---

## Section 2: JavaScript & Node.js Debugging (36–60)

**36.** Find the bug:
```javascript
const express = require('express');
const app = express();

app.get('/api/users/:id', (req, res) => {
    const userId = req.params.id;
    const user = { id: userId, name: 'Alice' };
    res.json(user);
});

app.listen(3000);
console.log('Server running on port 3000');
```
What is missing for production use?

**37.** Find the bug:
```javascript
async function fetchUsers() {
    const response = await fetch('/api/users');
    const users = response.json();
    return users;
}

fetchUsers().then(users => {
    users.forEach(user => console.log(user.name));
});
```
What error occurs and how do you fix it?

**38.** Find the bug:
```javascript
const config = {
    api: {
        baseUrl: 'https://api.example.com',
        timeout: 5000
    }
};

function getApiUrl(endpoint) {
    return `${config.api.baseUrl}/${endpoint}`;
}

console.log(getApiUrl('users'));
config.api = null;
console.log(getApiUrl('products'));
```
What error occurs and how do you prevent it?

**39.** Find the bug:
```javascript
class EventEmitter {
    constructor() {
        this.events = {};
    }

    on(event, listener) {
        if (!this.events[event]) {
            this.events[event] = [];
        }
        this.events[event].push(listener);
    }

    emit(event, data) {
        if (this.events[event]) {
            this.events[event].forEach(listener => listener(data));
        }
    }
}

const emitter = new EventEmitter();
emitter.on('error', (err) => console.error(err));
emitter.emit('error', new Error('Test'));
emitter.emit('error', new Error('Test2'));
```
What is missing from this implementation?

**40.** Find the bug:
```javascript
function debounce(func, wait) {
    let timeout;
    return function(...args) {
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(this, args), wait);
    };
}

const searchInput = document.getElementById('search');
searchInput.addEventListener('input', debounce((e) => {
    console.log('Searching for:', e.target.value);
}, 300));
```
What is the issue with this debounce implementation?

**41.** Find the bug:
```javascript
const promise1 = new Promise((resolve) => setTimeout(() => resolve(1), 1000));
const promise2 = new Promise((resolve) => setTimeout(() => resolve(2), 500));
const promise3 = new Promise((resolve, reject) => setTimeout(() => reject(new Error('Failed')), 750));

Promise.all([promise1, promise2, promise3])
    .then(results => console.log(results))
    .catch(error => console.error(error));
```
What is the output and why?

**42.** Find the bug:
```javascript
const obj = {
    name: 'Alice',
    greet: function() {
        setTimeout(function() {
            console.log('Hello, ' + this.name);
        }, 1000);
    }
};

obj.greet();
```
What is the output and how do you fix it?

**43.** Find the bug:
```javascript
const numbers = [1, 2, 3, 4, 5];
const result = numbers.filter(num => num > 2).map(num => num * 2);
console.log(result);

const sum = numbers.reduce((acc, num) => acc + num);
console.log(sum);
```
What is the issue with the reduce call?

**44.** Find the bug:
```javascript
const http = require('http');

const server = http.createServer((req, res) => {
    let body = '';
    req.on('data', chunk => {
        body += chunk;
    });
    req.on('end', () => {
        const data = JSON.parse(body);
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ received: data }));
    });
});

server.listen(3000);
```
What could go wrong and how do you handle it?

**45.** Find the bug:
```javascript
class ApiClient {
    constructor(baseUrl) {
        this.baseUrl = baseUrl;
    }

    async get(endpoint) {
        const response = await fetch(`${this.baseUrl}${endpoint}`);
        return response.json();
    }

    async post(endpoint, data) {
        const response = await fetch(`${this.baseUrl}${endpoint}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        return response.json();
    }
}

const client = new ApiClient('https://api.example.com');
client.get('/users').then(users => console.log(users));
```
What is missing for production use?

**46.** Find the bug:
```javascript
const arr = [1, 2, 3, 4, 5];
const [a, b, c, d, e, f] = arr;
console.log(a, b, c, d, e, f);
```
What is the output for `f` and why?

**47.** Find the bug:
```javascript
function createUser(name, age) {
    return {
        name,
        age,
        createdAt: new Date()
    };
}

const user1 = createUser('Alice', 30);
const user2 = createUser('Bob', 25);
user1.createdAt = '2024-01-01';
console.log(user2.createdAt);
```
What is the potential issue with object references?

**48.** Find the bug:
```javascript
const express = require('express');
const app = express();

app.use((req, res, next) => {
    console.log(`${req.method} ${req.url}`);
    next();
});

app.get('/api/data', (req, res) => {
    res.json({ data: 'test' });
});

app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong' });
});

app.listen(3000);
```
What is the issue with the error handling middleware placement?

**49.** Find the bug:
```javascript
const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
    name: String,
    email: { type: String, unique: true },
    createdAt: { type: Date, default: Date.now }
});

const User = mongoose.model('User', userSchema);

async function createUser(name, email) {
    const user = new User({ name, email });
    await user.save();
    return user;
}

createUser('Alice', 'alice@example.com')
    .then(user => console.log('Created:', user))
    .catch(err => console.error('Error:', err));
```
What is missing for proper error handling?

**50.** Find the bug:
```javascript
const cluster = require('cluster');
const os = require('os');

if (cluster.isMaster) {
    const numCPUs = os.cpus().length;
    for (let i = 0; i < numCPUs; i++) {
        cluster.fork();
    }
} else {
    const express = require('express');
    const app = express();
    app.get('/', (req, res) => res.send('Hello'));
    app.listen(3000);
}
```
What is the issue with this clustering approach?

**51.** Find the bug:
```javascript
const arr = [1, 2, 3, 4, 5];
arr.forEach(num => {
    if (num === 3) {
        arr.push(6);
    }
    console.log(num);
});
```
What is the unexpected behavior and why?

**52.** Find the bug:
```javascript
console.log(typeof []);
console.log(Array.isArray([]));
console.log([] instanceof Array);
console.log([] instanceof Object);
```
What are the outputs and why might they be confusing?

**53.** Find the bug:
```javascript
const user = {
    name: 'Alice',
    address: {
        city: 'New York'
    }
};

console.log(user.address.zipCode);
console.log(user.profile.bio);
```
What errors occur and how do you safely access nested properties?

**54.** Find the bug:
```javascript
function fetchUserData(userId) {
    fetch(`/api/users/${userId}`)
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error(error));
}

fetchUserData(1);
fetchUserData(2);
fetchUserData(3);
```
What is missing for proper error handling and how do you ensure all requests complete?

**55.** Find the bug:
```javascript
const numbers = [1, 2, 3];
const result = numbers.map(num => {
    num * 2;
});
console.log(result);
```
What is the output and how do you fix it?

**56.** Find the bug:
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

const dog = new Dog('Rex');
console.log(dog.speak());
delete dog.speak;
console.log(dog.speak());
```
What is the output and why?

**57.** Find the bug:
```javascript
let x = 10;
function outer() {
    console.log(x);
    let x = 20;
    console.log(x);
}
outer();
```
What error occurs and why?

**58.** Find the bug:
```javascript
const obj = {
    value: 42,
    getValue: function() {
        return this.value;
    }
};

const fn = obj.getValue;
console.log(fn());
console.log(obj.getValue());
```
What are the outputs and why?

**59.** Find the bug:
```javascript
async function processItems(items) {
    const results = [];
    for (const item of items) {
        const result = await fetch(`/api/process/${item}`);
        results.push(result);
    }
    return results;
}

processItems([1, 2, 3, 4, 5]).then(console.log);
```
What is the performance issue and how do you fix it?

**60.** Find the bug:
```javascript
const express = require('express');
const app = express();

app.get('/api/search', (req, res) => {
    const query = req.query.q;
    const page = req.query.page;
    const limit = req.query.limit;

    const results = searchDatabase(query, page, limit);
    res.json(results);
});

app.listen(3000);
```
What is missing for production use?

---

## Section 3: SQL & Database (61–85)

**61.** Write a query to find all users who registered in the last 30 days and have placed at least one order.

**62.** Write a query to find the top 5 products by revenue, including product name and total revenue.

**63.** Write a query to find duplicate email addresses in a `users` table.

**64.** Write a query to calculate the month-over-month growth rate of revenue.

**65.** Write a query to find all orders that have been pending for more than 7 days.

**66.** Write a query to find customers who have not logged in for 90 days but have an active subscription.

**67.** Write a query to pivot sales data by quarter (columns: Q1, Q2, Q3, Q4).

**68.** Write a recursive CTE to find all subordinates of a given manager.

**69.** Write a query to find the longest streak of consecutive daily logins for each user.

**70.** Write a query to calculate a running total of sales ordered by date.

**71.** Write a query to find the second highest salary without using `LIMIT` or `OFFSET`.

**72.** Write a query to delete all duplicate rows keeping only the one with the lowest `id`.

**73.** Write a query to find all users who have purchased every product in a specific category.

**74.** Write a query to calculate the median order value.

**75.** A customer reports a query that used to run in 1 second now takes 30 seconds. Walk through your investigation process.

**76.** Write a query to find all sessions where a user visited more than 3 pages (table: `page_views` with columns `session_id`, `page_url`, `timestamp`).

**77.** Write a query to find the most recent order for each customer.

**78.** Write a query to calculate the percentage of users who have made a purchase (vs. total registered users).

**79.** Write a query to find all products that have never been ordered.

**80.** Write a query to find the average time between a user's first and second purchase.

**81.** Write a query to find all customers whose total spending is above the average customer spending.

**82.** Write a query to find all pairs of users who have the same IP address (table: `login_history` with `user_id`, `ip_address`, `login_time`).

**83.** Write a query to calculate a 7-day rolling average of daily revenue.

**84.** Write a query to find all orders where the shipping address differs from the billing address.

**85.** Write a query to find the top 3 most common error messages from an `error_logs` table in the last 24 hours.

---

## Section 4: API Debugging (86–120)

**86.** A customer's API call returns `401 Unauthorized`. What are the possible causes and how do you troubleshoot each?

**87.** A customer reports their API call works in Postman but fails in their JavaScript code. What are the possible causes?

**88.** An API endpoint returns `500 Internal Server Error` intermittently. How do you investigate?

**89.** A customer needs to upload a large file (500MB) via API. What are the considerations and how do you implement it?

**90.** A customer reports API response times increased from 200ms to 5s. Walk through your troubleshooting process.

**91.** How do you debug a CORS error? What are the common causes and fixes?

**92.** A customer's OAuth token keeps expiring. Explain the token lifecycle and how to implement refresh tokens.

**93.** How do you handle API rate limiting? What headers do you check and what is the best retry strategy?

**94.** A customer reports their webhook deliveries are failing. How do you investigate and fix?

**95.** How do you debug an API that returns different responses for the same request?

**96.** A customer needs to migrate from API v1 to v2. How do you plan and communicate this?

**97.** How do you set up API monitoring and alerting? What metrics do you track?

**98.** A customer reports their API calls are timing out. What are the possible causes and how do you diagnose each?

**99.** How do you debug an API authentication issue in a microservices architecture?

**100.** A customer's API integration broke after your latest deployment. How do you investigate and resolve?

**101.** In Postman, write a pre-request script that generates a random email address and stores it in an environment variable.

**102.** How do you set up a Postman collection with a request that depends on the response of a previous request? Walk through the full workflow.

**103.** A customer reports that their API call returns `200 OK` but the response body is empty. What are the possible causes?

**104.** How do you debug a memory leak in a Node.js application? What tools and techniques do you use?

**105.** A customer's API returns `403 Forbidden` but they have a valid token. What are the possible causes?

**106.** How do you use Postman's Collection Runner to test an API with 100 different input values? List the steps.

**107.** A customer reports their API integration works with small payloads but fails with large ones (>10MB). What are the possible causes?

**108.** How do you debug a race condition in a Python application? Walk through your approach.

**109.** In Postman, write a test script that validates a JSON response has specific fields with correct data types.

**110.** A customer reports their API calls are slow only from a specific geographic region. How do you investigate?

**111.** How do you debug an SSL/TLS certificate issue? What are the common causes and fixes?

**112.** A customer needs to implement idempotency in their API. Explain the concept and how to implement it.

**113.** How do you use Postman to test a file upload endpoint? List the steps.

**114.** A customer reports their API returns inconsistent results when called concurrently. What is the likely issue and how do you fix it?

**115.** How do you debug a database connection pool exhaustion issue? What are the symptoms and fixes?

**116.** In Postman, how do you set up an environment with variables for different stages (dev, staging, production)? List the steps.

**117.** A customer's API integration broke after they updated their SSL certificate. How do you investigate?

**118.** How do you debug a CORS preflight (OPTIONS) request that fails? What are the common causes?

**119.** A customer needs to implement API versioning. Compare the three common approaches (URL path, header, query parameter).

**120.** How do you use Postman to mock an API endpoint that doesn't exist yet? List the steps.

---

## Section 5: Troubleshooting Scenarios (121–150)

**121.** A customer reports "the website is down." Walk through your complete troubleshooting process from initial contact to resolution.

**122.** A customer reports their application works in staging but fails in production. What are the key differences to investigate?

**123.** A customer reports intermittent connectivity issues. How do you diagnose the root cause?

**124.** A customer reports their data is missing. What are the immediate steps you take?

**125.** A customer reports their application is slow only during business hours. What are the likely causes?

**126.** A customer reports a critical issue but is unavailable for follow-up questions. How do you proceed?

**127.** A customer is angry and threatening to cancel their subscription. How do you handle this situation?

**128.** A major outage affects all customers. Walk through your incident response and communication plan.

**129.** A customer reports an issue you cannot reproduce. What steps do you take?

**130.** A customer provides feedback that your product is too complex. How do you handle this feedback and what actions do you take?

**131.** A customer reports that their API calls return different data each time, even though the database hasn't changed. What are the possible causes?

**132.** A customer reports their application crashes when processing files larger than 100MB. How do you investigate and fix?

**133.** A customer reports that their automated tests pass locally but fail in CI/CD. What are the key differences to investigate?

**134.** A customer's application was working yesterday but is broken today, and no changes were made. What are the possible causes?

**135.** A customer reports their database is running out of connections during peak hours. Walk through your investigation and resolution.

**136.** A customer reports their application memory usage grows continuously until it crashes. How do you investigate?

**137.** A customer reports their API integration works for one user but fails for another with the same permissions. What are the possible causes?

**138.** A customer reports their scheduled job that runs every hour sometimes takes 30 minutes to complete. What are the possible causes?

**139.** A customer reports their web application works in Chrome but shows a blank page in Safari. How do you troubleshoot?

**140.** A customer reports their backup restoration failed. What are the steps you take to recover?

**141.** A customer reports their API returns `502 Bad Gateway` errors randomly (about 5% of requests). How do you investigate?

**142.** A customer reports their application is slow after a recent deployment, but the deployment only changed frontend code. What are the possible causes?

**143.** A customer reports their email notifications are delayed by several hours. Walk through your investigation.

**144.** A customer reports their API integration returns `422 Unprocessable Entity`. What does this mean and how do you help them fix it?

**145.** A customer reports their application's SSL certificate expired and they need it renewed urgently. What are the steps?

**146.** A customer reports their database query works in MySQL Workbench but fails in their Python application. What are the possible causes?

**147.** A customer reports their API integration stopped working with no changes on their side. What are the first things you check?

**148.** A customer reports their application is experiencing intermittent `OutOfMemoryError` crashes. How do you investigate?

**149.** A customer reports their API calls are failing with `429 Too Many Requests` but they are well below their rate limit. What are the possible causes?

**150.** A customer reports their application was hacked — unauthorized users accessed their data. What are the immediate steps you take?

---

## Windows-Compatible Quick Reference

### VS Code
- **Open VS Code:** Press `Win + R`, type `code`, press Enter
- **Open folder:** `File > Open Folder` or `Ctrl + K, Ctrl + O`
- **Integrated terminal:** `` Ctrl + ` `` (backtick)
- **Run Python file:** Right-click in editor > `Run Python File in Terminal`
- **Run JavaScript/Node.js:** Open terminal → `node filename.js`
- **Install extension:** `Ctrl + Shift + X`, search for extension name
- **Format document:** `Shift + Alt + F`
- **Find in files:** `Ctrl + Shift + F`
- **Debug:** `F5` to start debugging, `F10` to step over, `F11` to step into

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

### Git on Windows
- **Clone repository:** `git clone https://github.com/user/repo.git`
- **Check status:** `git status`
- **Create branch:** `git checkout -b branchname`
- **Commit changes:** `git add .` then `git commit -m "message"`
- **Push changes:** `git push origin branchname`
- **Pull latest:** `git pull origin main`

---

*End of 150 Practice Problems*
