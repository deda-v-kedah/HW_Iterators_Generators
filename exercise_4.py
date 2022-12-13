import types


def flat_generator(list_of_list):
    list_return = []
    list_copy = list_of_list.copy()
    counter = 0
    while list_copy: 
            e = list_copy.pop()
            if type(e) == list: 
                    list_copy.extend(e) 
            else:
                    list_return.append(e) 
    list_return.reverse()

    while counter < len(list_return):
        yield list_return[counter]
        counter += 1



def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

   

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()

