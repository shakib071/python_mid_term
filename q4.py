

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

    def book_seats(self,id,seat_list):

        if id not in self.seats:
            print(f'id is not found')
            return
        for seat in seat_list:
            row ,col=seat
            if self.seats[id][row][col]=='free':
                self.seats[id][row][col]='Booked'
                print(f' your selected seat ({row},{col}) has been booked succesfully')
            else:
                print(f'Sorry,your selected seat ({row},{col}) Already booked ')
            
    
 




hall1=Hall(rows=12,cols=12,hall_no=1)
hall1.entry_show('s1','Avenger','12:12 PM')

print(hall1.seats)
print(hall1.show_list)
hall1.book_seats('s1',[(0,0),(1,1)])

    
