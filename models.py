

def Scheme():

    name: str
    areas: list[Area]

    def toJson():
        pass
    
def Area():

    name: str
    steps: list[Step]

def Step():

    method: str
    paintId: str

def Paint():

    name: str
    type: str

    def toJson():
        pass
