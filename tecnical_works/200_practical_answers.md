# 200 Practical Questions — Answer Key

## Section 1: API and Postman (1–40)

**1.** `200 OK` indicates success. `404 Not Found` means the requested resource does not exist on the server.

**2.** Steps: Open Postman → Click `+` for new tab → Select `GET` from dropdown → Enter URL `https://jsonplaceholder.typicode.com/users` → Click `Send`.

**3.** Query parameter: appears after `?` in URL (e.g., `?category=electronics`). Path parameter: part of the URL path itself (e.g., `/users/123` where `123` is the ID).

**4.** Steps: Open request → Click `Headers` tab → Enter `Content-Type` in Key column → Enter `application/json` in Value column.

**5.** POST creates a new resource. PUT updates/replaces an existing resource (idempotent).

**6.** Three causes: (a) Missing or invalid API key/token, (b) Expired authentication token, (c) Incorrect credentials (username/password).

**7.** Steps: Click `Save` button (or `Ctrl+S`) → Enter request name → Select or create a collection → Click `Save`.

**8.** JSON body: structured text format for sending data. Example:
```json
{
  "name": "John Doe",
  "email": "john@example.com"
}
```

**9.** In Postman, response time appears below the response body (bottom of response section) in milliseconds. Response size is shown next to it (e.g., "1.2 KB").

**10.** `Accept` header tells the server what content type the client can handle (e.g., `application/json`).

**11.** Query parameters: `category` = `electronics`, `limit` = `10`.

**12.** Steps: Click gear icon (top right) → `Manage Environments` → `Add` → Name it → Add variable `baseUrl` = `https://api.example.com` → `Save` → Select environment from dropdown (top right).

**13.** `400 Bad Request` means the server cannot process the request due to client error (e.g., malformed JSON, missing required field, invalid data type).

**14.** Steps: Click `Import` (top left) → Select `Raw text` tab → Paste cURL command → Click `Continue` → Click `Import`.

**15.** `200 OK` = request succeeded, resource returned. `201 Created` = request succeeded AND a new resource was created.

**16.** Steps: Click `...` on collection → `Run collection` → Configure iterations/delay → Click `Run [CollectionName]`.

**17.** Three checks: (a) Check server logs for stack trace, (b) Verify database connectivity, (c) Check if a recent deployment introduced a bug.

**18.** Pre-request script:
```javascript
pm.environment.set("timestamp", Math.floor(Date.now() / 1000));
```

**19.** Base URL: `https://api.example.com`, Version: `v2`, Resource: `orders`, Resource ID: `123`.

**20.** In Request A, add a test script:
```javascript
var jsonData = pm.response.json();
pm.environment.set("extractedId", jsonData.id);
```
In Request B, use URL: `{{baseUrl}}/users/{{extractedId}}`.

**21.** Authentication = verifying who you are (e.g., login with API key). Authorization = verifying what you can access (e.g., admin vs. user permissions).

**22.** Cause: missing or incorrect `Content-Type: application/json` header. Fix: add the header in Postman under Headers tab.

**23.** Test script:
```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});
```

**24.** Pagination splits large datasets into pages. Fetch all records by looping: request page 1, get `total`, calculate pages needed, loop through all pages.

**25.** Example: `{{baseUrl}}/users` — replace `{{baseUrl}}` with the environment variable defined in your environment.

**26.** Five causes: (a) Server overload/high CPU, (b) Slow database queries, (c) Network latency, (d) Large response payload, (e) Inefficient application code (e.g., N+1 queries).

**27.** Idempotency = same request produces same result if repeated. Idempotent methods: GET, PUT, DELETE. POST is not idempotent. Matters for retries — safe to retry idempotent requests.

**28.** Steps: Select request → `Authorization` tab → Select `Basic Auth` from dropdown → Enter username and password → Click `Send`.

**29.** Four reasons: (a) Different environment variables (staging vs. production), (b) CORS restrictions in browser, (c) Different authentication headers, (d) Browser caching or extensions interfering.

