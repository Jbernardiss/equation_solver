
import math


class equation():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.x1 = None
        self.x2 = None

    def calculate_delta(self):
        self.delta = self.b ** 2 - 4 * self.a * self.c

        if self.delta < 0:
            # print("Result is not real")
            return 2

        elif round(math.sqrt(self.delta)) != math.sqrt(self.delta):
            print(f"Imprecise root: {math.sqrt(self.delta)}")
            return 1

        else:
            self.delta = math.sqrt(self.delta)
            return 0

    def calculate_results(self):
        self.x1 = (-self.b + self.delta) / (2 * self.a)
        self.x2 = (-self.b - self.delta) / (2 * self.a)

        if self.x1 != int(self.x1):
            self.x1_1 = int(-self.b + self.delta)
            self.x1_2 = int(2 * self.a)
            self.x1_gdc = math.gcd(self.x1_1, self.x1_2)
            self.x1 = str(int(self.x1_1 / self.x1_gdc)) + "/" + str(int(self.x1_2 / self.x1_gdc))
        else:
            self.x1 = int(self.x1)

        if self.x2 != int(self.x2):
            self.x2_1 = int(-self.b - self.delta)
            self.x2_2 = int(2 * self.a)
            self.x2_gdc = math.gcd(self.x2_1, self.x2_2)
            self.x2 = str(int(self.x2_1 / self.x2_gdc)) + "/" + str(int(self.x2_2 / self.x2_gdc))
        else:
            self.x2 = int(self.x2)

    def calculate_complex_results(self):
        self.x1 = f"{str(int(-self.b))} +√{str(int(self.delta))}/{str(int(2 * self.a))}"
        self.x2 = f"{str(int(-self.b))} -√{str(int(self.delta))}/{str(int(2 * self.a))}"

    def print_results(self):
        print(f"X1 is {self.x1}")
        print(f"X2 is {self.x2}")
