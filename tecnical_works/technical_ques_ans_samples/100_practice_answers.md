# 150 Practice Problems — Answer Key

## Section 1: Python Debugging (1–35)

**1.** The discount is not divided by 100.
```python
def calculate_discount(price, discount_percent):
    return price - (price * (discount_percent / 100))
```

**2.** No error handling for network failures, no HTTP status check, no missing key handling.
```python
import requests

def get_user(user_id):
    try:
        response = requests.get(f"https://api.example.com/users/{user_id}", timeout=10)
        response.raise_for_status()
        return response.json().get("name")
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"
    except (ValueError, KeyError) as e:
        return f"Data error: {e}"
```

**3.** `return` is inside the `for` loop.
```python
def process_items(items):
    results = []
    for item in items:
        if item > 0:
            results.append(item * 2)
    return results
```

**4.** `connect()` was never called, so `self.connection` is `None`.
```python
db = DatabaseConnection("localhost", 5432)
db.connect()
print(db.query("SELECT * FROM users"))
```

**5.** `eval()` executes arbitrary code. Use `json.load()`.
```python
import json

def read_config(filename):
    with open(filename, "r") as f:
        config = json.load(f)
    return config
```

**6.** `parsed` is a dict with key `"users"`, not a list.
```python
for user in parsed["users"]:
    print(user["name"])
```

**7.** Returns `None` on error — caller can't distinguish from valid result.
```python
def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
```

**8.** `print(squared)` is inside the loop.
```python
numbers = [1, 2, 3, 4, 5]
squared = []
for num in numbers:
    squared.append(num ** 2)
print(squared)
```

**9.** Three issues: hardcoded credentials, no error handling, no TLS verification.
```python
import os
import smtplib
from email.mime.text import MIMEText

def send_email(to, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = os.environ.get('EMAIL_USER')
    msg['To'] = to
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(os.environ.get('EMAIL_USER'), os.environ.get('EMAIL_PASS'))
            server.send_message(msg)
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
```

**10.** Race condition — `counter += 1` is not atomic.
```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1
```

**11.** `ValueError: day is out of range for month` — Feb 30 doesn't exist.
```python
from datetime import datetime

dates = ["2024-01-15", "2024-02-30", "2024-03-10"]
for date in dates:
    try:
        print(parse_date(date))
    except ValueError as e:
        print(f"Invalid date: {date} - {e}")
```

**12.** Command injection risk with `shell=True`.
```python
import subprocess
import shlex

def run_command(cmd):
    result = subprocess.run(shlex.split(cmd), capture_output=True, text=True)
    return result.stdout
```

**13.** `KeyError` when key doesn't exist.
```python
def get_nested_value(data, *keys, default=None):
    for key in keys:
        if isinstance(data, dict) and key in data:
            data = data[key]
        else:
            return default
    return data
```

**14.** No try/except — error propagates uncaught.
```python
def process_order(order_id):
    logger.info(f"Processing order {order_id}")
    try:
        result = order_id / 1
        logger.info(f"Order {order_id} processed successfully")
        return result
    except Exception as e:
        logger.error(f"Failed to process order {order_id}: {e}")
        raise
```

**15.** No delay between retries.
```python
import time

def retry(max_attempts=3, backoff=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    time.sleep(backoff * (2 ** attempt))
        return wrapper
    return decorator
```

**16.** Requests run sequentially.
```python
async def main():
    urls = [("url1", 2), ("url2", 1), ("url3", 3)]
    tasks = [fetch_data(url, delay) for url, delay in urls]
    results = await asyncio.gather(*tasks)
    return results
```

**17.** Missing TTL, max size limit, thread safety, cache invalidation.
```python
import time
import threading

class Cache:
    def __init__(self, max_size=1000, ttl=300):
        self._cache = {}
        self._max_size = max_size
        self._ttl = ttl
        self._lock = threading.Lock()

    def get(self, key):
        with self._lock:
            if key in self._cache:
                value, timestamp = self._cache[key]
                if time.time() - timestamp < self._ttl:
                    return value
                del self._cache[key]
            return None

    def set(self, key, value):
        with self._lock:
            if len(self._cache) >= self._max_size:
                oldest = min(self._cache, key=lambda k: self._cache[k][1])
                del self._cache[oldest]
            self._cache[key] = (value, time.time())
```

