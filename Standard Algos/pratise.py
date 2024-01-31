class Item:
    def __init__(self,val,weight):
        self.val = val
        self.weight = weight
    def sampleFunc(self):
        return "This is for sample"
item1 = Item(100,60)
print(item1.sampleFunc())

        