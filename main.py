class Calculator:
    def __init__(self, length_km:float, unit_chosen:str):
        self.length_km = length_km
        self.unit_chosen = unit_chosen
        self.length_calculated = float
    # milimetry, centrymentry, metry, cale, stopy, mile
    def km_to_milimeter(self):
        return self.length_km * 1000*1000
    def km_to_centimeter(self):
        return self.length_km * 1000*100
    def km_to_meter(self):
        return self.length_km * 1000
    def km_to_inch(self):
        return self.length_km * 1000 * 39.3700787
    def km_to_feet(self):
        return self.length_km * 1000 * 3.2808399
    def km_to_mile(self):
        return self.length_km * 0.621371192
    def choose_unit(self):
        if self.unit_chosen=='milimeter':
            self.length_calculated = self.km_to_milimeter()
        elif self.unit_chosen=='centimeter':
            self.length_calculated = self.km_to_centimeter()
        elif self.unit_chosen=='meter':
            self.length_calculated = self.km_to_meter()
        elif self.unit_chosen=='inch':
            self.length_calculated = self.km_to_inch()
        elif self.unit_chosen=='feet':
            self.length_calculated = self.km_to_feet()
        elif self.unit_chosen=='mile':
            self.length_calculated = self.km_to_mile()
        else:
            print('Wrong unit! Try again')
        return self.length_calculated

    # milimetry, centrymentry, metry, cale, stopy, mile

calculator = Calculator(length_km=25.6, unit_chosen='inch')
przelicznik = calculator.choose_unit()
print(przelicznik)