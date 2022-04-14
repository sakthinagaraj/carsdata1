import psycopg2

def runquery(sql):
    try:
        #Connect to heroku postgre db
        connection=psycopg2.connect(user="rqmusyzeootffp",
                                    password="b7b92beb845588e052c8ec546f0d69fb19be3ed894e05cf664f85186d17a51d6",
                                    host="ec2-34-207-12-160.compute-1.amazonaws.com",
                                    database="dbo1v0h17300a2")
        #Create a cursor to perform database operations
        cursor=connection.cursor()
        # use the cursor to run an SQL. SQL can be passed in another script
        cursor.execute(sql)

        #Fetch all records from table using SQL

        record = cursor.fetchall()

        #return the fetcehd records to calling program
        return(record)
    except:
        print("Error while establishing connection/executing sql/ fetching data")
    finally:
            cursor.close()
            connection.close()
