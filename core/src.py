def run():
    menu_list = ['管理员功能', '学生功能', '老师功能']
    while True:
        print(f"=====欢迎来到选课系统=====")

        for i, v in enumerate(menu_list):
            print(f"{i}: {v}")
        print("=====     end     =====")
