1. Install PostgreSql in your local machine.
2. Create a database or use an existing database. 
3. Update your Db name, user name, password, host and port in the address_storage/settings.py file under DATABASES.
4. Activate the virtual environment in your terminal and execute the following commands: 
	i)  python manage.py makemigrations polls
	ii) python manage.py migrate
	# This would create the tables Company and StateJapan in your PostgreSql database.
5. Run python manage.py runserver
6. Visit http://localhost:8000/polls/docs/ for the documentation of the allowed api requests and responses.
7. Visit http://127.0.0.1:8000/polls/company/ for listing the various companies or adding a new company with its address into the Database.
8. Visit http://127.0.0.1:8000/polls/company/<company name> to retrieve the details of a company. 
9. Visit http://127.0.0.1:8000/polls/company?city<city name> to retrieve companies within a city.
10.Visit http://localhost:8000/polls/pincode/2 to retrieve all postal codes which have more than 2 companies.

Sample Post call to add a new company:
Request:
http://127.0.0.1:8000/polls/company/
{
        "company_name": "Urenok",
        "building_number": "396",
        "postal_code": "560-103",
        "locality": "HSR",
        "city": "Bangalore",
        "state": 2
}


Additional Information:
1. Run "python manage.py test" to run the test cases
2. Python version 3.6 has been used
3. Django rest framework has been used with the latest version 3.8.2