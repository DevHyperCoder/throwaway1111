import pickle

def search_emp(search_id):
    with open("emp.dat") as f:
        while True:
            try:

                emp = pickle.load(f)
                if emp["id"] == search_id:
                    print("Id:",emp["id"])
                    print("Name:",emp["name"])
                    print("Salary:",emp["sal"])
            except Exception:
                break

emp_id = int(input("Enter employee id: "))
search_emp(emp_id)