**30.** Use dynamic variables{{$randomEmail}}` or pre-request script:
```javascript
const randomEmail = "user" + Math.random().toString(36).substring(7) + "@test.com";
pm.environment.set("randomEmail", randomEmail);
```

**31.** Collection structure: `E-Commerce API` folder with subfolders `Products`. Each request includes tests validating status code, response time, and key response fields. Example: Create Product (POST) with test checking 201 status and returned ID.

**32.** Troubleshooting steps: (a) Check load balancer health, (b) Verify upstream servers are running, (c) Check error logs on load balancer, (d) Verify DNS resolution, (e) Check firewall rules, (f) Test upstream servers directly.

**33.** Schema validation test:
```javascript
pm.test("Response schema is valid", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.id).to.be.a("number");
    pm.expect(jsonData.name).to.be.a("string");
    pm.expect(jsonData.email).to.include("@");
});
```

**34.** CORS = Cross-Origin Resource Sharing. Cause: server doesn't include `Access-Control-Allow-Origin` header. Fix: configure server/API gateway to allow the requesting origin.

**35.** Workflow: Request A (login) → extract token to `{{token}}` → Request B (create user using `{{token}}` and `{{baseUrl}}`) → extract `userId` to `{{userId}}` → Request C (get user using `{{userId}}`).

**36.** Steps: Select `POST` → `Body` tab → Select `form-data` → Add key `file`, hover over key, select `File` type from dropdown → Click `Select File` → Choose file → Send.

**37.** Rate limiting = restricting number of requests per time window. Strategies: (a) Implement exponential backoff in client, (b) Use request queuing, (c) Cache responses to reduce API calls, (d) Upgrade to higher rate limit tier.

**38.** Steps: Click `+` beside `Mock Servers` (left sidebar) → Create mock server → Add example response with status 200 and JSON body containing 3 users → Use mock server URL instead of real API URL.

**39.** OAuth refresh flow: when access token expires, client sends refresh token to `/oauth/token` endpoint with `grant_type=refresh_token`, receives new access token. In Postman: use `Authorization` tab → `OAuth 2.0` → configure token URL, client credentials, and refresh token URL.

**40.** Security issue: sensitive data exposure. Fix: (a) Remove password field from API response, (b) Use DTOs/serializers to control response fields, (c) Hash passwords (never store plain text), (d) Audit other endpoints for similar issues.

---

## Section 2: SQL and MySQL (41–80)

**41.** `SELECT * FROM customers;`

**42.** `WHERE` filters rows before grouping/aggregation. `HAVING` filters groups after `GROUP BY`.

**43.**
```sql
SELECT * FROM customers WHERE city = 'New York';
```

**44.**
```sql
INSERT INTO products (name, price) VALUES ('Laptop', 999.99);
```

**45.** Primary key uniquely identifies each row. It cannot be NULL and must be unique.

**46.**
```sql
UPDATE customers SET email = 'newemail@example.com' WHERE id = 5;
```

**47.** Deletes the row with `id = 10`. Without `WHERE`, deletes ALL rows.

**48.** `INNER JOIN` returns only matching rows from both tables. `LEFT JOIN` returns all rows from left table, with NULLs for non-matching right table rows.

**49.**
```sql
SELECT COUNT(*) FROM orders;
```

**50.**
```sql
SELECT * FROM products ORDER BY price DESC;
```

**51.**
```sql
SELECT * FROM customers WHERE name LIKE 'A%';
```

**52.** `COUNT(*)` counts all rows including NULLs. `COUNT(column_name)` counts only non-NULL values in that column.

**53.**
```sql
SELECT DISTINCT country FROM customers;
```

**54.** Limits number of returned rows.
```sql
SELECT * FROM logs LIMIT 10;
```

**55.** Press `Win + R` → type `cmd` → Enter → type `mysql -u username -p` → Enter → enter password.

**56.**
```sql
SELECT orders.id, customers.name
FROM orders
INNER JOIN customers ON orders.customer_id = customers.id;
```

**57.** Foreign key links a column to a primary key in another table. Enforces referential integrity — prevents orphaned records and invalid references.

**58.**
```sql
SELECT c.name, SUM(oi.quantity * oi.price) AS total_sales
FROM customers c
JOIN orders o ON c.id = o.customer_id
JOIN order_items oi ON o.id = oi.order_id
GROUP BY c.id, c.name;
```

**59.** `UNION` removes duplicate rows. `UNION ALL` keeps all rows including duplicates.

**60.**
```sql
SELECT c.*
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
WHERE o.id IS NULL;
```

**61.** An index speeds up read queries at cost of slower writes and extra storage.
```sql
CREATE INDEX idx_email ON customers(email);
```

**62.**
```sql
SELECT MAX(salary) AS second_highest
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);
```

**63.** Groups rows by a column value and applies aggregate functions.
```sql
SELECT status, COUNT(*) AS order_count
FROM orders
GROUP BY status;
```

**64.** Steps: Open MySQL Workbench → Connect to server → Click `Create new schema` icon (database with +) → Enter name → `Apply` → `Apply` → `Finish`.

**65.**
```sql
DELETE u1 FROM users u1
INNER JOIN users u2
WHERE u1.email = u2.email AND u1.id > u2.id;
```

**66.**
```sql
SELECT name,
    CASE
        WHEN price > 100 THEN 'Expensive'
        ELSE 'Cheap'
    END AS category
