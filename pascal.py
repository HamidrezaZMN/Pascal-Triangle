class PascalTriangle():
#-----------initial functions-----------#

    # number is for debugging
    # pascal is a triangle with maximum lines needed,
    #    and it fastens the calculation
    def __init__(self, number=None, Pascal=None):
        self.number = number
        self.Pascal = Pascal
    
    # setter for number
    @property
    def _number(self):
        return self.number
    @_number.setter
    def setNumber(self, value):
        self.number = value
        
    # setter for Pascal
    @property
    def _pascal(self):
        return self.Pascal
    @_pascal.setter
    def setPascal(self, value):
        self.Pascal = self.pascal(value)

#-----------performer functions-----------#

    # makes a pascal triangle an returns it
    def pascal(self, lines):
        tri = [[0,1,0]]
        for loop in range(lines-1):
            temp = [0]
            last_num = 0
            last_tri = tri[-1]
            for i in range(1, len(last_tri)):
                temp.append(last_tri[i]+last_num)
                last_num = last_tri[i]
            temp.append(0)
            tri.append(temp)
        return [tri[i][1:len(tri[i])-1] for i in range(len(tri))]

    # returns the type of the given number according to the method
    def _type(self, num, method):
        # numbers less than or equal to 0 is not included
        if num>0:
            # Odd or Even
            if method=='ORE':
                    if num%2==1:
                        return 'odd'
                    return 'even'

            # Prime or Composite
            if method=='POC':
                if num==1:
                    return None
                else:
                    for i in range(2,num):
                        if num%i==0:
                            return 'composite'
                    return 'prime'
        else:
            print('You entered the wrong number fool')
            input('\npress enter...')
            import sys
            sys.exit()

    # returns the datas of the given line
    def line_data(self, _pascal):
        n=self.number-1
        data = [0, 0, 0, 0, 0] # odd, even, prime, composite, total
        for j in range(len(_pascal[n])):
            num = _pascal[n][j]
            if self._type(num, 'ORE')=='odd':
                data[0] += 1
            elif self._type(num, 'ORE')=='even':
                data[1] += 1
            if self._type(num, 'POC')=='prime':
                data[2] += 1
            elif self._type(num, 'POC')=='composite':
                data[3] += 1
            data[4] += 1
        return data
    
#-----------printers-----------#

    # prints the status of the given values
    def pstats(self, data):
        n = self.number
        print(n,
              ' : { '
              f'odd: {data[0]}'
              f', | even: {data[1]}'
              f', | prime: {data[2]}'
              f', | composite: {data[3]}'
              f', | total: {data[4]}'
              ' }')
    
    # prints the given pascal triangle
    def printer_total(self, triangle):
        for i in triangle:
            print(' '.join(str(j) for j in i))

    # prints pascal triangle from line A to B
    def printer_AtoB(self, triangle, A, B):
        for i in triangle[A-1:B+1]:
            print(' '.join(str(j) for j in i))

#-----------options-----------#

    # prints the pascal from beginning to the given number of line
    def print_pascal_0toEnd(self, end):
        self.setPascal = end
        self.printer_total(self.Pascal)

    # prints the pascal from line A to B
    def print_pascal_AtoB(self, A, B):
        self.setPascal = B
        self.printer_AtoB(self.Pascal, A, B)

    # prints the status of the given line
    def print_line_stats(self, line):
        self.setPascal = line
        self.setNumber = line
        _v = self.line_data(self.Pascal)
        self.pstats(_v)

    # pirnts the status of line A to B
    def print_lines_stats(self, a, b):
        self.setPascal = b
        for i in range(a, b+1):
            self.setNumber = i
            _v = self.line_data(self.Pascal)
            self.pstats(_v)

#-----------main function-----------#

    # starts the program
    def main(self):
        # input's text
        text = '''choose one of these:
    1) print pascal from the frist to the n-th line
    2) print pascal from the a-th to the b-th line (including a & b)
    3) print status of the n-th line of a pascal triangle
    4) print status of the a-th to the b-th line of a pascal triangle (including a & b)

enter the number: '''
        
        # input
        method = int(input(text).strip())
        
        # option performer
        if method == 1:
            line = int(input('\nenter the number of line: ').strip())
            print('----------------------------------------------------')
            self.print_pascal_0toEnd(line)
        if method == 2:
            lines = input('\nenter the number of lines(example: 2 5): ').strip().split(' ')
            print('----------------------------------------------------')
            lines = list(map(int, lines))
            self.print_pascal_AtoB(*lines)
        if method == 3:
            line = int(input('\nenter the number of line: ').strip())
            print('----------------------------------------------------')
            self.print_line_stats(line)
        if method == 4:
            lines = input('\nenter the number of lines(example: 2 5): ').strip().split(' ')
            print('----------------------------------------------------')
            lines = list(map(int, lines))
            self.print_lines_stats(*lines)

#-----------starter-----------#
triangle = PascalTriangle()
triangle.main()