def register():
    pass


def login():
    pass


def choice_school():
    pass


def choice_course():
    pass


def check_score():
    pass


def student_view():
    func_dic = {'1': ['注册', register],
                '2': ['登录', login],
                '3': ['选择校区', choice_school],
                '4': ['选择课程(先选择校区，再选择校区中的某一门课程）', choice_course],
                '5': ['查看分数', check_score]}
    while True:
        print("=====学生功能=====")
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