FROM products;
```

**67.**
```sql
SELECT * FROM orders
WHERE order_date >= DATE_SUB(CURDATE(), INTERVAL 7 DAY);
```

**68.** `CHAR(n)` — fixed-length, pads with spaces. `VARCHAR(n)` — variable-length, stores only actual data.

**69.** Steps: Connect in Workbench → Right-click table → `Table Data Export Wizard` → Select CSV → Choose path → `Next` → `Finish`.

**70.**
```sql
SELECT MONTH(order_date) AS month, AVG(total_amount) AS avg_order_value
FROM orders
WHERE YEAR(order_date) = YEAR(CURDATE())
GROUP BY MONTH(order_date)
ORDER BY month;
```

**71.**
```sql
SELECT c.name, SUM(oi.quantity * oi.price) AS total_spent
FROM customers c
JOIN orders o ON c.id = o.customer_id
JOIN order_items oi ON o.id = oi.order_id
GROUP BY c.id, c.name
ORDER BY total_spent DESC
LIMIT 3;
```

**72.**
```sql
START TRANSACTION;

UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

IF (SELECT balance FROM accounts WHERE id = 1) < 0 THEN
    ROLLBACK;
ELSE
    COMMIT;
END IF;
```

**73.** `DELETE` — removes rows one by one, can use WHERE, triggers fire, rollback possible. `TRUNCATE` — removes all rows quickly, resets auto-increment, cannot use WHERE, minimal logging. `DROP` — removes entire table and structure.

**74.**
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

**75.**
```sql
SELECT * FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

**76.** Command line: `mysql -u root -p` → `CREATE USER 'readonly'@'%' IDENTIFIED BY 'password';` → `GRANT SELECT ON dbname.* TO 'readonly'@'%';` → `FLUSH PRIVILEGES;`

**77.**
```sql
SELECT product,
    MAX(CASE WHEN quarter = 'Q1' THEN amount END) AS Q1,
    MAX(CASE WHEN quarter = 'Q2' THEN amount END) AS Q2,
    MAX(CASE WHEN quarter = 'Q3' THEN amount END) AS Q3,
    MAX(CASE WHEN quarter = 'Q4' THEN amount END) AS Q4
FROM sales
GROUP BY product;
```

**78.** Deadlock = two or more transactions waiting on each other's locks. Detect: `SHOW ENGINE INNODB STATUS;` — shows latest deadlock. Resolve: optimize queries, use consistent lock ordering, reduce transaction size, add indexes to reduce lock scope.

**79.**
```sql
WITH RECURSIVE subordinates AS (
    SELECT id, name, manager_id FROM employees WHERE id = 1
    UNION ALL
    SELECT e.id, e.name, e.manager_id
    FROM employees e
    INNER JOIN subordinates s ON e.manager_id = s.id
)
SELECT * FROM subordinates WHERE id != 1;
```

**80.** Process: (a) Enable slow query log, (b) Identify slow queries, (c) Run `EXPLAIN ANALYZE` on the query, (d) Check for missing indexes, (e) Check for full table scans, (f) Look for inefficient joins, (g) Optimize query structure, (h) Add/adjust indexes, (i) Consider query caching, (j) Monitor after changes.

---

## Section 3: Python Debugging (81–120)

**81.** Missing colon after function definition.
```python
def greet(name):
    print("Hello, " + name)
```

**82.** `IndexError: list index out of range` — index 5 doesn't exist in a 5-element list (valid indices: 0–4).

**83.** Assignment `=` used instead of comparison `==`.
```python
x = 10
if x == 10:
    print("x is 10")
```

**84.** Function subtracts instead of adds.
```python
def add(a, b):
    return a + b
```

