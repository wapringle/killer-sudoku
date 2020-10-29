import kl
import copy



case={
    1: (4,[
        (4,(1,(1,2))),
        (9,((2,3),1)),
        (8,[((2,2),2),(2,3)]),
        (7,[(4,(2,2)),(3,3)]),
        (7,[(1,(3,2)),(2,4)]),
        (5,((3,2),4))
        ]),
    3: (9,[
        (13,((1,4),1)),
        (18,[(5,(1,2)),(4,2)]),
        (24,((6,4),1)),
        (20,(1,(2,4))),
        (22,(2,(2,3))),
        (26,[(3,(2,2)),(4,(3,2))]),
        (13,((6,3),2)),
        (17,(9,(2,3))),
        (9,(5,(3,3))),
        (8,(6,(3,2))),
        (11,[((7,2),3),(7,4)]),
        (21,[(3,4),((3,2),5)]),
        (8,[(8,4),((7,2),5)]),
        (8,[(2,5),((1,2),6)]),
        (20,(6,(5,3))),
        (13,(9,(5,2))),
        (7,((3,2),6)),
        (13,[(5,(6,3)),(6,8)]),
        (24,((7,2),(6,2))),
        (18,(1,(7,3))),
        (12,((2,2),7)),
        (17,(4,(7,3))),
        (20,[(9,7),((7,3),8)]),
        (4,(2,(8,2))),
        (11,(3,(8,2))),
        (20,((5,3),9)),
        (8,((8,2),9))
    ]),

9: (9,[(14, [(1, 1), (2, 1), (2, 2)]),
 (18, [(1, 2), (1, 3), (1, 4), (2, 3)]),
 (21, [(1, 5), (2, 5), (3, 5)]),
 (20, [(1, 6), (1, 7), (1, 8), (2, 7)]),
 (18, [(1, 9), (2, 8), (2, 9)]),
 (16, [(2, 4), (3, 3), (3, 4)]),
 (6, [(2, 6), (3, 6), (3, 7)]),
 (12, [(3, 8), (3, 9)]),
 (10, [(3, 1), (3, 2)]),
 (11, [(4, 1), (4, 2), (5, 1), (6, 1)]),
 (22, [(4, 3), (4, 4), (4, 5), (4, 6), (4, 7)]),
 (22, [(4, 8), (4, 9), (5, 9), (6, 9)]),
 (28, [(5, 2), (5, 3), (6, 2), (6, 3)]),
 (25, [(5, 4), (5, 5), (5, 6), (6, 5)]),
 (21, [(5, 7), (5, 8), (6, 7), (6, 8)]),
 (28, [(7, 1), (7, 2), (7, 3), (8, 1), (8, 2)]),
 (9, [(9, 1), (9, 2)]),
 (12, [(6, 4), (7, 4)]),
 (6, [(6, 6), (7, 6)]),
 (16, [(7, 7), (7, 8), (7, 9), (8, 8), (8, 9)]),
 (13, [(9, 8), (9, 9)]),
 (22, [(7, 5), (8, 4), (8, 5), (8, 6)]),
 (35, [(8, 3), (9, 3), (9, 4), (9, 5),(8, 7), (9, 6), (9, 7)]),
 ]),

10: (9,[(15, [(1, 1), (1, 2), (1, 3), (2, 2)]),
 (14, [(1, 4), (2, 3), (2, 4)]),
 (14, [(1, 5), (1, 6), (2, 5)]),
 (22, [(1, 7), (2, 6), (2, 7), (2, 8)]),
 (17, [(1, 8), (1, 9), (2, 9), (3, 9)]),
 (27, [(2, 1), (3, 1), (3, 2), (4, 1)]),
 (7, [(3, 3), (3, 4)]),
 (15, [(3, 5), (3, 6)]),
 (13, [(3, 7), (3, 8), (4, 7), (5, 7)]),
 (19, [(4, 2), (4, 3), (5, 2)]),
 (28, [(4, 4), (4, 5), (5, 3), (5, 4)]),
 (7, [(4, 6), (5, 6)]),
 (19, [(4, 8), (4, 9), (5, 8), (5, 9)]),
 (19, [(5, 1), (6, 1), (7, 1), (7, 2)]),
 (19, [(5, 5), (6, 5), (6, 6), (7, 5), (8, 5)]),
 (9, [(6, 2), (6, 3)]),
 (15, [(6, 4), (7, 3), (7, 4), (8, 4)]),
 (27, [(6, 7), (6, 8), (6, 9), (7, 9)]),
 (29, [(7, 6), (8, 6), (9, 5), (9, 6)]),
 (19, [(7, 7), (7, 8), (8, 7), (8, 8)]),
 (9, [(8, 1), (8, 2), (9, 1)]),
 (23, [(8, 3), (9, 2), (9, 3), (9, 4)]),
 (5, [(9, 7), (9, 8)]),
 (14, [(8, 9), (9, 9)])]
        ),
11: (9,[(36, [(1, 1), (1, 2), (2, 2), (2, 3), (2, 4), (3, 3)]),
 (16, [(1, 3), (1, 4), (1, 5), (1, 6)]),
 (16, [(1, 7), (1, 8), (2, 7)]),
 (33, [(1, 9), (2, 8), (2, 9), (3, 7), (3, 8), (4, 8)]),
 (8, [(2, 1), (3, 1), (3, 2)]),
 (15, [(2, 5), (2, 6), (3, 6)]),
 (14, [(3, 4), (4, 4)]),
 (24, [(3, 5), (4, 5), (4, 6), (5, 5)]),
 (7, [(3, 9), (4, 9), (5, 9)]),
 (13, [(4, 1), (5, 1)]),
 (7, [(4, 2), (4, 3)]),
 (22, [(4, 7), (5, 7), (5, 8)]),
 (11, [(5, 2), (5, 3), (5, 4)]),
 (11, [(5, 6), (6, 5), (6, 6)]),
 (11, [(6, 1), (7, 1)]),
 (16, [(6, 3), (6, 4)]),
 (12, [(6, 7), (6, 8), (6, 9)]),
 (15, [(7, 4), (8, 4), (9, 4), (9, 5)]),
 (13, [(7, 5), (7, 6), (8, 5)]),
 (25, [(7, 7), (8, 6), (8, 7), (8, 8), (9, 8), (9, 9)]),
 (24, [(7, 8), (7, 9), (8, 9)]),
 (16, [(8, 3), (9, 2), (9, 3)]),
 (13, [(9, 6), (9, 7)]),
 (27, [(6, 2), (7, 2), (7, 3), (8, 1), (8, 2), (9, 1)])]),

12: ( 9, [( 36 , [(1, 1), (1, 2), (2, 2), (2, 3), (2, 4), (3, 3)] ),
 ( 16 , [(1, 3), (1, 4), (1, 5), (1, 6)] ),
 ( 16 , [(1, 7), (1, 8), (2, 7)] ),
 ( 33 , [(1, 9), (2, 8), (2, 9), (3, 7), (3, 8), (4, 8)] ),
 ( 8 , [(2, 1), (3, 1), (3, 2)] ),
 ( 15 , [(2, 5), (2, 6), (3, 6)] ),
 ( 14 , [(3, 4), (4, 4)] ),
 ( 24 , [(3, 5), (4, 5), (4, 6), (5, 5)] ),
 ( 7 , [(3, 9), (4, 9), (5, 9)] ),
 ( 13 , [(4, 1), (5, 1)] ),
 ( 7 , [(4, 2), (4, 3)] ),
 ( 11 , [(5, 2), (5, 3), (5, 4)] ),
 ( 11 , [(5, 6), (6, 5), (6, 6)] ),
 ( 12 , [(6, 7), (6, 8), (6, 9)] ),
 ( 22 , [(4, 7), (5, 7), (5, 8)] ),
 ( 11 , [(6, 1), (7, 1)] ),
 ( 27 , [(6, 2), (7, 2), (7, 3), (8, 1), (8, 2), (9, 1)] ),
 ( 16 , [(6, 3), (6, 4)] ),
 ( 16 , [(8, 3), (9, 2), (9, 3)] ),
 ( 15 , [(7, 4), (8, 4), (9, 4), (9, 5)] ),
 ( 13 , [(7, 5), (7, 6), (8, 5)] ),
 ( 25 , [(7, 7), (8, 6), (8, 7), (8, 8), (9, 8), (9, 9)] ),
 ( 24 , [(7, 8), (7, 9), (8, 9)] ),
 ( 13 , [(9, 6), (9, 7)] ),
 ]),

13: (9, [( 20 , [(1, 1), (1, 2), (2, 2)] ),
 ( 13 , [(1, 3), (2, 3), (3, 2), (3, 3)] ),
 ( 13 , [(1, 4), (1, 5)] ),
 ( 18 , [(1, 6), (2, 4), (2, 5), (2, 6)] ),
 ( 12 , [(1, 7), (1, 8), (1, 9)] ),
 ( 18 , [(2, 7), (2, 8), (3, 7), (3, 8)] ),
 ( 15 , [(2, 9), (3, 9)] ),
 ( 12 , [(2, 1), (3, 1)] ),
 ( 17 , [(3, 4), (4, 4), (4, 5)] ),
 ( 6 , [(3, 5), (3, 6), (4, 6)] ),
 ( 11 , [(4, 1), (5, 1), (6, 1)] ),
 ( 28 , [(4, 2), (4, 3), (5, 2), (6, 2)] ),
 ( 22 , [(5, 3), (5, 4), (5, 5), (6, 3)] ),
 ( 14 , [(4, 7), (5, 6), (5, 7)] ),
 ( 24 , [(4, 8), (5, 8), (6, 7), (6, 8)] ),
 ( 10 , [(4, 9), (5, 9), (6, 9)] ),
 ( 12 , [(6, 4), (7, 4), (7, 5)] ),
 ( 17 , [(6, 5), (6, 6), (7, 6)] ),
 ( 5 , [(7, 1), (8, 1)] ),
 ( 17 , [(7, 2), (7, 3), (8, 2), (8, 3)] ),
 ( 22 , [(7, 7), (7, 8), (8, 7), (9, 7)] ),
 ( 11 , [(7, 9), (8, 9)] ),
 ( 12 , [(8, 8), (9, 8), (9, 9)] ),
 ( 23 , [(9, 1), (9, 2), (9, 3)] ),
 ( 24 , [(8, 4), (8, 5), (8, 6), (9, 4)] ),
 ( 9 , [(9, 5), (9, 6)] ),
 ]),
14: (9, [
( 15 , [(1, 1), (1, 2), (2, 2), (3, 2)] ),
 ( 21 , [(1, 3), (1, 4), (1, 5), (2, 3)] ),
 ( 8 , [(1, 6), (2, 6), (3, 6)] ),
 ( 15 , [(1, 7), (1, 8)] ),
 ( 22 , [(1, 9), (2, 9), (3, 9), (4, 9)] ),
 ( 17 , [(2, 1), (3, 1), (4, 1)] ),
 ( 13 , [(2, 4), (2, 5)] ),
 ( 3 , [(2, 7), (3, 7)] ),
 ( 13 , [(2, 8), (3, 8)] ),
 ( 19 , [(3, 3), (3, 4), (4, 3)] ),
 ( 18 , [(3, 5), (4, 4), (4, 5), (4, 6)] ),
 ( 16 , [(4, 7), (4, 8), (5, 8), (5, 9)] ),
 ( 18 , [(4, 2), (5, 1), (5, 2)] ),
 ( 9 , [(5, 3), (5, 4)] ),
 ( 26 , [(5, 5), (5, 6), (5, 7), (6, 6)] ),
 ( 25 , [(6, 1), (7, 1), (8, 1), (8, 2)] ),
 ( 15 , [(6, 2), (6, 3), (7, 2)] ),
 ( 5 , [(6, 4), (6, 5)] ),
 ( 27 , [(6, 7), (7, 6), (7, 7), (8, 7)] ),
 ( 9 , [(6, 8), (6, 9), (7, 8)] ),
 ( 7 , [(7, 3), (7, 4)] ),
 ( 16 , [(7, 5), (8, 5), (8, 6)] ),
 ( 22 , [(7, 9), (8, 8), (8, 9), (9, 9)] ),
 ( 3 , [(9, 1), (9, 2)] ),
 ( 19 , [(8, 3), (8, 4), (9, 3), (9, 4)] ),
 ( 24 , [(9, 5), (9, 6), (9, 7), (9, 8)] ),
]),
15: (9, [ ( 28 , [(1, 1), (1, 2), (2, 1), (2, 2)] ),
 ( 7 , [(1, 3), (2, 3)] ),
 ( 25 , [(1, 4), (1, 5), (1, 6), (2, 4), (2, 6)] ),
 ( 15 , [(1, 7), (2, 7)] ),
 ( 11 , [(1, 8), (1, 9), (2, 8), (2, 9)] ),
 ( 15 , [(2, 5), (3, 5), (4, 5)] ),
 ( 15 , [(3, 3), (3, 4), (4, 3), (4, 4)] ),
 ( 26 , [(3, 6), (3, 7), (4, 6), (4, 7)] ),
 ( 15 , [(3, 8), (3, 9), (4, 9)] ),
 ( 10 , [(4, 8), (5, 7), (5, 8)] ),
 ( 18 , [(3, 1), (3, 2), (4, 1)] ),
 ( 17 , [(4, 2), (5, 2), (5, 3)] ),
 ( 6 , [(5, 1), (6, 1), (6, 2)] ),
 ( 37 , [(5, 4), (5, 5), (5, 6), (6, 5), (7, 5), (8, 5)] ),
 ( 18 , [(6, 6), (6, 7), (7, 6), (7, 7), (7, 8)] ),
 ( 27 , [(6, 3), (6, 4), (7, 2), (7, 3), (7, 4)] ),
 ( 26 , [(7, 1), (8, 1), (8, 2), (9, 1)] ),
 ( 20 , [(5, 9), (6, 8), (6, 9)] ),
 ( 28 , [(7, 9), (8, 8), (8, 9), (9, 9)] ),
 ( 14 , [(8, 6), (8, 7), (9, 7), (9, 8)] ),
 ( 10 , [(8, 3), (8, 4), (9, 2), (9, 3)] ),
 ( 17 , [(9, 4), (9, 5), (9, 6)] ), 
]),
16: (9, [( 27 , [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2)] ),
( 14 , [(1, 4), (1, 5), (2, 3), (2, 4)] ),
( 18 , [(1, 6), (2, 6), (2, 7)] ),
( 4 , [(1, 7), (1, 8)] ),
( 29 , [(1, 9), (2, 8), (2, 9), (3, 9)] ),
( 12 , [(3, 1), (4, 1)] ),
( 18 , [(3, 2), (3, 3), (3, 4), (4, 3)] ),
( 12 , [(2, 5), (3, 5), (4, 5)] ),
( 22 , [(3, 6), (4, 6), (5, 6), (6, 6)] ),
( 20 , [(3, 7), (3, 8), (4, 7), (4, 8)] ),
( 15 , [(4, 9), (5, 9)] ),
( 9 , [(4, 2), (5, 2), (5, 3)] ),
( 29 , [(4, 4), (5, 4), (5, 5), (6, 4), (7, 4)] ),
( 14 , [(5, 7), (5, 8), (6, 8)] ),
( 4 , [(6, 9), (7, 9)] ),
( 21 , [(6, 7), (7, 6), (7, 7), (7, 8)] ),
( 19 , [(6, 5), (7, 5), (8, 5)] ),
( 16 , [(5, 1), (6, 1)] ),
( 19 , [(6, 2), (6, 3), (7, 2), (7, 3)] ),
( 21 , [(7, 1), (8, 1), (8, 2), (9, 1)] ),
( 10 , [(8, 3), (8, 4), (9, 4)] ),
( 12 , [(9, 2), (9, 3)] ),
( 17 , [(8, 6), (8, 7), (9, 5), (9, 6)] ),
( 23 , [(8, 8), (8, 9), (9, 7), (9, 8), (9, 9)] ),
]),
17: (9, [
( 6 , [(1, 1), (1, 2)] ),
 ( 17 , [(1, 3), (2, 3)] ),
 ( 7 , [(1, 4), (2, 4)] ),
 ( 18 , [(1, 5), (2, 5), (3, 5)] ),
 ( 26 , [(2, 1), (3, 1), (4, 1), (5, 1)] ),
 ( 19 , [(2, 2), (3, 2), (4, 2), (5, 2)] ),
 ( 11 , [(2, 6), (2, 7)] ),
 ( 21 , [(3, 3), (3, 4), (4, 3), (4, 4)] ),    
 ( 16 , [(3, 6), (3, 7), (4, 7)] ),    
 ( 9 , [(3, 8), (4, 8)] ),    
 ( 39 , [(1, 6), (1, 7), (1, 8), (1, 9), (2, 8), (2, 9), (3, 9), (4, 9)] ),    
 ( 13 , [(4, 5), (4, 6), (5, 5), (5, 6)] ),    
 ( 25 , [(5, 3), (6, 3), (7, 3), (7, 4), (7, 5)] ),    
 ( 20 , [(5, 4), (6, 4), (6, 5)] ),    
 ( 14 , [(6, 6), (6, 7), (7, 6), (7, 7)] ),    
 ( 16 , [(5, 7), (5, 8), (5, 9)] ),    
 ( 7 , [(6, 8), (6, 9)] ),
 ( 7 , [(6, 1), (6, 2)] ),
 ( 39 , [(7, 1), (7, 2), (8, 1), (8, 2), (8, 3), (9, 1), (9, 2), (9, 3)] ),    
 ( 6 , [(8, 4), (9, 4)] ),    
 ( 20 , [(8, 5), (8, 6), (8, 7), (8, 8)] ),    
 ( 17 , [(7, 8), (7, 9)] ),    
 ( 8 , [(8, 9), (9, 9)] ),
 ( 24 , [(9, 5), (9, 6), (9, 7), (9, 8)] ),
])
}



caseno=17


def dbg(*kargs):
#    print(*kargs)
    return


def solve():
    zz=kl.KillerSudoku(case[caseno][0])
    zz.load           (case[caseno][1])
    return zz


def main():

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--test", help="test number", type=int, default=15)
    parser.add_argument("-d","--debug", help="debug", action="store_true")
    args = parser.parse_args()
    cc=args.test
    kl.debug=args.debug
    zz=kl.KillerSudoku(case[cc][0])
    try:
        zz.load(case[cc][1])
    except Exception as e:
        print(e.args)
        return 1
    
    solution=kl.doit(zz)
    if solution:
        #import pprint
        #pprint.pprint(solution)
        for r in zz.board_size:
            rw=" ".join([str(solution[(r,c)]) for c in zz.board_size])
            print(rw)
        return 0


    

if __name__ == '__main__':
    main()
    
