#Issue Summary
#Duration:

Start: June 7, 2024, 10:30 AM UTC
End: June 7, 2024, 12:00 PM UTC
#Impact:

Our e-commerce platform was down, preventing users from accessing the website and completing purchases. Approximately 80% of users were affected, resulting in an estimated revenue loss of $15,000.
Root Cause:

A misconfigured database index led to a severe degradation in database query performance, causing the web servers to timeout.
#Timeline
10:30 AM: Issue detected by monitoring alert indicating increased response times and error rates.
10:32 AM: On-call engineer notified via PagerDuty.
10:35 AM: Initial investigation started focusing on recent code deployments.
10:45 AM: Assumed root cause to be a recently deployed feature; feature rollback initiated.
11:00 AM: Rollback completed; no improvement in system performance.
11:10 AM: Database performance metrics analyzed; significant query delays identified.
11:20 AM: Database team engaged to assist with the investigation.
11:35 AM: Identified a missing index on a frequently queried table.
11:50 AM: Index created on the problematic table.
12:00 PM: System performance restored; monitoring confirms normal operation.
#Root Cause and Resolution
#Root Cause:

The issue was caused by a missing index on a database table that experienced a high volume of queries. A recent increase in traffic exacerbated the problem, leading to prolonged query execution times and eventually causing web server timeouts.
#Resolution:

The database team created the necessary index on the problematic table, which immediately improved query performance. The application servers were then able to handle requests within acceptable timeframes, restoring normal service.
Corrective and Preventative Measures
#Improvements/Fixes:

Database Index Monitoring: Implement monitoring for missing or suboptimal database indexes.
Performance Testing: Conduct regular performance testing to identify potential bottlenecks under increased load.
Pre-deployment Checks: Enhance pre-deployment checks to include database index verification.
#Tasks:

Task 1: Implement a script to periodically check for missing indexes and alert the database team. Due: June 15, 2024
Task 2: Set up a performance testing environment that simulates high traffic scenarios to identify and address potential performance issues. Due: June 20, 2024
Task 3: Update deployment pipeline to include automated checks for database indexes before pushing new code to production. Due: June 25, 2024
