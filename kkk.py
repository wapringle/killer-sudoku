import ktest,sys
import argparse
from time import process_time 
parser = argparse.ArgumentParser()
parser.add_argument("-t","--test", help="test number", type=int, default=10)
args = parser.parse_args()
t_start=process_time()
ktest.main(args.test)
t_end=process_time()
print(t_end - t_start)
