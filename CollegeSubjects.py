
class CollegeSubjects:

    def __init__(self, id,  name, course, dbManager, table):
        self._id = id
        self._name = name
        self._course = course
        self._table  = table
        self._dbManager = dbManager

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getCourse(self):
        return self._course

    def getDbManager(self):
        return self._dbManager

    def getTable(self):
        return self._table
        
    def setId(self, id):
        self._id = id

    def setName(self, name):
        self._name = name

    def setCourse(self, course):
        self._course = course

    def setDbManager(self, dbManager):
        self._dbManager = dbManager
        
    def setTable(self, table):
        self._table = table

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