**18.** Regex doesn't handle dots, plus signs, hyphens, or subdomains.
```python
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
```

**19.** `RecursionError` for deeply nested lists.
```python
def flatten_list(nested_list):
    result = []
    stack = [nested_list]
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            stack.extend(reversed(current))
        else:
            result.append(current)
    return result
```

**20.** The code is correct. For more types:
```python
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, set):
            return list(obj)
        return super().default(obj)
```

**21.** The `FizzBuzz` condition is never reached because `i % 3 == 0` catches it first.
```python
def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
```

**22.** `str.replace()` returns a new string; result is discarded.
```python
def remove_vowels(text):
    vowels = "aeiou"
    for vowel in vowels:
        text = text.replace(vowel, "")
    return text
```

**23.** Case-sensitive and doesn't handle spaces/punctuation.
```python
def is_palindrome(text):
    cleaned = "".join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]
```

**24.** Initial `max_val = 0` fails for all-negative arrays.
```python
def get_max(numbers):
    if not numbers:
        return None
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val
```

**25.** `self.items.count()` — wrong method; use `len()`.
```python
def size(self):
    return len(self.items)
```

**26.** `count[word] += 1` — `KeyError` when word not in dict. Use `collections.Counter` or `dict.get()`.
```python
def word_count(text):
    words = text.split()
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count
```

**27.** Shallow copy — nested lists share references.
```python
import copy

original = [[1, 2], [3, 4]]
duplicate = copy.deepcopy(original)
duplicate[0][0] = 99
```

**28.** Exponential time complexity — redundant calculations.
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

**29.** `ZeroDivisionError` on empty list.
```python
def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
```

**30.** `NameError` — `file` undefined if `open()` fails.
```python
try:
    with open("data.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("File not found")
```

**31.** `dict1` is modified in place — caller's original dict changes.
```python
def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = value
    return result
```

**32.** Not thread-safe — race condition between check and creation.
```python
import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
```

**33.** Passes list as single argument instead of unpacking.
```python
print(sum_args(*numbers))
```

**34.** `IndexError` on empty string (word is `""`).
```python
def capitalize_words(sentence):
    if not sentence:
        return ""
    words = sentence.split()
    capitalized = []
    for word in words:
        capitalized.append(word[0].upper() + word[1:])
    return " ".join(capitalized)
```

**35.** Stores only one word per length instead of grouping.
```python
def group_by_length(words):
    result = {}
    for word in words:
        length = len(word)
        if length not in result:
            result[length] = []
        result[length].append(word)
    return result
```

---

## Section 2: JavaScript & Node.js Debugging (36–60)

**36.** Missing error handling, request validation, graceful shutdown, security headers, timeout.
```javascript
const express = require('express');
const app = express();

app.use(express.json({ limit: '10mb' }));

app.get('/api/users/:id', (req, res) => {
    const userId = req.params.id;
    if (!userId) return res.status(400).json({ error: 'Invalid ID' });
    const user = { id: userId, name: 'Alice' };
    res.json(user);
});

app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Internal server error' });
});

const server = app.listen(3000);
process.on('SIGTERM', () => server.close());
```

**37.** Missing `await` on `response.json()`.
```javascript
async function fetchUsers() {
    const response = await fetch('/api/users');
    const users = await response.json();
    return users;
}
```

**38.** `TypeError: Cannot read properties of null`.
```javascript
function getApiUrl(endpoint) {
    if (!config.api) throw new Error('API config not initialized');
    return `${config.api.baseUrl}/${endpoint}`;
}
```

**39.** Missing `off()`, `once()`, error handling in emit.
```javascript
off(event, listener) {
    if (this.events[event]) {
        this.events[event] = this.events[event].filter(l => l !== listener);
    }
}
```

**40.** Debounce is correct. For immediate execution support:
```javascript
function debounce(func, wait, immediate = false) {
    let timeout;
    return function(...args) {
        const callNow = immediate && !timeout;
        clearTimeout(timeout);
        timeout = setTimeout(() => {
            timeout = null;
            if (!immediate) func.apply(this, args);
        }, wait);
        if (callNow) func.apply(this, args);
    };
}
```

**41.** Output: `Error: Failed` — `Promise.all` rejects on first rejection. Use `Promise.allSettled()` for all results.

