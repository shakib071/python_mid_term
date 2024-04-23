

class Star_Cinema:
    _hall_list=[]

    def entry_hall(self,hall):
        self._hall_list.append(hall)


class Hall(Star_Cinema):

    def __init__(self,rows,cols,hall_no) -> None:
        self._rows=rows
        self._cols=cols
        self._hall_no=hall_no
        self._seats={}
        self._show_list=[]
        
    def entry_show(self,id,movie_name,time):
        temp=(id,movie_name,time)
        self._show_list.append(temp)
        self._seats[id]=[['free' for _ in range(self._cols)] for _ in range(self._rows)]

    def book_seats(self,id,seat_list):

        if id not in self._seats:
            print(f'id is not found')
            return
        for seat in seat_list:
            row ,col=seat
            if self._seats[id][row][col]=='free':
                self._seats[id][row][col]='Booked'
                print(f' your selected seat ({row},{col}) has been booked succesfully')
            else:
                print(f'Sorry,your selected seat ({row},{col}) Already booked ')
            
    
    def view_show_list(self):
        print("Running shows are:")

        for show in self._show_list:
            print(f'Show ID: {show[0]}, Movie : {show[1]} Time: {show[2]}' )


    def view_available_seats(self,id):

        if id in self._seats:
            print (f'Available seats for id :{id} are')
            for x in range(self._rows):
                for y in range(self._cols):
                    if self._seats[id][x][y]=='free':
                        print(f'Seat ({x},{y})')
        else:
            print('Invalid Id')
    



class CounterSystem:
    def __init__(self, hall):
        self.hall = hall

    def run(self):
        while True:
            
            print("\nCounter Menu:")
            print("1. View all shows running")
            print("2. View available seats for a show")
            print("3. Book tickets for a show")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.hall.view_show_list()
            elif choice == "2":
                show_id = input("Enter the show ID to view available seats: ")
                self.hall.view_available_seats(show_id)
            elif choice == "3":
                show_id = input("Enter the show ID to book tickets: ")
                num_seats = int(input("How many seats do you want to book?: "))
                seat_list = []
                for _ in range(num_seats):
                    row = int(input("Enter row number for seat: "))
                    col = int(input("Enter col number for seat: "))
                    seat_list.append((row, col))
                self.hall.book_seats(show_id, seat_list)
            elif choice == "4":
                print("Exit")
                break
            else:
                print("Invalid choice. Please enter a valid option.")





hall1=Hall(12,12,1)
hall1.entry_show('s1','Avenger','12:12 PM')

print(hall1._seats)
print(hall1._show_list)
hall1.book_seats('s1',[(0,0),(1,1)])
hall1.view_show_list()
hall1.view_available_seats('s1')
C1=CounterSystem(hall1)
C1.run()
    
