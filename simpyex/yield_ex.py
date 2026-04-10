
# In yield keyword is used to create generators,
# which are special types of iterators that allow values to be produced lazily, one at a time,
# instead of returning them all at once.
# https://www.geeksforgeeks.org/python/python-yield-keyword/

class SimpleGenerator:

    # This example demonstrates a simple generator function that yields numbers from 0 up to 4.
    # It shows how yield can be used to produce a sequence one value at a time using a loop.

    def generator(self, number):
        for i in range(number):
            yield i

    def run(self, number):
        for n in self.generator(number):
            print(n, end=' ')
        print()

class GeneratorFunctions:

    # Generator functions behave like normal functions but use yield instead of return.
    # They automatically create __iter__() and __next__() methods,
    # making them iterable objects.

    def generator(self):
        yield "Hello world!!"
        yield "GeeksForGeeks"

    def run(self):
        g = self.generator()
        print(type(g))
        print(next(g))
        print(next(g))

class GeneratingInfiniteSequence:

    # we generate an infinite sequence of numbers using yield.

    def generator(self):
        n = 0
        while True:
            yield n
            n += 1

    def run(self, limit):
        g = self.generator()
        for _ in range(limit):
            print(next(g), end=" ")
        print()

class ExtractingEvenNumbers:

    # we are extracting the even number from the list.

    def generator(self, l):
        for n in l:
            if n % 2 == 0:
                yield n

    def run(self):
        l = [1, 4, 5, 6, 7]
        print(list(self.generator(l)))

class BooleanExpression:

    # yield can be useful in handling large data
    # and searching operations efficiently without requiring repeated scans.

    def generator(self, text, keyword):
        w = text.split()
        for n in w:
            if n == keyword:
                yield True

    def run(self):
        print(sum(self.generator("geeks for geeks", "geeks")))

if __name__ == '__main__':
    print("Example1")
    example1 = SimpleGenerator()
    example1.run(5)

    print("Example2")
    example2 = GeneratorFunctions()
    example2.run()

    print("Example3")
    example3 = GeneratingInfiniteSequence()
    example3.run(10)

    print("Example4")
    example4 = ExtractingEvenNumbers()
    example4.run()

    print("Example5")
    example5 = BooleanExpression()
    example5.run()