**42.** Output: `Hello, undefined` — `this` refers to global object.
```javascript
greet: function() {
    setTimeout(() => {
        console.log('Hello, ' + this.name);
    }, 1000);
}
```

**43.** `reduce` without initial value fails on empty array.
```javascript
const sum = numbers.reduce((acc, num) => acc + num, 0);
```

**44.** No error handling for invalid JSON, no request size limit, no timeout.
```javascript
req.on('end', () => {
    try {
        const data = JSON.parse(body);
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ received: data }));
    } catch (e) {
        res.writeHead(400);
        res.end(JSON.stringify({ error: 'Invalid JSON' }));
    }
});
```

**45.** Missing error handling, timeout, retry logic, response status check.
```javascript
async get(endpoint) {
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 10000);
    try {
        const response = await fetch(`${this.baseUrl}${endpoint}`, { signal: controller.signal });
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        return response.json();
    } finally {
        clearTimeout(timeout);
    }
}
```

**46.** Output: `undefined` — array has only 5 elements.

**47.** Separate objects, so modifying one doesn't affect the other. The real issue is `Date` objects are mutable — use `Object.freeze()` or return copies.

**48.** Error middleware placement is after routes — move it after all routes.
```javascript
app.get('/api/data', (req, res) => {
    res.json({ data: 'test' });
});

app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong' });
});
```

**49.** Missing connection error handling, duplicate key handling, validation.
```javascript
async function createUser(name, email) {
    try {
        const user = new User({ name, email });
        await user.save();
        return user;
    } catch (err) {
        if (err.code === 11000) throw new Error('Email already exists');
        throw err;
    }
}
```

**50.** All workers share port 3000. No crash handling.
```javascript
if (cluster.isMaster) {
    for (let i = 0; i < numCPUs; i++) {
        cluster.fork();
    }
    cluster.on('exit', (worker) => {
        console.log(`Worker ${worker.process.pid} died`);
        cluster.fork();
    });
} else {
    app.listen(3000);
}
```

**51.** Array grows during iteration — `forEach` visits newly added elements too. Output: `1 2 3 4 5 6`.

**52.** Outputs: `object, true, true, true`. `typeof []` returns `"object"` (historical JS quirk). `[] instanceof Object` is `true` since arrays inherit from Object.

**53.** `TypeError: Cannot read properties of undefined`. Use optional chaining.
```javascript
console.log(user.address?.zipCode);
console.log(user.profile?.bio);
```

**54.** No error handling, no guarantee all requests complete. Use `Promise.all`.
```javascript
async function fetchAllUsers() {
    const promises = [fetchUserData(1), fetchUserData(2), fetchUserData(3)];
    return Promise.all(promises);
}
```

**55.** Missing `return` in arrow function.
```javascript
const result = numbers.map(num => num * 2);
```

**56.** First: `"Rex barks"`. After `delete`: `"Rex makes a sound"` — falls through to `Animal.prototype.speak`.

**57.** `ReferenceError: Cannot access 'x' before initialization` — temporal dead zone. The inner `let x` shadows outer `x`.

**58.** `fn()` → `undefined` (no `this` binding). `obj.getValue()` → `42` (method invocation sets `this`).

**59.** Requests run sequentially — total time = sum of all delays.
```javascript
async function processItems(items) {
    const promises = items.map(item => fetch(`/api/process/${item}`));
    return Promise.all(promises);
}
```

**60.** Missing input validation, error handling, pagination, rate limiting, timeout.
```javascript
app.get('/api/search', async (req, res) => {
    const { q, page = 1, limit = 20 } = req.query;
    if (!q) return res.status(400).json({ error: 'Query required' });
    try {
        const results = await searchDatabase(q, parseInt(page), parseInt(limit));
        res.json(results);
    } catch (err) {
        res.status(500).json({ error: 'Search failed' });
    }
});
```

---

## Section 3: SQL & Database (61–85)

**61.**
```sql
SELECT DISTINCT u.*
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE u.created_at >= DATE_SUB(CURDATE(), INTERVAL 30 DAY);
```

**62.**
```sql
SELECT p.name, SUM(oi.quantity * oi.price) AS total_revenue
FROM products p
JOIN order_items oi ON p.id = oi.product_id
GROUP BY p.id, p.name
ORDER BY total_revenue DESC
LIMIT 5;
```