**95.** Infinite loop — appending to list while iterating over it.
```python
numbers = [1, 2, 3, 4, 5]
for i in numbers.copy():
    print(numbers[i])
    numbers.append(i)
```

**86.** `input()` returns a string. Can't compare string with integer.
```python
age = int(input("Enter your age: "))
if age >= 18:
    print("Adult")
```

**87.** `ZeroDivisionError`. Handle with try/except or check for zero.
```python
def divide(a, b):
    if b == 0:
        return None
    return a / b
```

**88.** `IndexError: string index out of range` — string length is 11, valid indices 0–10, index 10 is the last character 'd'.

**89.** `KeyError: 'email'` — key doesn't exist. Use `.get()` method.
```python
print(my_dict.get("email", "No email"))
```

**90.** `ValueError: math domain error`. Handle negative input.
```python
import math
import cmath
result = cmath.sqrt(-1)
```

**91.** Infinite recursion — function calls itself with same argument.
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

**92.** `TypeError: unsupported operand type(s) for +: 'int' and 'str'`.
```python
x = 5
y = "10"
print(x + int(y))
```

**93.** Missing colon after `for` statement.
```python
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(total)
```

**94.** Assignment `=` instead of comparison `==`.
```python
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
```

**95.** File not closed — resource leak. Use `with` statement.
```python
with open("data.txt", "r") as file:
    content = file.read()
print(content)
```

**96.** Mutable default argument — `my_list` persists across calls.
```python
def append_to_list(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list
```

**97.** Withdrawal allowed even with insufficient funds — balance goes negative.
```python
def withdraw(self, amount):
    if amount > self.balance:
        raise ValueError("Insufficient funds")
    self.balance -= amount
    return self.balance
```

**98.** `KeyError` if `email` doesn't exist in response. Handle gracefully.
```python
print(parsed.get("email", "Email not provided"))
```

**99.** `ZeroDivisionError` when list is empty.
```python
def get_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
```

**100.** `NameError: name 'result' is not defined` in `finally` if exception occurs before assignment.
```python
result = None
try:
    result = 10 / 0
except ZeroDivisionError:
    result = None
finally:
    print("Result is: " + str(result))
```

**101.** `NameError: name 'result' is not defined` — `result` is local to `process_data`, not accessible outside.
```python
result = process_data(numbers)
print(len(result))
```

**102.** No error handling for network failures or invalid JSON.
```python
import requests
try:
    response = requests.get("https://api.example.com/users")
    response.raise_for_state()
    data = response.json()
    for user in data:
        print(user["name"])
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
except (ValueError, KeyError) as e:
    print(f"Data error: {e}")
```

**103.** Logic error — compares each element with every element including itself, producing duplicates.
```python
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return list(duplicates)
```

**104.** `TypeError: 'tuple' object does not support item assignment` — tuples are immutable.

**105.** Infinite loop — if `n` is negative or zero, loop never executes (not technically a bug for negative input, but no guard).
```python
def countdown(n):
    if n <= 0:
        print("Invalid input")
        return
    while n > 0:
        print(n)
        n = n - 1
```

**106.** `upper()` returns a new string; original is unchanged.
```python
text = "hello world"
text = text.upper()
print(text)
```

**107.** `c` is `[1, 2, 3, 4, 5]` — `a.append(7)` doesn't affect `c` because `+` creates a new list.

**108.** Danger: permanently deletes files without confirmation. Add safety checks.
```python
import os
files = os.listdir(".")
for file in files:
    if file.endswith(".txt"):
        confirm = input(f"Delete {file}? (y/n): ")
        if confirm.lower() == "y":
            os.remove(file)
            print(f"Deleted {file}")
```

**109.** Missing special character check.
```python
def validate_password(password):
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        return False
    return True
```

**110.** `IndexError: pop from empty stack` — no check for empty stack.
```python
def pop(self):
    if self.is_empty():
        raise IndexError("Stack is empty")
    return self.items.pop()
```

**111.** Race condition — `counter += 1` is not atomic. Multiple threads overwrite each other's changes.
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

**112.** `RecursionError` — default recursion limit (~1000) exceeded for `fibonacci(100)`. Use iterative approach or `functools.lru_cache`.
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

**113.** `TypeError: Object of type User is not JSON serializable`.
```python
def to_json(self):
    return json.dumps({"name": self.name, "age": self.age})
```

