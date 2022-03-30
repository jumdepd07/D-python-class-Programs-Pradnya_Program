def myFunction(**kwargs):
    for kw in kwargs:
        print(kw, '-', kwargs[kw])

#if __name__ == "__main__":
myFunction(a = 24, b = 87, c = 3, d = 46)