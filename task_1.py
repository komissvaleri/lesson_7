
class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for el in row:
                print(f"{el:4}", end="")
            print()
        return ''

    def __add__(self, other):
        for el in range(len(self.my_list)):
            for el_2 in range(len(other.my_list[el])):
                self.my_list[el][el_2] = self.my_list[el][el_2] + other.my_list[el][el_2]
        return Matrix.__str__(self)

m_1 = Matrix([[31, 22, 0], [37, 43, 0], [51, 86, 0]])
m_2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
m_2_1 = Matrix([[3, 5, 32, 0], [2, 4, 6, 0], [-1, 64, -8, 0]])
m_3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1], [0, 0, 0, 0]])
print(m_1.__add__(m_2))
print(m_2_1.__add__(m_3))

