class FlatIterator:

    def __init__(self, list_of_list):
        self.list = list_of_list

    def __iter__(self):
        self.list_of_list = self.list.copy()
        self.my_list = []
        self.flag = True
        self.counter_1 = -1
        return self

    def __next__(self):
        
        while self.list_of_list:
            el = self.list_of_list.pop()
            if isinstance(el, list): 
                self.list_of_list += el
            else:
                self.my_list.append(el) 


        if self.flag:
            self.flag = not self.flag
            self.my_list.reverse()

        
        
        if self.counter_1 < len(self.my_list)-1:
            self.counter_1 += 1
            return self.my_list[self.counter_1]
            
        else:
            raise StopIteration


       


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()