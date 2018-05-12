import re
def demo_string():
    stra='hellD'
    print(stra.replace('he', 'now'))
    strb='     \n\r dw dw d wd \r\n      '
    print(1, strb.lstrip())
    print(2, strb.rstrip())
    print(3, stra.startswith('p'))
    print(5, stra+strb.lstrip())
    print(7, '-'.join(['I', 'love', 'you']))
    print(8,stra.find('l'))
def demo_operation():
    print( 1+2,   5/2,   213*312+231-213*1)
    print(2, True, not True)
def demo_bulit():
    print(1, max(1,2), min(5,3))
    print(2, len('xxxxxasdasd'),len([1,2,3,4,5]))
    print(3, abs(-32+11))
    print(range(1, 10 ,5))
    print(5, dir(list))
    print(7, chr(97),ord('a'))
    print(8, divmod(11,3))
def demo_control():
    score=65
    if(score>99):
        print(1, 'A')
    elif score>80:
        print(2, 'B')
    else :
        print(3, 'C')
    for i in range(0,10,2):

        if i==0:
            pass
        elif i<=5:
          print(3,i)
        if i==6:
            break;
def demo_list():
    lista=[1,2,3] #vector
    print(1,lista)
    listb=['a',1,'c',1.1]
    print(2,listb)
    lista=lista+listb
    print(3,lista,len(lista))
    print(4,'b' in listb)
    listb.insert(1,'www')
    print(5,listb)
    listb.pop(1)
    listb.reverse()
    print(5,listb)
    print(6,listb[3])
    listb=listb*2
    listc=[0]*5
    print(7,listb)
    print(8,listc)
    tuplea=(1,2,3)
def add(x,y):
    return x+y
def demo_dict():
    dicta={1:1, 2:4, 3:9}
    print(1,dicta)
    print(2,dicta.keys())
    print(3,dicta.values())
    print(4,dicta.has_key(3))
    for key,value in dicta.items():
        print 'key-value', key ,value

    dictb={'+': add}
    print 5, dictb['+'](3,5)
    del dicta[1]
    print 6,dicta
def demo_set():
    seta = set((1,2,3))
    setb = set((4,5,2))
    print 3, seta.intersection(setb)
    print 4, seta.union(setb)
    print 5, seta.difference(setb)
    print 6,seta.isdisjoint((1,2))
def demo_re():
    str='adsadsad123asd'
    re.compile('[\d]+')
if __name__ =='__main__':
    print('hgello')
    #demo_string()
    #demo_operation()
    #demo_bulit()
    #demo_control()
    #demo_list()
    #demo_dict()
    #demo_set()