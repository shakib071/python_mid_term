

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
        super().__init__()
        Star_Cinema.entry_hall(self)
     