class student():
    def __init__(self, name, Math_score, Chinese_score):
        self.name = name
        self.Math_score = Math_score
        self.Chinese_score = Chinese_score
    
    ## repr 函数用于定义对象被输出时的输出结果
    def __repr__(self):
        return str((self.name, self.Math_score, self.Chinese_score))
    
    def change_score(self, course_name, score):
        if course_name == 'Math':
            self.Math_score = score
        elif course_name == 'Chinese':
            self.Chinese_score = score
        else:
            print(course_name, " course is still not in current system")
    
    def print_name(self,):
        print(self.name)
    
    name = 'Undefined'
    Math_score = None
    Chinese_score = None