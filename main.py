from application import salary, db
# from application import db
# from salary import calculate_salary
from application.db import people
from datetime import datetime




if __name__=='__main__':
    salary.calculate_salary()
    people.get_employees()
    d = datetime.now()
    print(datetime.now())