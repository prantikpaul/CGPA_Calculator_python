# #CGPA Calculator

_1st_sem = float(input('Please Enter your 1st_sem result : '))
result = 0
if _1st_sem >=1 and _1st_sem <=4 :
    result +=  _1st_sem  * 5/100 #taking 5% of 1st semester
    _2nd_sem = float(input('Please Enter your 2nd_sem result : '))
    if _2nd_sem >= 1 and _2nd_sem <= 4:
        result += _2nd_sem * 5 / 100 #taking 5% of 2nd semester
        _3rd_sem = float(input('Please Enter your 3rd_sem result : '))
        if _3rd_sem >= 1 and _3rd_sem <= 4:
            result += _3rd_sem * 5 / 100 #taking 5% of 3rd semester
            _4th_sem = float(input('Please Enter your 4th_sem result : '))
            if _4th_sem >= 1 and _4th_sem <= 4:
                result += _4th_sem * 10 / 100 #taking 10% of 4th semester
                _5th_sem = float(input('Please Enter your 5th_sem result : '))
                if _5th_sem >= 1 and _5th_sem <= 4:
                    result += _5th_sem * 15 / 100 #taking 15% of 5th semester
                    _6th_sem = float(input('Please Enter your 6th_sem result : '))
                    if _6th_sem >= 1 and _6th_sem <= 4:
                        result += _6th_sem * 20 / 100 #taking 20% of 6th semester
                        _7th_sem = float(input('Please Enter your 7th_sem result : '))
                        if _7th_sem >= 1 and _7th_sem <= 4:
                            result += _7th_sem * 25 / 100 #taking 25% of 7th semester
                            _8th_sem = float(input('Please Enter your 8th_sem result : '))
                            if _8th_sem >= 1 and _8th_sem <= 4:
                                result += _8th_sem * 15 / 100 #taking 15% of 8th semester
                                print("%.2f" % result)
else:print('Ivalid Result')