**63.**
```sql
SELECT email, COUNT(*) AS count
FROM users
GROUP BY email
HAVING COUNT(*) > 1;
```

**64.**
```sql
WITH monthly_revenue AS (
    SELECT DATE_FORMAT(order_date, '%Y-%m') AS month, SUM(total) AS revenue
    FROM orders
    GROUP BY DATE_FORMAT(order_date, '%Y-%m')
)
SELECT month, revenue,
    LAG(revenue) OVER (ORDER BY month) AS prev_revenue,
    ROUND((revenue - LAG(revenue) OVER (ORDER BY month)) / LAG(revenue) OVER (ORDER BY month) * 100, 2) AS growth_rate
FROM monthly_revenue;
```

**65.**
```sql
SELECT * FROM orders
WHERE status = 'pending'
AND created_at < DATE_SUB(CURDATE(), INTERVAL 7 DAY);
```

**66.**
```sql
SELECT u.*
FROM users u
JOIN subscriptions s ON u.id = s.user_id
WHERE s.status = 'active'
AND u.last_login < DATE_SUB(CURDATE(), INTERVAL 90 DAY);
```

**67.**
```sql
SELECT product,
    MAX(CASE WHEN quarter = 'Q1' THEN amount END) AS Q1,
    MAX(CASE WHEN quarter = 'Q2' THEN amount END) AS Q2,
    MAX(CASE WHEN quarter = 'Q3' THEN amount END) AS Q3,
    MAX(CASE WHEN quarter = 'Q4' THEN amount END) AS Q4
FROM sales
GROUP BY product;
```

**68.**
```sql
WITH RECURSIVE subordinates AS (
    SELECT id, name, manager_id FROM employees WHERE id = ?
    UNION ALL
    SELECT e.id, e.name, e.manager_id
    FROM employees e
    JOIN subordinates s ON e.manager_id = s.id
)
SELECT * FROM subordinates WHERE id != ?;
```

**69.**
```sql
WITH ranked AS (
    SELECT user_id, login_date,
        DATE_SUB(login_date, INTERVAL ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY login_date) DAY) AS grp
    FROM user_logins
)
SELECT user_id, MIN(login_date) AS streak_start, MAX(login_date) AS streak_end, COUNT(*) AS streak_length
FROM ranked
GROUP BY user_id, grp
ORDER BY user_id, streak_start;
```

**70.**
```sql
SELECT order_date, total,
    SUM(total) OVER (ORDER BY order_date) AS running_total
FROM orders
ORDER BY order_date;
```

**71.**
```sql
SELECT MAX(salary) AS second_highest
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);
```

**72.**
```sql
DELETE u1 FROM users u1
JOIN users u2 ON u1.email = u2.email AND u1.id > u2.id;
```

**73.**
```sql
SELECT u.*
FROM users u
WHERE NOT EXISTS (
    SELECT p.id FROM products p
    WHERE p.category_id = ?
    AND NOT EXISTS (
        SELECT 1 FROM order_items oi
        JOIN orders o ON oi.order_id = o.id
        WHERE oi.product_id = p.id AND o.user_id = u.id
    )
);
```

**74.**
```sql
SELECT AVG(total) AS median
FROM (
    SELECT total, ROW_NUMBER() OVER (ORDER BY total) AS row_num, COUNT(*) OVER () AS total_rows
    FROM orders
) AS sorted
WHERE row_num IN (FLOOR((total_rows + 1) / 2), CEIL((total_rows + 1) / 2));
```

**75.** Enable slow query log, run `EXPLAIN ANALYZE`, check missing indexes, check table statistics, review fragmentation, review schema changes, check data volume growth.

**76.**
```sql
SELECT session_id, COUNT(DISTINCT page_url) AS pages_visited
FROM page_views
GROUP BY session_id
HAVING COUNT(DISTINCT page_url) > 3;
```

**77.**
```sql
SELECT o.*
FROM orders o
INNER JOIN (
    SELECT customer_id, MAX(order_date) AS latest_date
    FROM orders
    GROUP BY customer_id
) latest ON o.customer_id = latest.customer_id AND o.order_date = latest.latest_date;
```

**78.**
```sql
SELECT
    COUNT(DISTINCT o.user_id) * 100.0 / COUNT(DISTINCT u.id) AS purchase_percentage
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;
```

