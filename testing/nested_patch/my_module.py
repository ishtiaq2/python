class Database:

    data = dict()
    data['Toyota'] = {
        'Model': 'Corolla',
        "Year": 2020,
        'Price': 100000
    }

    data['Tesla'] = {
        "Model": "TES-10",
        "Year" : 2020,
        'Price': 5000000
    }

    def get_data(self, company='Toyota'):
        return self.data[company]



class Car:

    def __init__(self, company, model):
        self.company = company
        self.model = model

    def get_car_data(self):
        db = Database()
        data = db.get_data(self.company)
        return data



def open_function():
    db = Database()
    data = db.get_data('Toyota')
    return data