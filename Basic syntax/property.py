# # Method 1 BIF
# class Celsius():
#     def __init__(self,temperature = 0):
#         self.set_temperature(temperature)
#
#     def to_fahrenheit(self):
#         return (self.get_temperature() * 1.8) + 32
#
#     def get_temperature(self):
#         return print(self._temperature)
#
#     def set_temperature(self,value):
#         if value < -273:
#             raise ValueError("Temperature below -273 is not possible!")
#         self._temperature = value
#
# c = Celsius(37)
# c.get_temperature()
# c.set_temperature(10)
# c.get_temperature()

# # Method 2 Add Attribution
# class Celsius():
#     def __init__(self,temperature = 0):
#         self._temperature = temperature
#
#     def to_fahrenheit(self):
#         return print((self.get_temperature() * 1.8) + 32)
#
#     def get_temperature(self):
#         print("Getting value")
#         return self._temperature
#
#     def set_temperature(self,value):
#         if value < -273:
#             raise ValueError("Temperature below -273 is not possible!")
#         print("Setting value")
#         self._temperature = value
#
#     temperature = property(get_temperature,set_temperature)
#     # temperature = property()
#     # temperature = temperature.getter(get_temperature)
#     # temperature = temperature.setter(set_temperature)
#
# c = Celsius()
# c.temperature
# c.temperature = 37
# c.to_fahrenheit()

# Method 3 @property
class Celsius():
    def __init__(self,temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self,value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible!")
        print("Setting value")
        self._temperature = value

c = Celsius()
c.temperature
c.temperature = 27
print(c.to_fahrenheit())
print(c.temperature)