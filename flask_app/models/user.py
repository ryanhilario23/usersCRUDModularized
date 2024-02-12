from flask_app.config.mysqlconnection import connectToMySQL

class User:
    DB = 'users_schema'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_users(cls):
        query = """
                SELECT *
                FROM users;
                """
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
    
    @classmethod
    def get_one_user_id(cls,id):
        query = """
                SELECT *
                FROM users
                WHERE id = %(id)s;
                """
        data = {'id': id}
        results = connectToMySQL(cls.DB).query_db(query,data)
        print(results)
        return results[0]

    @classmethod
    def save_user(cls,data):
        query = """
                INSERT INTO users (first_name, last_name, email, created_at, updated_at)
                VALUES (%(first_name)s, %(last_name)s,%(email)s,NOW(),NOW())
                """
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results
    
    @classmethod
    def update(cls,data):
        query = """ 
                UPDATE users
                SET first_name = %(first_name)s,last_name = %(last_name)s, email= %(email)s
                WHERE id = %(id)s;"""
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results
    
    @classmethod
    def delete_user(cls,user_id):
        query = """
                DELETE FROM users
                WHERE id = %(id)s;
                """
        data ={'id':user_id}
        return connectToMySQL(cls.DB).query_db(query,data)