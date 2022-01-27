from conn import Sql
from getpass import getpass
import datetime as dt

while True:
    sql = Sql()
    print("***********************")
    print("* Quiz Python Project *")
    print("*                v1.0 *")
    print("***********************")
    print()
    adm_or_user = input("Admin (y/n)?\n\t[STR] ").lower()
    val_inp = ['y', 'n']
    while adm_or_user not in val_inp:
        print("Enter correct character!")
        adm_or_user = input("[A]dmin or [U]ser?\n\t[STR] ").lower()
    if adm_or_user == val_inp[0]:
        user = input("Username\n\t[STR] ")
        pwd = getpass()
        is_admin = sql.check_if_admin(user, pwd)
        if is_admin:
            print('(1) Add question to bank')
            print('(2) View question bank')
            print('(3) Delete from bank')
            print('(4) Get all users')
            print('(5) Get all user reports')
            ch = [1, 2, 3, 4, 5]
            dec = int(input("Enter your choice?\n\t[INT] "))
            while dec not in ch:
                print("Enter correct character!")
                dec = int(input("Enter your choice?\n\t[INT] "))
            if dec == ch[0]:
                question = input("Enter the question?\n\t[STR] ")
                ops = list(map(str, input(
                    "Enter the options separated by a comma?\n\t[STR,STR,STR,STR] ").split(',')))
                answer = input("Enter the answer?\n\t[STR] ")
                sql.add_question(question, ops, answer)
            elif dec == ch[1]:
                ques = sql.view_qbank()
                print('***********************')
                for q in ques:
                    print(f'Question ID     -> {q[0]}')
                    print(f'Question        -> {q[1]}')
                    print(f'Option Number 1 -> {q[2]}')
                    print(f'Option Number 2 -> {q[3]}')
                    print(f'Option Number 3 -> {q[4]}')
                    print(f'Option Number 4 -> {q[5]}')
                    print(f'Answer          -> {q[6]}')
                    print('***********************')
            elif dec == ch[2]:
                qno = int(
                    input("Enter the question number to delete?\n\t[INT] "))
                sql.delete_question(qno)
            elif dec == ch[3]:
                users = sql.get_all_users()
                print('***********************')
                for user in users:
                    print(f"Username     -> {user[0]}")
                    print(f"User's name  -> {user[2]}")
                    if user[3] == 0:
                        print(f'Account type -> 0 - Admin')
                    else:
                        print(f'Account type -> 0 - Regular User')
            elif dec == ch[4]:
                reports = sql.get_all_reports()
                for report in reports:
                    print(
                        f'{report[0]} attempted the quiz on {report[2]} getting a score of {report[1]}!')
        else:
            pass
    elif adm_or_user == val_inp[1]:
        name = input("Enter your name\n\t[STR] ")
        score = 0
        correct = 0
        wrong = 0
        marks_for_correct = 0
        questions = sql.get_all_questions()
        for question in questions:
            print('***********************')
            print("Statement:", question[1])
            op_dict = {
                'a': question[2],
                'b': question[3],
                'c': question[4],
                'd': question[5],
                'answer': question[6]
            }
            for k, v in op_dict.items():
                if k != 'answer':
                    print(f'{k.upper()}: {v}')
            answer = input(
                "Enter your answer [A],[B],[C],[D]\n\t[STR] ").lower()
            valid_ans = ['a', 'b', 'c', 'd']
            if answer not in valid_ans:
                print("Enter correct character!")
                answer = input(
                    "Enter your answer [A],[B],[C],[D]\n\t[STR] ").lower()
            if op_dict[answer] == op_dict['answer']:
                correct += 1
            else:
                wrong += 1
        score = correct * 1
        today = dt.datetime.now()
        today_frmt = today.strftime('%d %b %Y')

        print(
            f'{name} got {correct} answers right and {wrong} answers wrong! That means the total score is {score}!')
        sql.add_report(name, score, today_frmt)
