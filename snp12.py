class JellyBean():
    def __init__(self, name = None, calories = None, flavor = None):
        self.name = name
        self.calories = calories
        self.flavore = flavor


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property 
    def calories(self):
        return self._calories
    
    @calories.setter
    def calories(self, calories):
        self._calories = calories

    @property
    def flavor(self):
        return self._flavor 
    
    @flavor.setter
    def flavor(self, flavor):
        self._flavor = flavor

    
    
    def is_healthy(self):
        if type(self._calories) in (int, float):
            return self._calories < 200
        else:
            return None
        
    def is_delicious(self):
        if self._flavor != "black licorice":
            return True
        else:
            return False
    