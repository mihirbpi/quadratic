import math

# Returns a boolean if an integer n is a perfect square or not
def is_perfect_square(n):
    # If the sqrt(n) and the lowest integer at or below the sqrt(n) are the same then n is a perfect square
    return math.sqrt(n) == math.floor(math.sqrt(n))

# Returns the sqrt if the input is a perfect square
def get_int_square_root(perfect_square):
    # Return the sqrt as an integer (without the math.floor the answer would be a float)
    return math.floor(math.sqrt(perfect_square))

# Returns a list representing the simplified sqrt of a number n
def my_sqrt(n):

    # If n is a perfect square the list has length 1 and its only element is an integer which is the sqrt of n
    # For example a list [5] means sqrt(n) = 5
    if(is_perfect_square(n)):
        list_result = []
        list_result.append(get_int_square_root(n))
        return list_result

    # If n is not a perfect square the list has length 2 and its two elements represent the integral and sqrt parts
    # For example a list [5, 2] represents that sqrt(n) = 5√2
    else:
        # To make this list first make a list of all perfect squares less than or equal to n that also divide n
        # If m is the maximum perfect square in that list then n = m * q where q is some integer and q will have no perfect square factors
        # This is because m is the maximum perfect_square that divides n
        # So sqrt(n) = sqrt(m) * sqrt(q) where sqrt(m) is an integer since m is a perfect square and q has no perfect square factors
        list_squares = []

        for i in range(1, n+1):

            if(n % i == 0 and is_perfect_square(i)):
                # Add perfect squares that divide n to the list of perfect squares less than n that divide it as integers
                div = math.floor(i)
                list_squares.append(div)

                # Extract the maximum perfect square (m) that divides n from this list
                # n = m * q where q is some integer
                # So q = n / m represented as an integer
                # And sqrt(n) = sqrt(m) * √q
                # The first element in the list is sqrt(m) which is an integer the second element is q which is under the sqrt
                # The list represents sqrt(m) * √q
        m = max(list_squares)
        q = math.floor(n / max(list_squares))
        list_result = [get_int_square_root(m), q]
        return list_result