**79.**
```sql
SELECT p.*
FROM products p
LEFT JOIN order_items oi ON p.id = oi.product_id
WHERE oi.product_id IS NULL;
```

**80.**
```sql
SELECT AVG(DATEDIFF(second_order, first_order)) AS avg_days
FROM (
    SELECT user_id,
        MIN(order_date) AS first_order,
        MIN(CASE WHEN order_date > (SELECT MIN(order_date) FROM orders o2 WHERE o2.user_id = o1.user_id) THEN order_date END) AS second_order
    FROM orders o1
    GROUP BY user_id
    HAVING COUNT(*) >= 2
) user_orders;
```

**81.**
```sql
SELECT u.*
FROM users u
JOIN orders o ON u.id = o.user_id
GROUP BY u.id
HAVING SUM(o.total) > (SELECT AVG(total_spent) FROM (SELECT user_id, SUM(total) AS total_spent FROM orders GROUP BY user_id) avg_table);
```

**82.**
```sql
SELECT DISTINCT l1.user_id AS user1, l2.user_id AS user2, l1.ip_address
FROM login_history l1
JOIN login_history l2 ON l1.ip_address = l2.ip_address AND l1.user_id < l2.user_id;
```

**83.**
```sql
SELECT date, daily_revenue,
    AVG(daily_revenue) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS rolling_7day_avg
FROM (
    SELECT DATE(order_date) AS date, SUM(total) AS daily_revenue
    FROM orders
    GROUP BY DATE(order_date)
) daily
ORDER BY date;
```

**84.**
```sql
SELECT o.*
FROM orders o
JOIN addresses shipping ON o.shipping_address_id = shipping.id
JOIN addresses billing ON o.billing_address_id = billing.id
WHERE shipping.street != billing.street
   OR shipping.city != billing.city
   OR shipping.zip != billing.zip;
```

**85.**
```sql
SELECT error_message, COUNT(*) AS error_count
FROM error_logs
WHERE timestamp >= DATE_SUB(NOW(), INTERVAL 24 HOUR)
GROUP BY error_message
ORDER BY error_count DESC
LIMIT 3;
```

---

## Section 4: API Debugging (86–120)

**86.** Causes: expired token, invalid API key, missing auth header, incorrect credentials. Check headers, verify token expiry, test with fresh token, check auth service logs.

**87.** Causes: CORS, different auth headers, environment variables, browser caching, request interceptors. Check browser console, compare headers, verify CORS config.

**88.** Check error logs for patterns, check recent deployments, monitor resource usage, add request tracing, check for intermittent dependency failures.

**89.** Considerations: chunked upload, resumable uploads, timeout config, storage limits, progress tracking. Implement: multipart upload with chunks, presigned URLs for direct-to-S3 upload.

**90.** Check response time metrics, identify slow endpoint, run query analysis, check database performance, review code changes, check external dependencies, monitor server resources.

**91.** Causes: missing `Access-Control-Allow-Origin` header, preflight OPTIONS failing, credentials mode mismatch. Fix: configure CORS on server, handle OPTIONS, set proper headers.

**92.** Token lifecycle: access token (short-lived) + refresh token (long-lived). When access token expires, client sends refresh token to get new access token. Implement token endpoint with `grant_type=refresh_token`.

