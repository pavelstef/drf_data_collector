# drf_data_collector

Simple Python project: Django(DRF) , JSON output, XLSX output

Superuser: admin\admin

API Information:
+ GET <server_ip:port>/api/v1/docs - Automatically generated API documentation

+ GET <server_ip:port>/api/v1/management - Getting the current number of records in the database
+ POST <server_ip:port>/api/v1/management - Download data from an external source and create records in the database

+ GET <server_ip:port>/api/v1/json/greetings - Getting the data list as a JSON
+ GET <server_ip:port>/api/v1/json/greetings?limit=100 - Getting the first 100 entries as a JSON
+ GET <server_ip:port>/api/v1/json/greetings/14396 - Retrieving the record with ID = 14396 as a JSON
+ GET <server_ip:port>/api/v1/json/greetings/2012-01-30 - Retrieving one or a few records with "thedate" = 2012-01-30 as a JSON

+ GET <server_ip:port>/api/v1/xlsx/greetings - Getting the data list as a XLSX
+ GET <server_ip:port>/api/v1/xlsx/greetings?limit=100 - Getting the first 100 entries as a XLSX
+ GET <server_ip:port>/api/v1/xlsx/greetings/14396 - Retrieving the record with ID = 14396 as a XLSX
+ GET <server_ip:port>/api/v1/xlsx/greetings/2012-01-30 - Retrieving one or a few records with "thedate" = 2012-01-30 as a XLSX
