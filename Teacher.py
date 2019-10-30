from Person import *

class Teacher(Person):
  
  def __init__(self, id, name, dbManager,  gender, date_of_birth, rg, table, academic_degree):
    super().__init__(id, name, dbManager,  gender, date_of_birth, rg, table)
    self._academic_degree = academic_degree
        
  def getAcademicDegree(self, academic_degree):
    return self._academic_degree

  def setAcademicDegree(self, academic_degree):
    self._academic_degree = academic_degree

  #polymorphism
  def insert(self):
    data = [super().getId(), super().getName(), super().getGender(), super().getDateOfBirth(), super().getRg(), self._academic_degree]
    super().insert(data)

        