**93.** Headers: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`, `Retry-After`. Strategy: exponential backoff with jitter, respect `Retry-After`, request queuing.

**94.** Check webhook delivery logs, verify endpoint reachability, check SSL certificate, verify payload format, test with Postman, check for timeout issues.

**95.** Check for caching (CDN, browser, server), verify request headers, check for A/B testing, look at server-side routing, check load balancer config.

**96.** Document changes, provide migration guide, set up deprecation timeline, offer sandbox environment, provide support during transition, communicate via email and in-app.

**97.** Metrics: request rate, error rate, response time (p50, p95, p99), availability. Tools: Prometheus + Grafana, Datadog. Alerts: error rate > 1%, p95 > threshold, availability < 99.9%.

**98.** Causes: server overload, database slowness, network latency, DNS issues, firewall rules, connection pool exhaustion. Diagnose: traceroute, curl with timing, check server metrics, review logs.

**99.** Check service mesh logs, verify service discovery, check inter-service auth, review network policies, use distributed tracing, check certificate expiry.

**100.** Identify what changed in deployment, check deployment logs, compare request/response before and after, rollback if possible, fix forward if needed, communicate with customer.

**101.**
```javascript
const randomEmail = "user" + Math.random().toString(36).substring(7) + "@test.com";
pm.environment.set("randomEmail", randomEmail);
```

**102.** Steps: (a) Send Request A, (b) Add test script to extract value: `pm.environment.set("token", pm.response.json().token)`, (c) In Request B use `{{token}}` in headers/URL, (d) Chain requests in collection.

**103.** Possible causes: empty result set from database, serialization error returning empty body, response intercepted by middleware, database query timeout returning empty.

**104.** Tools: `clinic.js`, `node --inspect`, Chrome DevTools. Techniques: heap snapshots, monitor memory over time, check for unclosed connections/files, look for growing global caches, use `process.memoryUsage()`.

**105.** Causes: valid token but insufficient scopes/permissions, IP not whitelisted, user account disabled/suspended, token valid but endpoint requires different auth method.

**106.** Steps: (a) Create collection with request, (b) Create CSV/JSON data file with 100 rows, (c) Click collection `...` > `Run collection`, (d) Click `Select File` under Data, (e) Choose file, (f) Click `Run`.

**107.** Causes: request timeout too short, server payload size limit, memory limit on server, slow serialization. Fix: increase timeouts, stream large responses, use pagination, compress responses.

**108.** Approach: (a) Add logging to identify the race condition, (b) Check for shared mutable state, (c) Use async locks/mutexes for critical sections, (d) Use atomic operations, (e) Add integration tests that run concurrently.

**109.**
```javascript
pm.test("Response has correct types", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.id).to.be.a("number");
    pm.expect(jsonData.name).to.be.a("string");
    pm.expect(jsonData.email).to.be.a("string");
    pm.expect(jsonData.active).to.be.a("boolean");
});
```

**110.** Check CDN configuration, DNS resolution from that region, regional service health, latency from different locations, check if region has different firewall rules.

**111.** Common causes: expired certificate, mismatched domain name, missing intermediate certificate, clock skew. Fix: renew certificate, verify domain match, install intermediate certs, check system time.

**112.** Idempotency = same request produces same result if repeated. Implement: unique idempotency key per operation, store processed keys in database, return original result for duplicate keys.

**113.** Steps: Select `POST` > `Body` > `form-data` > Add key `file` > hover and select `File` type > Click `Select File` > Choose file > Send.

**114.** Likely race condition. Fix: use database transactions, implement optimistic locking with version column, use `SELECT ... FOR UPDATE`, add unique constraints.

**115.** Symptoms: connection timeouts, slow queries, "too many connections" errors. Fix: increase pool size, add connection timeout, implement connection retry, use connection pooling library, add monitoring.

**116.** Steps: Click gear icon > `Manage Environments` > `Add` > Name it (e.g., "Production") > Add variables (`baseUrl`, `token`, etc.) > `Save` > Repeat for each stage > Switch via dropdown.

**117.** Investigate: check if new certificate includes intermediate chain, verify certificate matches domain, check if old clients need backward compatibility, verify certificate format.

**118.** Common causes: missing CORS headers on OPTIONS response, authentication middleware blocking OPTIONS, custom middleware not handling OPTIONS. Fix: ensure OPTIONS requests bypass auth, return proper CORS headers on OPTIONS.

**119.** URL path (`/v1/users`): simple, visible in browser. Header (`Accept: application/vnd.api.v1+json`): clean URLs, but harder to test. Query parameter (`?version=v1`): easy to toggle, but less RESTful. Best practice: URL path for major versions.

**120.** Steps: Click `+` beside `Mock Servers` > Create mock server > Add example with status 200 and JSON body > Use mock server URL (`https://mockserverid.mock.pstmn.io`) as base URL.

---

## Section 5: Troubleshooting Scenarios (121–150)

**121.** Acknowledge and gather info, check if widespread or isolated, check monitoring dashboards, review recent deployments, check service health, reproduce if possible, implement fix, verify resolution, document and follow up.

**122.** Environment variables, database size/data, network/firewall rules, dependency versions, SSL certificates, caching state, external service endpoints, feature flags.

**123.** Ask about pattern, check logs during failure windows, monitor network latency, check resource exhaustion, set up continuous monitoring, use distributed tracing.

