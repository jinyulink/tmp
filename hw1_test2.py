import hw1_2;

def test_hw1_2():
    print(hw1_2.hw1_2() == 20/(2**14))
    assert hw1_2.hw1_2() == 20/(2**14) or hw1_2.hw1_2() == str(20/(2**14))

test_hw1_2()