UCLA project

Database steps (Part 1 and 2):
1. Create programming_assignment_db schema (username: adriana password: abc123
2. Run SQL script provided with assignment to create and fill the tables (includes null values)
3. Open cmd and run fill_users_table.py that will call API and fill missing values in table columns
4. The tables will now contain missing values

Build Commenter's Excel Report (Part 3):
1. Run v_users_commenters.sql to create a view that will be used to pull data for excel report and subsequent API.
2. Once the view has been created, run f_distance.sql script that will create a function that calculates distance between two points (using longitude and latitude)
3. Open cmd and run build_commenters_report.py that will build excel report called FrequentCommenterReport.xlsx in the directory

Build and Test API (Part 4)
1. Install pip flask (in not already installed - python)
2. Open cmd and run api.py using PostMan (or another Soap ui)
3. For id search e.g. http://127.0.0.1:5000/api/v1/posters?id=21
or for username search e.g. http://127.0.0.1:5000/api/v1/posters?username=Bret

Note: there are more frequent commenter rows but only displaying one, due to time constraint (struggled with proper Json formatting) and learning/completing part 5 in time. 

Final thoughts(improvements) that would be helpful.
Ideally, json should be an object instead of string collection to make building json output cleaner/readable. Also, use of stored procedure instead of SQL.

Thank you for your consideration.

