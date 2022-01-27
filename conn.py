import mysql.connector


class Sql:
    db = None
    cursor = None

    def __init__(self):
        # Initialize the database
        self.db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='toor',
        )

        # Initialize the cursor
        self.cursor = self.db.cursor()

        # Execution of commands at initialization
        try:
            # Creation of db if it not exists
            self.cursor.execute(
                "create database if not exists quiz"
            )
            # Select the db
            self.cursor.execute('use quiz')
            # Create the login table
            self.cursor.execute(
                "create table if not exists login (username varchar(30) primary key not null,password varchar(30) not null, name varchar(30) not null, acc_type int not null)"
            )
            # Create the report table
            self.cursor.execute(
                "create table if not exists report(username varchar(30) primary key not null, score int not null, quiz_date varchar(20) not null);"
            )
            # Create the quiz.ques_bank table
            self.cursor.execute(
                "create table if not exists quiz.ques_bank(qno int primary key auto_increment, ques varchar(300) not null, op1 varchar(300) not null,op2 varchar(300) not null,op3 varchar(300) not null,op4 varchar(300) not null,ans varchar(300) not null)"
            )
            self.cursor.execute(
                'insert into quiz.login(username, password, name, acc_type) values("admin","admin","admin",0)'
            )
        except mysql.connector.Error as e:
            print(f"Error: {e}")

    # Fn to add a question
    def add_question(self, question, ops, answer):
        try:
            self.cursor.execute(
                f"insert into quiz.ques_bank(ques, op1, op2, op3, op4, ans) values('{question}', '{ops[0]}', '{ops[1]}', '{ops[2]}', '{ops[3]}', '{answer}')"
            )
            self.db.commit()
            print("Question Added!")
        except mysql.connector.Error as e:
            print(f'Error: {e}')

    # Fn to view the question bank
    def view_qbank(self):
        try:
            self.cursor.execute(
                "select * from quiz.ques_bank"
            )
            res = self.cursor.fetchall()
            return res
        except mysql.connector.Error as e:
            print(f"Error: {e}")

    # Fn to delete a question from the question bank
    def delete_question(self, qno):
        try:
            self.cursor.execute(f'delete from quiz.ques_bank where qno={qno}')
            self.db.commit()
            print("Question deleted!")
        except mysql.connector.Error as e:
            print(f"Error: {e}")

    # Fn to create the user in the login table
    def create_user(self, login, password, name, type):
        try:
            self.cursor.execute(
                f"insert into quiz.login(username, password, name, acc_type) values('{login}', '{password}', '{name}', {type})")
            self.db.commit()
            print("User added!")
        except mysql.connector.Error as e:
            print(f"Error: {e}")

    # Fn to create a report of the user
    def add_report(self, name, score, date):
        try:
            self.cursor.execute(
                f"insert into quiz.report(username, score, quiz_date) values('{name}','{score}','{date}')"
            )
            self.db.commit()
            print("Report Added!")
        except mysql.connector.Error as e:
            print(f'Error: {e}')

    # Fn to get all users
    def get_all_users(self):
        try:
            self.cursor.execute('select * from quiz.login')
            res = self.cursor.fetchall()
            return res
        except mysql.connector.Error as e:
            print(f'Error: {e}')

    # Fn to check if it is admin
    def check_if_admin(self, username, pwd):
        try:
            self.cursor.execute(
                'select * from quiz.login where acc_type=0'
            )
            for rec in self.cursor.fetchall():
                if username == rec[0] and pwd == rec[1]:
                    return True
                else:
                    return False
        except mysql.connector.Error as e:
            print(f'Error: {e}')

    def get_all_questions(self):
        try:
            self.cursor.execute('select * from quiz.ques_bank')
            res = self.cursor.fetchall()
            return res
        except mysql.connector.Error as e:
            print(f'Error: {e}')

    def get_all_reports(self):
        try:
            self.cursor.execute('select * from quiz.report')
            res = self.cursor.fetchall()
            return res
        except mysql.connector.Error as e:
            print(f'Error: {e}')
