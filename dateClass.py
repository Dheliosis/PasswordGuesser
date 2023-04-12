class Date:
    # gestion des jours en 01 - 1
    month = {
            "01": [1, 'janvier', 'janv'],
            "02": [2, 'février', 'fevr'],
            "03": [3, 'mars', 'mars'],
            "04": [4, 'avril', 'avr'],
            "05": [5, 'mai', 'mai'],
            "06": [6, 'juin', 'juin'],
            "07": [7, 'juillet', 'juill'],
            "08": [8, 'aout', 'aout'],
            "09": [9, 'septembre', 'sept'],
            "10": ['octobre', 'oct'],
            "11": ['novembre', 'nov'],
            "12": ['decembre', 'dec'],
        }
    
    def cleanDate(self, date):
        print('[cleanDate]')
        date= str(date)
        dateArray = date.split('-')
        # print(dateArray)
        return dateArray
    
    def transformMonth(self, date):
        for el in self.month:
            if date == el:
                # print(el)
                # print(self.month[el])
                return self.month[el]