**114.** `IndexError` if file has fewer than 101 lines. Also `FileNotFoundError`.
```python
try:
    with open("data.txt", "r") as f:
        lines = f.readlines()
    processed = [line.strip().upper() for line in lines]
    if len(processed) > 100:
        print(processed[100])
    else:
        print("File has fewer than 101 lines")
except FileNotFoundError:
    print("File not found")
```

**115.** `AttributeError: 'NoneType' object has no attribute 'value'` — when list is empty, `self.head` is `None`.
```python
def remove(self, value):
    if self.head is None:
        return
    if self.head.value == value:
        self.head = self.head.next
        return
    current = self.head
    while current.next:
        if current.next.value == value:
            current.next = current.next.next
            return
        current = current.next
```

**116.** Regex doesn't handle dots in domain (e.g., `name@sub.domain.com`), plus signs, or hyphens. Improved:
```python
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
```

**117.** Integer overflow in `(low + high) // 2` for very large arrays. Fix: `low + (high - low) // 2`.

**118.** SQL Injection vulnerability. Fix with parameterized queries:
```python
def get_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result
```

**119.** No backoff between retries — hammers the service. Add delay:
```python
import time

def retry(func, max_retries=3, backoff=1):
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            time.sleep(backoff * (2 ** attempt))
```

**120.** Requests run sequentially — total time ~5s instead of ~1s.
```python
async def main():
    urls = ["url1", "url2", "url3", "url4", "url5"]
    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results
```

---

## Section 4: Troubleshooting & Root Cause (121–150)

**121.** Five checks: (a) Is the server running? (b) Can you ping/curl the website? (c) Check browser console for errors, (d) Check DNS resolution, (e) Check if other websites load (internet connectivity).

**122.** Questions: What endpoint? What error message/status code? When did it start? Is it consistent or intermittent? What changed recently? Can you share the request/response?

**123.** Three investigations: (a) Check application logs/crash dumps, (b) Verify system requirements and dependencies, (c) Check recent changes (updates, config changes, new installations).

**124.** Troubleshooting = identifying and fixing the immediate issue. Root cause analysis = investigating WHY the issue occurred to prevent recurrence.

**125.** Four causes: (a) Server overload, (b) Large unoptimized images/assets, (c) Slow database queries, (d) Network issues (DNS, CDN, bandwidth).

**126.** Steps: (a) Verify with customer what data is missing, (b) Check application logs around the time, (c) Check database directly, (d) Check for accidental deletions or failed migrations, (e) Check backup availability.

