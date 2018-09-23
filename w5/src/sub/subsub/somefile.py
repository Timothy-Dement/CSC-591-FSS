import os
import sys

root = os.path.abspath(os.path.join(os.getcwd().split("src")[0], 'src'))
if root not in sys.path:
    sys.path.append(str(root))

from num import Num

if __name__ == '__main__':
    print(type(Num))
