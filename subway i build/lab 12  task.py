

class birthday:

    def __init__(self,day,month,year):
        self.day=day
        self.month=month
        self.year=year



class person:
    def __init__(self,day,month,year,name,age):
        self.day =day
        self.month = month
        self.year = year
        self.name=name
        self.age=age
        self.obj_data=birthday(self.day,self.month,self.year)

    def print_detail( self ):
        print(self.day,self.month,self.year,self.name,self.age)


x=person("monday","12","2000","usman","15")
person.print_detail(x)


