class MySet:
    def __init__(self, enumerable=[]): 
        # Initializes a new MySet and adds any values from a list.
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True
    def has(self, value):
        # Checks if the value is already included in the MySet. Must have a O(1) runtime.
        return value in self.dictionary
    def add(self, value):
        # Adds the value to the MySet if it isn't already present. Must have a O(1) runtime.
        self.dictionary[value] = True
        return self
    def delete(self, value):
        # Removes the value from the MySet. Must have a O(1) runtime.
        del self.dictionary[value]
        return self
    def size(self):
        # Returns the number of elements in the MySet.
        return len(self.dictionary)