**127.** A log file records application events. On Windows: typically in `C:\ProgramData\ApplicationName\logs\` or `C:\Users\{user}\AppData\Local\ApplicationName\logs\`.

**128.** "Connection refused" means nothing is listening on the target port. Check: (a) Is the server running? (b) Is the port correct? (c) Is a firewall blocking? (d) Is the IP/hostname correct?

**129.** Ask "why" five times to drill from symptom to root cause. Example: Slow query → why? Full table scan → why? No index → why? New column added without index → why? Migration didn't include index → why? No review process for schema changes.

**130.** Three causes: (a) Email service/API key expired or misconfigured, (b) Notifications disabled in database/settings, (c) Emails being caught by spam filters or bounced.

**131.** Possible causes: browser-specific JS errors, unsupported APIs, CSS compatibility, cached old version. Troubleshoot: check browser console, test in incognito, clear cache, check caniuse.com for API support.

**132.** Steps: (a) Check disk space with `df -h` or Windows Explorer, (b) Identify largest tables/files, (c) Check for unpurged logs or temporary files, (d) Delete unnecessary data, (e) Add archiving strategy, (f) Alert before reaching threshold.

**133.** Possible causes: (a) Request timeout too short for large payloads, (b) Server memory limit exceeded, (c) Payload size limit on server/load balancer, (d) Database query not optimized for large datasets.

**134.** Steps: (a) Ask about pattern (time of day, specific actions), (b) Check logs during failure windows, (c) Monitor network latency and packet loss, (d) Check for resource exhaustion, (e) Set up continuous monitoring.

**135.** Process: (a) Acknowledge incident, (b) Assess severity and impact, (c) Communicate to stakeholders, (d) Roll back deployment if possible, (e) Verify fix, (f) Document timeline, (g) Conduct post-mortem.

**136.** Likely memory leak. Investigate: (a) Monitor memory usage over time, (b) Use profiling tool (e.g., `memory_profiler`), (c) Check for unclosed connections/files, (d) Look for growing data structures without cleanup, (e) Check for circular references.

**137.** Possible causes: (a) CDN not configured or misconfigured for external regions, (b) Firewall rules affecting external traffic, (c) DNS resolution differences, (d) Different SSL certificate issues for external domains.

**138.** Steps: (a) Verify expiration date, (b) Obtain new certificate from CA, (c) Install new certificate on server, (d) Update any intermediate certificates, (e) Test HTTPS connection, (f) Set up renewal reminders.

**139.** Steps: (a) Check service's own logs and metrics, (b) Check downstream dependency health, (c) Run distributed trace (e.g., Jaeger, Zipkin), (d) Check network latency between services, (e) Review recent deployments to each component.

**140.** Five checks: (a) Check backup job logs for error message, (b) Verify disk space on backup destination, (c) Check network connectivity to backup storage, (d) Verify credentials haven't expired, (e) Check if backup schedule conflicts with other jobs.

**141.** Analysis: (a) Enable `innodb_print_all_deadlocks`, (b) Check `SHOW ENGINE INNODB STATUS`, (c) Identify the two conflicting queries, (d) Analyze lock order, (e) Rewrite queries to use consistent ordering, (f) Add appropriate indexes, (g) Reduce transaction size.

**142.** Likely causes: (a) Resource contention during peak hours, (b) Scheduled jobs competing for resources, (c) Connection pool exhaustion, (d) Caching not effective under load. Investigate: compare metrics at 3 PM vs. 3 AM, check connection pool usage, review cron/scheduled tasks.

**143.** Approach: (a) Correlate timestamps across all service logs, (b) Check metrics dashboards for anomaly timing, (c) Trace a failing request across all services, (d) Look for common dependency (database, cache, message queue), (e) Check infrastructure events (deploys, scaling, network changes).

**144.** Process: (a) Identify which system is source of truth, (b) Query both systems for specific discrepancy, (c) Check sync job logs, (d) Look for failed sync attempts, (e) Check for race conditions or ordering issues, (f) Verify network connectivity between systems.

**145.** Confirm: (a) Use `tracemalloc` or `memory_profiler` to track allocations, (b) Take memory snapshots at intervals, (c) Compare snapshots to find growing objects, (d) Check for unclosed resources, (e) Look for global caches without eviction, (f) Use `objgraph` to find reference cycles.

**146.** Investigation: (a) Identify what changed in deployment, (b) Diff config files, (c) Check for connection pool changes, (d) Query performance analysis (`EXPLAIN`), (e) Check if new code path introduces N+1 queries, (f) Rollback and verify performance returns to baseline.

**147.** Possible causes: (a) Sticky sessions routing unevenly, (b) Health checks failing on some servers, (c) Different server capacities, (d) DNS caching issues. Fix: verify health check config, check server weights, review load balancing algorithm.

**148.** Key differences: (a) Environment variables/config, (b) Database size and data, (c) Network/firewall rules, (d) Dependency versions, (e) SSL certificates, (f) Caching state, (g) External service endpoints.

**149.** Process: (a) Run `EXPLAIN ANALYZE`, (b) Check if indexes exist on WHERE/JOIN columns, (c) Look for full table scans, (d) Check table statistics are up to date (`ANALYZE TABLE`), (e) Review query structure for unnecessary operations, (f) Check for table fragmentation, (g) Consider adding composite indexes.

**150.** Cascading failure = one failure triggers failures in dependent services. Identify: trace the origin (usually the deepest dependency). Prevent: implement circuit breakers, bulkheads, timeouts, graceful degradation, and retries with backoff.

---

## Section 5: Customer Support & Communication (151–175)

**151.** Three things: (a) Listen actively and acknowledge their frustration, (b) Apologize for the inconvenience, (c) Focus on solving the problem — take ownership.

**152.** Bug = software behaves incorrectly/unexpectedly. Feature request = customer wants new functionality that doesn't exist.

**153.** Questions: What were you trying to do? What happened instead? What error message do you see? When did this start? Has it worked before? What browser/version are you using? Can you share a screenshot?

**154.** Use analogies and avoid jargon. Example: "Think of the API like a waiter — your app sends an order (request), the kitchen (server) prepares it, and the waiter brings back your food (response). Right now the kitchen doesn't understand the order format, so we need to adjust how your app sends it."

**155.** Respond: "I understand this would be helpful. While this is currently a design limitation, I'll document your feedback and share it with our product team. In the meantime, here's a workaround you can use..."

**156.** SLA = Service Level Agreement — contract defining expected support response/resolution times. Important because it sets expectations, ensures accountability, and prioritizes work.

**157.** Response: "I'm sorry to hear you're experiencing an issue. To help you quickly, could you provide: (1) what you were trying to accomplish, (2) what happened instead, (3) any error messages, (4) your browser/operating system?"

**158.** Respond: "Thank you for the suggestion. I understand this feature would help your workflow. I'll submit this to our product team for consideration. In the meantime, is there an alternative approach I can help with?"

**159.** Best practice: be proactive — notify customers before they discover it, be transparent about cause and impact, provide workarounds, give regular updates, and share resolution timeline.

**160.** Steps: (a) Try different browsers/devices, (b) Ask for exact steps to reproduce, (c) Check if issue is environment-specific, (d) Ask for screen recording, (e) Check server-side logs for their account, (f) Request remote session if possible.

**161.** Steps: (a) Gather all info from initial report, (b) Check logs and monitoring data, (c) Try to reproduce in staging, (d) Escalate to engineering with detailed notes, (e) Document everything, (f) Follow up when customer is available.

**162.** Factors: (a) Severity (data loss > crash > cosmetic), (b) Number of users affected, (c) SLA commitments, (d) Business impact, (e) Complexity/effort required.

**163.** Steps: (a) Stay professional and don't take it personally, (b) Document everything you've done, (c) Summarize findings clearly for manager, (d) Continue working on resolution, (e) Learn from feedback.

**164.** Communicate tactfully: "I found the issue — it looks like [specific configuration/usage] is causing this. Let me walk you through how to adjust it so it works correctly." Focus on education, not blame.

**165.** Immediate steps: (a) Assess scope and cause, (b) Restore from backup if available, (c) Communicate transparently: what happened, what data can be recovered, what's the timeline, (d) Provide regular updates, (e) Conduct root cause analysis to prevent recurrence.

**166.** Essential elements: (a) Clear title, (b) Environment details, (c) Steps to reproduce, (d) Expected behavior, (e) Actual behavior, (f) Screenshots/logs, (g) Severity/priority, (h) Contact info.

**167.** Steps: (a) Listen to their concerns, (b) Re-examine the issue with fresh eyes, (c) Escalate to senior support or engineering if needed, (d) Offer alternative solutions, (e) Follow up to ensure satisfaction.

**168.** Say: "I don't have that information right now, but I'll find out and get back to you by [specific time]." Then escalate to documentation, engineering, or senior team members.

**169.** Steps: (a) Post on status page, (b) Send email to affected users, (c) In-app notification if applicable, (d) Provide timeline and workaround, (e) Send resolution confirmation.

**170.** Include: (a) Issue summary, (b) Root cause, (c) Steps to resolve, (d) Prevention measures, (e) Date resolved, (f) Resolved by, (g) Related tickets.

**171.** Communication plan: (a) Immediate: acknowledge outage on status page, (b) Every 30 min: progress update, (c) Resolution: confirm fix and summarize cause, (d) Post-incident: publish post-mortem within 48 hours. Channels: status page, email, social media, in-app banners.

**172.** Steps: (a) Empathize with their frustration, (b) Acknowledge the ongoing issues, (c) Escalate to engineering for priority fix, (d) Offer temporary workarounds, (e) Provide timeline for permanent fix, (f) Consider goodwill gesture (discount, extended trial), (g) Follow up personally.

**173.** Communication: (a) 60 days before: initial notice via email + in-app, (b) 30 days: reminder with migration guide, (c) 7 days: final warning, (d) Day of: disable old endpoint. Include: reason for change, benefits, migration guide, support contact.

**174.** Steps: (a) Acknowledge receipt, (b) Ask them not to share publicly yet, (c) Escalate to security team immediately, (d) Investigate and validate, (e) Fix the vulnerability, (f) Notify customer of fix, (g) Coordinate disclosure timeline.

**175.** Handling: (a) Thank them for honest feedback, (b) Ask clarifying questions about specific pain points, (c) Document and share with product team, (d) Offer immediate workarounds or training, (e) Follow up to see if suggestions help.

---

## Section 6: JavaScript Basics (176–200)

**176.** `var` — function-scoped, hoisted, can redeclare. `let` — block-scoped, not hoisted, cannot redeclare. `const` — block-scoped, not hoisted, cannot redeclare or reassign (but object properties can be modified).

**177.** Subtracts instead of adds.
```javascript
function add(a, b) {
    return a + b;
}
```

**178.** `==` coerces types before comparison. `===` checks type AND value. Example: `5 == "5"` is `true`, `5 === "5"` is `false`.

**179.** Output: `undefined` — array has 5 elements (indices 0–4), index 5 doesn't exist.

**180.** A function passed as an argument to be executed later. Example:
```javascript
setTimeout(function() {
    console.log("Executed after 1 second");
}, 1000);
```

**181.** Assignment `=` instead of comparison `===`. Condition always truthy.
```javascript
let x = 10;
if (x === 5) {
    console.log("x is 5");
}
```

**182.** `null` = intentional absence of value (developer sets it). `undefined` = variable declared but never assigned, or property doesn't exist.

**183.** Output: `undefined`. Safe access:
```javascript
console.log(user.email || "No email");
```

**184.** Converts JSON string to JavaScript object. Throws `SyntaxError` on invalid JSON. Use try/catch:
```javascript
try {
    const obj = JSON.parse(jsonString);
} catch (e) {
    console.log("Invalid JSON");
}
```

**185.** Output: `5, 5, 5` — `var` is function-scoped, single `i` shared. Fix:
```javascript
for (let i = 0; i < 5; i++) {
    setTimeout(function() {
        console.log(i);
    }, 1000);
}
```

**186.** Missing `return` in map callback — returns `undefined` for each element.
```javascript
const result = arr.map(function(num) {
    return num * 2;
});
```

**187.** Promise = object representing eventual completion/failure of async operation.
```javascript
const promise = new Promise((resolve, reject) => {
    setTimeout(() => resolve("Done"), 1000);
});
promise.then(result => console.log(result));
```

**188.** Missing `await` on `response.json()` (which returns a Promise).
```javascript
async function fetchUser(id) {
    const response = await fetch(`/api/users/${id}`);
    const data = await response.json();
    return data;
}
```

**189.** `forEach` — executes function for each element, returns `undefined`, used for side effects. `map` — transforms each element, returns new array. Use `forEach` when you don't need a new array; `map` when you do.

**190.** Output: `Hello, undefined` — `this` context is lost when function is detached from object. Fix:
```javascript
const greet = obj.greet.bind(obj);
```
Or use arrow function:
```javascript
const greet = () => obj.greet();
```

**191.** Event delegation = attaching event listener to parent element, using event bubbling to handle events on children. Use when: many similar elements need same handler, or elements are dynamically added/removed.

**192.** `typeof null` → `"object"` (historical bug in JS). `null instanceof Object` → `false`. `null` is not an instance of `Object` despite `typeof` saying "object".

**193.** Spread operator `...` expands iterable into individual elements.
```javascript
const arr1 = [1, 2];
const arr2 = [...arr1, 3, 4];

