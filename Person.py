class Person(object):

  def __init__(self, id, name, dbManager,  gender, date_of_birth, rg, table_name):
    self._dbManager = dbManager
    self._id = id
    self._name = name
    self._gender = gender
    self._date_of_birth = date_of_birth
    self._rg = rg
    self._table = table_name

  def getId(self):
    return self._id

  def getName(self):
    return self._name

  def getDbManager(self):
    return self._dbManager
        
  def getGender(self):
    return self._gender

  def getDateOfBirth(self):
    return self._date_of_birth

  def getRg(self):
    return self._rg

  def getTableName(self):
    return self._table

  def getAttributes(self):
    return self._attributes

  def setId(self, id):
    self._id = id
        
  def setDbManager(self, dbManager):
    self._dbManager = dbManager

  def setName(self, name):
    self._name = name

  def setGender(self, gender):
    self._gender = gender

  def setDateOfBirth(self, date_of_birth):
    self._date_of_birth = date_of_birth

  def setRg(self, rg):
    self._rg = rg

  def setTableName(self, table_name):
    self._table = table_name

  def setAttributes(self, attributes):
    self._attributes = attributes

  def insert(self, data):
    self._dbManager.insert(self._table, data)

  def delete(self):
    self._dbManager.deleteData(self._table, self._id)

  def update(self, attributes, data):
    self._dbManager.updateData(self._table, attributes, data)
        
  def listAll(self):
    return self._dbManager.listData(self._table)

  def listAData(self):
    return self._dbManager.listAData(self._table, self._id)

