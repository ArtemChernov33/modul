
from salary import calculate_salary
from db import people
from datetime import datetime




if __name__=='__main__':
    calculate_salary()
    people.get_employees()
    d = datetime.now()
    print(datetime.now())