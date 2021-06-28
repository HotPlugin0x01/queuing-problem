class BankQueue:
    def __init__(self, typeId, size):
        self.type = typeId
        self.size = size
        self.line = [None]*size
        self.front = 0
        self.rear = 0
        self.count = 0
        self.served = 0
        self.notserved = 0
        self.totaltime = 0
        self.wait = None

    def EnqueueCustomer(self, time):
        if not self.IsFull():
            self.line[self.rear] = time
            self.totaltime +=time
            self.rear = (self.rear + 1) % self.size
            self.count +=1
        else:
            self.notserved +=1

    def DequeueCustomer(self):
        if not self.IsEmpty():
            if self.wait == None:
                self.wait = self.Peek()
            elif self.wait > 0:
                self.wait -=1
            else:
                self.front = (self.front + 1) % self.size
                self.count -=1
                self.served +=1
                self.wait = self.Peek()
            
    def IsFull(self):
        return self.size == self.count

    def IsEmpty(self):
        return self.count == 0

    def Peek(self):
        return self.line[self.front]

       
class BankSimulation:
    def __init__(self, filename):
        self.filename = filename
        self.qs = {1: BankQueue(1, 10), 2: BankQueue(2, 10), 3: BankQueue(3, 10), 4: BankQueue(4, 10)}

    def Process(self):
        with open(self.filename) as f:
            cutomers_lst = f.readlines()
            for i in range(420):
                if i < len(cutomers_lst):
                    data = cutomers_lst[i].strip().split()
                    typeId = int(data[0])
                    time = int(data[1])
                    self.qs[typeId].EnqueueCustomer(time)
                    
                self.qs[1].DequeueCustomer()
                self.qs[2].DequeueCustomer()
                self.qs[3].DequeueCustomer()
                self.qs[4].DequeueCustomer()


    def CustomersServed(self):
        qs = list(self.qs.values())
        served_lst = [q.served for q in qs]
        return served_lst

    def AverageTime(self):
        avg_time_lst = [q.totaltime/q.served if q.served > 0 else 0 for q in self.qs.values()]
        return avg_time_lst

    def NotServerd(self):
        not_served_lst = [q.notserved for q in self.qs.values()]
        return not_served_lst


# Obj = BankSimulation("customers.txt")
# Obj.Process()
# print(Obj.CustomersServed())  # [4, 2, 2, 3]
# print(Obj.AverageTime())      # [3.5, 5, 3, 4.66]
# print(Obj.NotServerd())       # [0, 0, 0, 0]