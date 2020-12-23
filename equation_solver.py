
import equation as eq


print("Enter the second degree equation(ax² + bx + c = 0)")

a = int(input("Enter the a: "))
b = int(input("Enter the b: "))
c = int(input("Enter the c: "))

equation = eq.equation(a, b, c)

equation.calculate_delta()
equation.calculate_results()
equation.print_results()
