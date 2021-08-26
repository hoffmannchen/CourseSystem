def login():
    pass


def check_course():
    pass


def choose_course():
    pass


def check_stu_from_course():
    pass


def change_score_from_student():
    pass


def teacher_view():
    func_dic = {'1': ['登录', login],
                '2': ['查看教授课程', check_course],
                '3': ['选择教授课程', choose_course],
                '4': ['查看课程下学生', check_stu_from_course],
                '5': ['修改学生分数', change_score_from_student]}
    while True:
        print("=====老师功能=====")
        for i, v in func_dic.items():
            print(f"{i}: {v[0]}")
        print("=====   end   =====")
        choice = input('请输入功能编号: ').strip()
        if choice == 'q':
            break
        if choice not in func_dic:
            print("请输入正确的编号!")
            continue
        else:
            func_dic.get(choice)[1]()
