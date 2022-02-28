class Data:
    # Protected
    _char = 'J'
    # Private
    __digit = 9

    def disp(self):
        print(self._char)
        print(self.__digit)

data = Data()

#print(data.__digit)
data.disp()
# Accessing Private and Protected atrributes.
print(data._Data__digit)