# Solves a quadratic equation with coefficients a,b, and c
def quadratic(a, b, c):

    # Discriminant of the quadratic (D)
    D = b ** 2 - 4 * a * c

    # If a = 0 the solution is -c / b
    if(a == 0):
        # Print the equation
        print("Solutions to "+str(b)+"x + "+str(c)+" = 0:")
        num = -c
        denom = b
        gcd = math.gcd(num, denom)

        # If the numerator -c is divisible by the denominator b divide them and give the answer as an integer
        if(num % denom == 0):
            # Print the solution
            print(str(math.floor(num / denom)))

        # If the gcd of numerator -c and the denominator b is 1 give the answer as a fraction -c / b
        elif(gcd == 1):
            # Print the solution
            print(str(num)+"/"+str(denom))

        # If the gcd of numerator -c and the denominator b is not 1 divide both by the gcd and give the answer as a simplified fraction -c / b
        else:
            num = math.floor(num / gcd)
            denom = math.floor(denom / gcd)
            # Print the solution
            print(str(num)+"/"+str(denom))

    # Else the solution has two parts -b / 2a and D / 2a
    # D / 2a is either added or subtracted from -b / 2a
    # The simplified -b / 2a will be called str1 and the simplified D / 2a will be called str2

    # If D >= 0 then the quadratic has two real solutions
    elif(D >= 0):
        answer_plus = ""
        answer_minus = ""
        denom1 = 2 * a
        denom2 = 2 * a
        num1 = -b
        gcd1 = math.gcd(num1, denom1)

        # If the numerator -b is divisible by the denominator 2a divide them and give the answer as an integer
        if(num1 % denom1 == 0):
            str1 = str(math.floor(num1 / denom1))

        # If the gcd of numerator -b and the denominator 2a is 1 give the answer as a fraction -b / 2a
        elif (gcd1 == 1):
            str1 = str(num1)+"/"+str(denom1)

        # If the gcd of numerator -b and the denominator 2a is not 1 divide both by the gcd and give the answer as a simplified fraction -b / 2a
        else:
            num1 = math.floor(num1 / gcd1)
            denom1 = math.floor(denom1 / gcd1)
            str1 = str(num1)+"/"+str(denom1)

        # If length of the my_sqrt(D) list is 1 then D was a perfect square and simplifies to an integer after taking the sqrt
        if (len(my_sqrt(D)) == 1):
            num2 = my_sqrt(D)[0]
            gcd2 = math.gcd(num2, denom2)

            # If the numerator my_sqrt(D)[0] is divisible by the denominator 2a divide them and give the answer as an integer
            if(num2 % denom2 == 0):
                str2 = str(math.floor(num2 / denom2))

            # If the gcd of numerator sqrt(D)[0] and the denominator 2a is 1 give the answer as a fraction sqrt(D) / 2a
            elif (gcd2 == 1):
                str2 = str(num2)+"/"+str(denom2)

            # If the gcd of numerator sqrt(D)[0] and the denominator 2a is not 1 divide both by the gcd and give the answer as a simplified fraction sqrt(D) / 2a
            else:
                num2 = math.floor(num2 / gcd2)
                denom2 = math.floor(denom2 / gcd2)
                str2 = str(num2)+"/"+str(denom2)

        # If length of the my_sqrt(D) list is 2 then D was not a perfect square and simplified to an integer times a sqrt (e.g. a√b) after taking the sqrt
        else:
            # Extract the integer and sqrt parts from the my_sqrt(D) list
            sqrt_list = my_sqrt(D)
            num2 = sqrt_list[0]
            sqrt = sqrt_list[1]
            gcd2 = math.gcd(num2, denom2)

            # If the integer part is divisible by the denominator 2a divide them
            # The answer is the resulting integer times the sqrt
            if(num2 % denom2 == 0):
                str2 = str(math.floor(num2 / denom2))+"√"+str(sqrt)

            # If the gcd of the integer part and the denominator 2a is 1 give the answer as a fraction
            # The answer is the integer part times the sqrt divided by the denominator
            elif (gcd2 == 1):
                str2 = "("+str(num2)+"√"+str(sqrt)+")"+"/"+str(denom2)

            # If the gcd of the integer part and the denominator 2a is not 1 divide both by the gcd and give the answer as a simplified fraction
            # The answer is the simplified integer part times the sqrt divided by the simplified denominator
            else:
                num2 = math.floor(num2 / gcd2)
                denom2 = math.floor(denom2 / gcd2)
                str2 = "("+str(num2)+"√"+str(sqrt)+")"+"/"+str(denom2)

        # The final answers should be str1 +/- str2 where str1 is the simplified -b / 2a and str2 is the simplified D/2a
        answer_plus = str1+" + "+str2
        answer_minus = str1+" - "+str2

        # If both str1 and str2 simplified to integers the answer can be simplifed further by adding/subtracting str1 from str2
        # The result is are new strings with the simplified answers which are integers
        if(len(str1) <= 2 and len(str2) <= 2):
            answer_plus = str(math.floor(num1 / denom1) + math.floor(num2 / denom2))
            answer_minus = str(math.floor(num1 / denom1) - math.floor(num2 / denom2))

        # If the denominators for the simplified str1 and str2 are the same and D was a perfect square then the fractions can be combined since there are no square roots
        # This can be done by adding/subtracting the numerators, puttting them over this common denominator, and simplifying the resulting fraction
        elif(denom1 == denom2 and len(my_sqrt(D)) == 1):
            num_plus = num1 + num2
            num_minus = num1 - num2
            denom = denom1
            gcd_plus = math.gcd(num_plus, denom)
            gcd_minus = math.gcd(num_minus, denom)

            # If the numerator num_plus is divisible by the common denominator divide them and give the result as an integer
            if(num_plus % denom == 0):
                answer_plus = str(math.floor(num_plus / denom))

            # If the gcd of the numerator num_plus and the common denominator is 1 give the result as a fraction num_plus / denom
            elif (gcd_plus == 1):
                answer_plus = str(num_plus)+"/"+str(denom)

            # If the gcd of the numerator num_plus and the common denominator is not 1 divide both by tthe gcd and give the result as a simplified fraction num_plus / denom
            else:
                num_plus = math.floor(num_plus / gcd_plus)
                denom = math.floor(denom / gcd_plus)
                answer_plus = str(num_plus)+"/"+str(denom)

            # Do the same 3 steps above but for num_minus (the minus solution)
            if(num_minus % denom == 0):
                answer_minus = str(math.floor(num_minus / denom))

            elif (gcd_minus == 1):
                answer_minus = str(num_minus)+"/"+str(denom)

            else:
                num_minus = math.floor(num_minus / gcd_minus)
                denom = math.floor(denom / gcd_minus)
                answer_minus = str(num_minus)+"/"+str(denom)

        # If str1 and str2 were both 0 then D = 0 which means str1 and str2 are both integers (0)
        # The solutions would be their sum (0) and their difference (0)
        # This case of two integerss is already taken care of

        # If str1 happens to be 0 and str2 is not 0 then only str2 occurs in the answer
        # The solutions are +/- str2
        if(str1 == "0"):
            answer_plus = str2
            answer_minus = "-"+str2

        # If str2 happens to be 0 and str1 is not 0 then only str1 occurs in the answer
        # This means the D = 0 and the quadratic has a repeated root
        # The solutions are str1 and str1
        elif(str2 == "0"):
            answer_plus = str1
            answer_minus = str1

        # Print the equationn and solutions
        print("Solutions to "+str(a)+"x^2 + "+str(b)+"x + "+str(c)+" = 0 are:")
        print(answer_plus)
        print(answer_minus)

    # If D < 0 then the quadratic has two complex solutions that are complex conjugates
    # The steps are slightly different in this case
    else:
        answer_plus = ""
        answer_minus = ""
        denom1 = 2 * a
        denom2 = 2 * a
        num1 = -b
        gcd1 = math.gcd(num1, denom1)

        # If the numerator -b is divisible by the denominator 2a divide them and give the answer as an integer
        if(num1 % denom1 == 0):
            str1 = str(math.floor(num1 / denom1))

        # If the gcd of numerator -b and the denominator 2a is 1 give the answer as a fraction -b / 2a
        elif (gcd1 == 1):
            str1 = str(num1)+"/"+str(denom1)

        # If the gcd of numerator -b and the denominator 2a is not 1 divide both by the gcd and give the answer as a simplified fraction -b / 2a
        else:
            num1 = math.floor(num1 / gcd1)
            denom1 = math.floor(denom1 / gcd1)
            str1 = str(num1)+"/"+str(denom1)

        # If length of the my_sqrt(-D) list is 1 then -D was a perfect square and simplifies to an integer after taking the sqrt
        if (len(my_sqrt(-D)) == 1):
            num2 = my_sqrt(-D)[0]
            gcd2 = math.gcd(num2, denom2)

            # If the numerator my_sqrt(-D)[0] is divisible by the denominator 2a divide them and give the answer as an integer times i
            if(num2 % denom2 == 0):
                str2 = str(math.floor(num2 / denom2))+"i"

            # If the gcd of numerator sqrt(-D)[0] and the denominator 2a is 1 give the answer as a fraction i*sqrt(-D) / 2a
            elif (gcd2 == 1):
                str2 = str(num2)+"i"+"/"+str(denom2)

            # If the gcd of numerator sqrt(-D)[0] and the denominator 2a is not 1 divide both by the gcd and give the answer as a simplified fraction i*sqrt(-D) / 2a
            else:
                num2 = math.floor(num2 / gcd2)
                denom2 = math.floor(denom2 / gcd2)
                str2 = str(num2)+"i"+"/"+str(denom2)

        # If length of the my_sqrt(-D) list is 2 then -D was not a perfect square and simplified to an integer times a sqrt (e.g. a√b) after taking the sqrt
        else:
            # Extract the integer and sqrt parts from the my_sqrt(-D) list
            sqrt_list = my_sqrt(-D)
            num2 = sqrt_list[0]
            sqrt = sqrt_list[1]
            gcd2 = math.gcd(num2, denom2)

            # If the integer part is divisible by the denominator 2a divide them
            # The answer is the resulting integer times the sqrt times i
            if(num2 % denom2 == 0):
                str2 = str(math.floor(num2 / denom2))+"i√"+str(sqrt)

            # If the gcd of the integer part and the denominator 2a is 1 give the answer as a fraction
            # The answer is the integer part times the sqrt times i divided by the denominator
            elif (gcd2 == 1):
                str2 = "("+str(num2)+"i√"+str(sqrt)+")"+"/"+str(denom2)

            # If the gcd of the integer part and the denominator 2a is not 1 divide both by the gcd and give the answer as a simplified fraction
            # The answer is the simplified integer part times i times the sqrt divided by the simplified denominator
            else:
                num2 = math.floor(num2 / gcd2)
                denom2 = math.floor(denom2 / gcd2)
                str2 = "("+str(num2)+"i√"+str(sqrt)+")"+"/"+str(denom2)

        # The final answers should be str1 +/- str2 where str1 is the simplified -b / 2a and str2 is the simplified D/2a
        answer_plus = str1+" + "+str2
        answer_minus = str1+" - "+str2

        # If str1 happens to be 0 and str2 is not 0 then only str2 occurs in the answer
        # The solutions are +/- str2
        if(str1 == "0"):
            answer_plus = str2
            answer_minus = "-"+str2

        # Print the equation and solutions
        print("Solutions to "+str(a)+"x^2 + "+str(b)+"x + "+str(c)+" = 0 are:")
        print(answer_plus)
        print(answer_minus)

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
quadratic(a,b,c)
