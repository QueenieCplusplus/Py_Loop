# -*- coding: utf-8 -*-
'''
Created on 2020.3.02
@author: 100900 QueenPy
'''

def fun_func_call(props):


    try: 

        for x in props:
        
            if x == 15:
                print("fifteen")

            elif x == 17:
                print("seventeen")

            else:
                print("not at all")
        
        else:
            return False

    except:
        print("exception raised this time.") 


if __name__ == "__main__":
    oList = [11, 13, 15, 17, 19]
    aList = ["q", "u", "e", "e", "n"]
    fun_func_call(props=aList)

    # execute fun_func_call(props=oList)
    # not at all
    # not at all
    # fifteen
    # seventeen
    # not at all

    # execute fun_func_call(props=aList)
    # not at all
    # not at all
    # not at all
    # not at all
    # not at all
