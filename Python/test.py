class ComplexNum:
    def __init__(self, real, ima):
        self.real_part = real
        self.imag_part = ima

    def get_real(self):
        return self.real_part

    def get_imaginary(self):
        return self.imag_part

    def __repr__(self):
        return f"ComplexNum ({self.get_real()}, {self.get_imaginary()})"

    def __str__(self) -> str:
        return f"{self.get_real()} + {self.get_imaginary()}i"

        pass


class Stack:
    def __init__(self) -> None:
        self.itemlst = []

    def push(self, x):
        self.itemlst.append(x)


cl = ComplexNum(2.0, -1.5)
print(cl)


def bisection(f, a, b, tau):
    if f(a) * f(b) > 0:
        return None
    else:
        while abs(b-a) > tau:
            c = (a+b)/2
            if f(c) == 0:
                return c
            elif f(a) * f(c) < 0:
                b = c
            else:
                a = c
        return (a+b)/2

    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i+1:]
        for p in permutation(remLst):
            l.append([m] + p)
    return l

    while abs(f(c)) > tau:
        if f(c)*f(a) < 0:
            b = c
        else:
            a = c
        c = (a+b)/2
    return c
