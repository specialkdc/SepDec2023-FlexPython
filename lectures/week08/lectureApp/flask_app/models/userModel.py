from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db = 'anime'
    def __init__(self, data):
        self.id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.username = data['username']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM user;'
        # let results = connect to the database send above query and return with results
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users

    @classmethod
    def getOne(cls, data):
        # %()s = wild card or basically the information we are passing in
        query = "SELECT * FROM user WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def getUsername(cls, data):
        # %()s = wild card or basically the information we are passing in
        query = "SELECT * FROM user WHERE username = %(username)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO user (firstName, lastName, username) VALUES (%(firstName)s, %(lastName)s, %(username)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update():
        pass

    @classmethod
    def delete():
        pass