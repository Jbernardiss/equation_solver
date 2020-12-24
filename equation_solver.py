
import sys
import equation as eq


print("Enter the second degree equation(ax² + bx + c = 0)")

a = int(input("Enter the a: "))
b = int(input("Enter the b: "))
c = int(input("Enter the c: "))

equation = eq.equation(a, b, c)

delta_status = equation.calculate_delta()

if delta_status == 0:
    equation.calculate_results()

elif delta_status == 1:
    equation.calculate_complex_results()

elif delta_status == 2:
    print("Result is not real number")
    sys.exit()

equation.print_results()
