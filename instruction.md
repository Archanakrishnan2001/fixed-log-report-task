An Apache-style access log is at /app/access.log. Parse it and write a summary report to /app/report.json.

The report must be a JSON object with exactly these keys:
- total_requests: the total number of log lines, as an integer.
- unique_ips: the count of distinct client IP addresses, as an integer.
- top_path: the request path (e.g. "/index.html") that appears most often, as a string.

Success criteria:
1. /app/report.json exists and contains valid JSON.
2. total_requests equals the total number of lines in access.log.
3. unique_ips equals the number of distinct IP addresses found in access.log.
4. top_path equals the most frequently requested path in access.log.