**124.** Verify what data is missing, check application logs, check database directly, look for accidental deletions, check backup availability, restore if possible.

**125.** Resource contention, scheduled jobs, connection pool exhaustion, caching not effective under load. Compare metrics peak vs off-peak, check connection pools, review cron jobs.

**126.** Gather all info from initial report, check logs and monitoring, try to reproduce in staging, escalate to engineering with detailed notes, document everything, follow up when available.

**127.** Empathize, acknowledge issues, escalate to engineering for priority fix, offer workarounds, provide timeline, consider goodwill gesture, follow up personally.

**128.** Acknowledge outage on status page, update every 30 minutes, communicate resolution, post-incident review within 48 hours. Channels: status page, email, social media, in-app.

**129.** Try different environments, ask for exact steps, check if environment-specific, ask for screen recording, check server logs for their account, request remote session.

**130.** Thank them for feedback, ask clarifying questions, document and share with product team, offer workarounds or training, follow up to see if suggestions help.

**131.** Possible causes: caching (browser, CDN, server), database replication lag, eventual consistency in distributed system, A/B testing flags.

**132.** Investigate: check memory usage during file processing, look for loading entire file into memory, check for memory leaks in parsing logic. Fix: stream files instead of loading entirely, increase memory limits, implement chunked processing.

**133.** Key differences: environment variables, dependency versions, file paths, OS differences, environment-specific configuration, missing secrets in CI, different timezone/locale settings.

**134.** Possible causes: external API changes, certificate expiry, DNS changes, dependency updates (auto-update), storage quota reached, scheduled job failure, third-party service outage.

**135.** Investigation: monitor connection count during peak, check connection pool settings, look for connection leaks (unclosed connections), check slow queries holding connections. Fix: increase pool size, add timeout, fix leaks, add monitoring.

**136.** Investigation: monitor memory over time, use memory profiler (`memory_profiler`), check for unclosed resources, look for growing data structures, check for circular references, take heap snapshots.

**137.** Possible causes: user-specific data conditions, cached auth tokens with different permissions, feature flags enabled/disabled per user, user-specific configuration, rate limiting per user.

**138.** Possible causes: database locks from concurrent runs, increased data volume, resource contention with other jobs, network latency to database, missing indexes on large tables.

**139.** Troubleshoot: check browser console for JS errors, test in private/incognito mode, clear cache, check caniuse.com for API support, verify polyfills, check Safari-specific CSS issues.

**140.** Steps: check backup integrity, verify backup is not corrupted, try restoring to different location, check disk space, verify database user permissions, check for incompatible database versions.

**141.** Investigation: check load balancer health, verify upstream servers, check error rate pattern, identify which requests fail, check for intermittent dependency failures, review recent changes.

**142.** Possible causes: frontend code triggers more API calls, new frontend uses different endpoints, CDN cache invalidation causing more origin hits, frontend deployment changed API interaction patterns.

**143.** Investigation: check email service queue, verify SMTP/API credentials, check for rate limiting from email provider, review email queue processor logs, check for bounced emails blocking queue.

**144.** `422 Unprocessable Entity` = server understands request but can't process due to semantic errors (validation failures, wrong data types). Help customer check: required fields present, correct data types, valid field values.

**145.** Steps: verify expiration, obtain new certificate from CA, install on server, update intermediate certificates, test HTTPS connection, set up auto-renewal (certbot), add monitoring alerts.

**146.** Possible causes: different connection string/credentials, different database user permissions, driver version differences, connection pooling issues, network/firewall differences, different timezone settings.

**147.** First checks: status page for known issues, recent deployments/changes, API version deprecation, customer's SSL certificate expiry, customer's IP whitelist, rate limit status on their account.

**148.** Investigation: monitor heap usage over time, use profiling tools, check for memory leaks in code, review recent deployments, take heap dumps during high memory, check for unbounded caches or queues.

**149.** Possible causes: shared rate limit across all users on their account, rate limit based on IP (multiple customers sharing IP), bug in rate limit counter, rate limit includes other API calls they made.

**150.** Immediate steps: (a) Isolate affected systems, (b) Revoke compromised credentials, (c) Assess scope of breach, (d) Preserve logs for forensics, (e) Notify affected users, (f) Patch vulnerability, (g) Engage security team, (h) Document timeline, (i) Post-incident review.

---

*End of Answer Key*
