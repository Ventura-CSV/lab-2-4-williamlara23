import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '10 \n 20 \n 30'
    # sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    res = re.search(r'[\w,\W]*Programming[\w,\W]*', lines[0])
    assert res != None
    print(res.group())

    res = re.search(r'[\w,\W]*Python[\w,\W]*', lines[1])
    assert res != None
    print(res.group())

    res = re.search(r'[\w,\W]*Programming[\w,\W]*Python[\w,\W]*', lines[2])
    assert res != None
    print(res.group())
