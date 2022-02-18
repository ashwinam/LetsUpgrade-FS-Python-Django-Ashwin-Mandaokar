# make a class home which will take owner name , price , road_no, floor,size,area as parameter
# it has a class variable which keeps count of total flats 
# it has instance method which returns the introduction of flat 
# it will have repr method 
# it will have static method which will find rate of flat based on size


class home:
    flats=0
    def __init__(self,owner,price,road_no,floor,size,area):
        self.owner=owner
        self.price=price
        self.road_no=road_no
        self.floor=floor
        self.size=size
        self.area=area
        home.flats+=1

    def Introduction(self):
        return f'The owner name is{self.owner} the price of flat is{self.price}the address is{self.road_no},{self.floor},The size & area of flat is{self.size} {self.area}'
    
    def __repr__(self):
        return f'{self.owner}, {self.price}, {self.road_no}, {self.floor}, {self.size}, {self.area}'

    @staticmethod
    def rate_of_flat(size,price):
        return size*price
