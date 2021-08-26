from interface import admin_interface


def register():
    while True:
        username = input("请输入用户名: ").strip()
        password = input("请密码: ").strip()
        re_password = input("请确认密码: ").strip()
        if password == re_password:
            admin_interface.admin_register_interface(username, password)
        else:
            print('两次密码不一致，请重新输入')


def login():
    pass


def create_school():
    pass


def create_course():
    pass


def create_teacher():
    pass


def admin_view():
    func_dic = {'1': ['注册', register],
                '2': ['登录', login],
                '3': ['创建学校', create_school],
                '4': ['创建课程(先选择学校)', create_course],
                '5': ['创建讲师', create_teacher]}
    while True:
        print("=====管理员功能=====")
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
