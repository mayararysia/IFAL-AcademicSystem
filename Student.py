from Person import Person

class Student(Person):

  def __init__(self, id, name, dbManager,  gender, date_of_birth, rg, table_name):
      super(Student, self).__init__(id, name, dbManager,  gender, date_of_birth, rg, table_name)
                  
