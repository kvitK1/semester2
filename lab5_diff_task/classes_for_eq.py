"""lab5 task3 classes"""


class Polynomial:
    """A class to represent the polynomial.

    Attributes:
        coefficients: list
            list of coefficients in the polynomial

    """

    def __init__(self, coefficients):
        """Inits Polynomial with coefficients."""

        self.coefficients = self.check_empty(self.first_non_zero(list(coefficients)))

    def __eq__(self, other):
        """Overrides == operator."""
        bol = set()
        if isinstance(self, Polynomial) and isinstance(other, Polynomial):
            if len(self.coefficients) == len(other.coefficients):
                for elem, emel in zip(self.coefficients, other.coefficients):
                    if elem == emel:
                        bol.add(True)
                    else:
                        bol.add(False)
            else:
                return False
            if False not in bol:
                return True
        elif len(self.coefficients)==1 and other==self.coefficients[0]:
            return True

    def __hash__(self):
        """Overrides hash method."""
        return hash(tuple(self.coefficients))

    def __str__(self):
        """Shows info about Polynomial coefficients when printed."""
        return f"Polynomial(coeffs=[{', '.join([str(item) for item in self.coefficients])}])"

    @staticmethod
    def first_non_zero(coeffs):
        """Checks if first n elements are 0 and
        returns list of coefficients without 0s."""
        for inx, num in enumerate(coeffs):
            if num != 0:
                return coeffs[inx:]
        return coeffs

    @staticmethod
    def check_empty(coeffs):
        """Checks if list of coefficients is empty and equals it to [0]."""
        if len(coeffs) == 0:
            coeffs = [0]
        return coeffs

    @staticmethod
    def helper_for_eval(coeffs):
        """Creates a string with polynomial."""
        equat = f"{coeffs[0]}*x**{len(coeffs)-1}"
        for i in range(1, len(coeffs)):
            if coeffs[i][0] != '-':
                coeffs[i] = f"+{coeffs[i]}"
        for i in range(1, len(coeffs)):
            equat += f"{coeffs[i]}*x**{len(coeffs)-i-1}"
        return equat

    def evalAt(self, value):
        """Evals the string with polynomial
        and finds the result, when x = some value."""
        equat=self.helper_for_eval([str(item) for item in self.coefficients])
        x=value
        return eval(equat)

    def coeff(self, deg):
        """Returns the n-th coefficient."""
        if deg < len(self.coefficients):
            return self.coefficients[::-1][deg]
        else:
            return None

    def degree(self):
        """Returns the degree of polynomial."""
        return len(self.coefficients)-1

    def scaled(self, scale):
        """Multiplies the polynomial by 10."""
        new_coeffs = []
        for el in self.coefficients:
            new_el = el*scale
            new_coeffs.append(new_el)
        return Polynomial(new_coeffs)

    def derivative(self):
        """Finds the derivative of polynomial."""
        der_coeffs = []
        for i in range(1, len(self.coefficients)):
            elem = self.coefficients[i-1]*(len(self.coefficients)-i)
            der_coeffs.append(elem)
        return Polynomial(der_coeffs)

    def addPolynomial(self, other):
        """Adds two polynomials."""
        if isinstance(other, Polynomial):
            if len(self.coefficients) >= len(other.coefficients):
                bigger = self.coefficients[::-1]
                smaller = other.coefficients[::-1]
            else:
                bigger = other.coefficients[::-1]
                smaller = self.coefficients[::-1]
            lst = []
            i=1
            while len(lst) != len(smaller):
                lst = bigger[:i]
                i+=1
            for j in range(len(lst)):
                lst[j] += smaller[j]
            for el in bigger[i-1:]:
                lst.append(el)
            return Polynomial(lst[::-1])
        else:
            return None

    def multiplyPolynomial(self, other):
        """Multiplies two polynomials."""
        if isinstance(other, Polynomial):
            multiple_res = [0]*(len(self.coefficients)+len(other.coefficients)-1)
            for i_1,j_1 in enumerate(self.coefficients):
                for i_2,j_2 in enumerate(other.coefficients):
                    multiple_res[i_1+i_2] += j_1*j_2
            return Polynomial(multiple_res)
        else:
            return None


class Quadratic(Polynomial):
    """A class to represent the quadratic polynomial.

    Attributes:
        coefficients: list
            list of coefficients in the quadratic polynomial

    """

    def __init__(self, coefficients):
        """Inits Quadratic with coefficients."""
        super().__init__(coefficients)
        if len(self.coefficients) != 3:
            raise ValueError('You entered polynomial, \
which is not quadratic one.')

    def __str__(self):
        """Shows info about quadratic polynomial when printed."""
        return f"Quadratic(a={self.coefficients[0]}, \
b={self.coefficients[1]}, c={self.coefficients[2]})"

    def discriminant(self):
        """Finds the discriminant of quadratic equatation."""
        return self.coefficients[1]**2-\
            4*self.coefficients[0]*self.coefficients[2]

    def numberOfRealRoots(self):
        """Finds number of roots for quadratic polynomial."""
        if self.discriminant() > 0:
            return 2
        elif self.discriminant() == 0:
            return 1
        else:
            return 0

    def getRealRoots(self):
        """Returns roots of quadratic polynomial."""
        from math import sqrt

        if self.numberOfRealRoots() == 0:
            return []
        elif self.numberOfRealRoots() == 1:
            return [int(-self.coefficients[1]/(2*self.coefficients[0]))]
        else:
            rot1 = int((-self.coefficients[1]+\
                sqrt(self.discriminant()))/(2*self.coefficients[0]))
            rot2 = int((-self.coefficients[1]-\
                sqrt(self.discriminant()))/(2*self.coefficients[0]))
            arguments = [rot1, rot2]
            return min(arguments), max(arguments)
