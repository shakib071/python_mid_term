

class Star_Cinema:
    hall_list=[]

    def entry_hall(self,hall):
        self.hall_list.append(hall)


class Hall(Star_Cinema):

    def __init__(self,rows,cols,hall_no) -> None:
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no
        self.seats={}
        self.show_list=[]
        
    def entry_show(self,id,movie_name,time):
        temp=(id,movie_name,time)
        self.show_list.append(temp)
        self.seats[id]=[['free' for _ in range(self.cols)] for _ in range(self.rows)]


hall1=Hall(rows=12,cols=12,hall_no=1)
hall1.entry_show('s1','Avenger','12:12 PM')

print(hall1.seats)
print(hall1.show_list)
    
