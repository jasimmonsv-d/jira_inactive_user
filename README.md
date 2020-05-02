# Jira User Count v0.1.0

This program is a process to pull users who made changes in a defined time
period, and to compare that with the users in the Jira database and return
a file with users who made no changes within that defined timeframe.

## Requirements
* Python3
* DB access

## Getting Database data
[Jira Database Schema](https://developer.atlassian.com/server/jira/platform/database-schema)

User will need to retrieve data from the Jira data base from the `changegroup`
and the `cwd_user` tables.
`psql_command.txt` file contains commands for psql to run the queries and
save the results as required files for the Python3 script.

## Running script
Ensuring that the files are the same name as required in the `process.py`
file, running the script will quickly process the two files, resulting in
a `final_results.txt` file which will contain all users who have not made
changes to any Jira tickets since the defined date from the 
SQL query.

## Notes
This entire query could probably be ran as an SQL UNION statement, of some 
sort, but would require someone better in SQL then I had time for.