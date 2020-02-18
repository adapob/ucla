import mysql.connector
import xlsxwriter

#mySQL connection
config = {
  'user': 'adriana',
  'password': 'abc123',
  'host': '127.0.0.1',
  'database': 'programming_assignment_db',
  'raise_on_warnings': True
}

#pull database records and write to excel
cnx = mysql.connector.connect(**config)
mycursor = cnx.cursor()
mycursor.execute("SELECT * FROM v_users_commenters")
myresult = mycursor.fetchall()

workbook = xlsxwriter.Workbook('FrequentCommenterReport.xlsx')
worksheet = workbook.add_worksheet("Frequent Commenter Report.")
#write report headers
worksheet.write('A1', 'Poster Username')
worksheet.write('B1', 'Poster Latitude')
worksheet.write('C1', 'Poster Longitude')
worksheet.write('D1', 'Commenter Username')
worksheet.write('E1', 'Distance')
worksheet.write('F1', 'Comment Count')

ex_row = 2
for row in myresult:
    worksheet.write('A' + str(ex_row), row[1])
    worksheet.write('B' + str(ex_row), row[2])
    worksheet.write('C' + str(ex_row), row[3])
    worksheet.write('D' + str(ex_row), row[6])
    worksheet.write('E' + str(ex_row), row[10])
    worksheet.write('F' + str(ex_row), row[5])
    #increment for rows 
    ex_row = ex_row + 1
    # to test output
    # print("Poster Username: ", row[1])
    # print("Poster Latitude: ", row[2])
    # print("Poster Longitude: ", row[3])
    # print("Commenter Username: ", row[6])
    # print("Distance: ", row[10])
    # print("Comment Count: ", row[5])
    # print("\n")

workbook.close()
# close connection
cnx.close()


