# class College:
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id
#     def getCollegeName(self):
#         return self.name
#     def show(self):
#         print("This is the show of the college class.")
#         return
# class Student(College):
#     def __init__(self,s_name,s_id,c_name,c_id):
#         super().__init__(c_name,c_id)
#         self.s_name = s_name
#         self.s_id = s_id
#     # def show(self):
#     #     print("This is the show of the student class.")
#     #     return    
#     def m1(self,n1):
#         print(n1)
#         return
#     def m1(self,n1,n2):
#         print(n1,n2)
#         return
    

# stud = Student("lav",132,"PSIT",124)
# print(stud.getCollegeName())
# # stud.m1(12,12)
# stud.m1(43)



class Student:
    def __init__(self,s_name,s_id):
        self.__s_name = s_name
        self.__s_id = s_id
    def getName(self):
        return self.__s_name
stud = Student("naman",12)
print(stud.getName())