const obj1 = { a: 1 };
const obj2 = { ...obj1, b: 2 };
```

**194.** `ReferenceError: d is not defined` — destructured 3 elements into 3 variables, `d` doesn't exist.

**195.** `localStorage` — persists until explicitly cleared, survives browser restart. `sessionStorage` — cleared when tab/browser session ends.

**196.** Output: `2, 0` — each `createCounter()` call creates a new closure with its own `count`. `counter1` and `counter2` have independent counters.

**197.** Output: `[1, 2, 3]` after ~1.5s (slowest promise). If one rejects, `Promise.all` immediately rejects with that error.

**198.** First `dog.speak()` → `"Rex barks"`. After `delete dog.speak`, second call → `"Rex makes a sound"` — `delete` removed the own property, so lookup goes to `Animal.prototype`.

**199.** Issue: `for...in` iterates over inherited enumerable properties. Fix:
```javascript
for (let key in obj) {
    if (obj.hasOwnProperty(key)) {
        console.log(key, obj[key]);
    }
}
```
Or use `Object.keys(obj).forEach(...)`.

**200.** Output: `"Operation executed"` printed once, 1s after last call. Debouncing delays execution until calls stop for the specified delay. Debounce: executes only once after calls stop (good for search input). Throttle: executes at most once per interval (good for scroll/resize events).

---

*End of Answer Key*
