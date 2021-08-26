from core import admin
from core import student
from core import teacher


def run():
    func_dic = {'1': ['管理员功能', admin.admin_view],
                '2': ['学生功能', student.student_view],
                '3': ['老师功能', teacher.teacher_view]}
    while True:
        print(f"=====欢迎来到选课系统=====")

        for i, v in func_dic.items():
            print(f"{i}: {v[0]}")
        print("=====     end     =====")

        choice = input('请输入功能编号: ').strip()
        if choice == 'q':
            break
        if choice not in func_dic:
            print("请输入正确的编号!")
            continue
        else:
            func_dic.get(choice)[1]()
