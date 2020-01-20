anl = int(input('input mark for analysis'))
des = int(input('input mark for design'))
imp = int(input('input mark for implementation'))
eva = int(input('input mark for evaluation'))

mark = (anl+des+imp+eva)
if mark>=80:
    print('A*')
else:
    if mark>=67:
        print('A')
        if mark!=67:
            print('anl ',(67-mark),' marks needed')
    else:
        if mark>=54:
          if mark!=54:
            print('anl ',(54-mark),' marks needed')
            print(B)
        else:
            if mark>=41:
                print(C)
                
            else:
                if mark>=31:
                    print(D)
                else:
                    if mark>=22:
                        print(E)
                    else:
                        if mark>=13:
                            print(F)
                        else:
                            if mark>=4:
                                print(G)
                            else:
                                if mark>=0:
                                    print(U)
