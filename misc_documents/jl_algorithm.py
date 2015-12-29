import numpy as np

##


# we have a profit m x n matrix of each factory combined with every customer
# [a1, a2, a3, ..., a60]
# [b1, b2, b3, ..., b60]
# [c1, c2, c3, ..., c60]
# [d1, d2, d3, ..., d60]
# [e1, e2, e3, ..., e60]
#
# then we have the weight 1 x n matrix of each customer
# [w1, w2, w3, ..., w60]
#
#
# 
# first iteration phase(inital assignment): opportunity_cost +=1
# assign sources to customers with the priority to those if assigned 
# 	otherwise would suffer the largest difference in profit. (largest opportunity cost)
# if initial assignment satisfies all customers, set is optimal.
# 
# if not, begin second iterations 
# second iteration phase(switching phase): opportunity cost -=1
# free up allocations that have the lowest opportunity cost (make obsolete all allocation possibiliy exceeding the opportunity 
#	cost limit) and find all possible combinations in relevant space
# 
# USE NUMPY SCIPY ARRAY
#facA = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]
#facB = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10]
#facC = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
#facD = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10]
#facE = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]

#def max2(numbers):
#    count = 0
#    m1 = m2 = float('-inf')
#    for x in numbers:
#        count += 1
#        if x > m2:
#            if x >= m1:
#                m1, m2 = x, m1            
#            else:
#                m2 = x
#    return m2 if count >= 2 
#	else None
	
# cus001 = [a1,b1,c1,d1,e1]
# cus002 = [a2,b2,c2,d2,e2]
# cus003 = [a3,b3,c3,d3,e3]
# cus004 = [a4,b4,c4,d4,e4]
# cus005 = [a5,b5,c5,d5,e5]
# cus006 = [a6,b6,c6,d6,e6]
# cus007 = [a7,b7,c7,d7,e7]
# cus008 = [a8,b8,c8,d8,e8]
# cus009 = [a9,b9,c9,d9,e9]
# cus010 = [a10,b10,c10,d10,e10]

# op1cost001 = max(cus001) - max2(cus001)
# op1cost002 = max(cus002) - max2(cus002)
# op1cost003 = max(cus003) - max2(cus003)
# op1cost004 = max(cus004) - max2(cus004)
# op1cost005 = max(cus005) - max2(cus005)
# op1cost006 = max(cus006) - max2(cus006)
# op1cost007 = max(cus007) - max2(cus007)
# op1cost008 = max(cus008) - max2(cus008)
# op1cost009 = max(cus009) - max2(cus009)
# op1cost010 = max(cus010) - max2(cus010)



##for x is facA[1] =


# cost matrix of each factory
# Ansan - A, Daesan - B, Dangjin - C, Ulsan - D, Yeosu - E

def max2(numbers):
    count = 0
    m1 = m2 = float('-inf')
    for x in numbers:
        count += 1
        if x > m2:
            if x >= m1:
                m1, m2 = x, m1
            else:
                m2 = x
    return m2 if count >= 2 else None

#############################################

def max3(numbers):
    count = 0
    m1 = m2 = m3 = float('-inf')
    for x in numbers:
        count +=1
        if x > m3:
            if x > m2:
                if x >= m1:
                    m1, m2, m3 = x, m1, m2
                else:
                    m3 = x
    return m3 if count >=3 else none

############################################
cost_per_km = 20

### capacity of each factory
CAP_facA = 10000
CAP_facB = 2000
CAP_facC = 4000
CAP_facD = 20000
CAP_facE = 45000

### demand of each customer
W1 = 4000
W2 = 1000
W3 = 4000
W4 = 10000
W5 = 7500
W6 = 2000
W7 = 15000
W8 = 9500
W9 = 8000
W10 = 12000

# price of good to each customer

P1 = 300
P2 = 300
P3 = 300
P4 = 300
P5 = 300
P6 = 300
P7 = 300
P8 = 300
P9 = 300
P10 = 300

sourceA = 120
sourceB = 100
sourceC = 150
sourceD = 170
sourceE = 220

distance_a1 = 1
distance_a2 = 3
distance_a3 = 5
distance_a4 = 5
distance_a5 = 8
distance_a6 = 8
distance_a7 = 8
distance_a8 = 5
distance_a9 = 5
distance_a10 = 9

distance_b1 = 1
distance_b2 = 9
distance_b3 = 1
distance_b4 = 1
distance_b5 = 1
distance_b6 = 3
distance_b7 = 4
distance_b8 = 7
distance_b9 = 6
distance_b10 = 5

distance_c1 = 4
distance_c2 = 4
distance_c3 = 9
distance_c4 = 8
distance_c5 = 1
distance_c6 = 2
distance_c7 = 1
distance_c8 = 4
distance_c9 = 4
distance_c10 = 5

distance_d1 = 1
distance_d2 = 5
distance_d3 = 2
distance_d4 = 3
distance_d5 = 5
distance_d6 = 1
distance_d7 = 1
distance_d8 = 1
distance_d9 = 9
distance_d10 = 1

distance_e1 = 1
distance_e2 = 2
distance_e3 = 4
distance_e4 = 3
distance_e5 = 6
distance_e6 = 1
distance_e7 = 1
distance_e8 = 2
distance_e9 = 3
distance_e10 = 1




###

fA1 = 0
fA2 = 0
fA3 = 0
fA4 = 0
fA5 = 0
fA6 = 0
fA7 = 0
fA8 = 0
fA9 = 0
fA10 = 0
fB1 = 0
fB2 = 0
fB3 = 0
fB4 = 0
fB5 = 0
fB6 = 0
fB7 = 0
fB8 = 0
fB9 = 0
fB10 = 0
fC1 = 0
fC2 = 0
fC3 = 0
fC4 = 0
fC5 = 0
fC6 = 0
fC7 = 0
fC8 = 0
fC9 = 0
fC10 = 0
fD1 = 0
fD2 = 0
fD3 = 0
fD4 = 0
fD5 = 0
fD6 = 0
fD7 = 0
fD8 = 0
fD9 = 0
fD10 = 0
fE1 = 0
fE2 = 0
fE3 = 0
fE4 = 0
fE5 = 0
fE6 = 0
fE7 = 0
fE8 = 0
fE9 = 0
fE10 = 0

### Indicator Xij = 0 or 1
Xa1 = 0
Xb1 = 0
Xc1 = 0
Xd1 = 0
Xe1 = 0
Xa2 = 0
Xb2 = 0
Xc2 = 0
Xd2 = 0
Xe2 = 0
Xa3 = 0
Xb3 = 0
Xc3 = 0
Xd3 = 0
Xe3 = 0
Xa4 = 0
Xb4 = 0
Xc4 = 0
Xd4 = 0
Xe4 = 0
Xa5 = 0
Xb5 = 0
Xc5 = 0
Xd5 = 0
Xe5 = 0
Xa6= 0
Xb6 = 0
Xc6 = 0
Xd6 = 0
Xe6 = 0
Xa7 = 0
Xb7 = 0
Xc7 = 0
Xd7 = 0
Xe7 = 0
Xa8 = 0
Xb8 = 0
Xc8 = 0
Xd8 = 0
Xe8 = 0
Xa9 = 0
Xb9 = 0
Xc9 = 0
Xd9 = 0
Xe9 = 0
Xa10 = 0
Xb10 = 0
Xc10 = 0
Xd10 = 0
Xe10 = 0

### price function of each (customer, factory) pair
a1 = W1 * ((P1 - sourceA) - (distance_a1 * cost_per_km))
a2 = W2 * ((P2 - sourceA) - (distance_a2 * cost_per_km))
a3 = W3 * ((P3 - sourceA) - (distance_a3 * cost_per_km))
a4 = W4 * ((P4 - sourceA) - (distance_a4 * cost_per_km))
a5 = W5 * ((P5 - sourceA) - (distance_a5 * cost_per_km))
a6 = W6 * ((P6 - sourceA) - (distance_a6 * cost_per_km))
a7 = W7 * ((P7 - sourceA) - (distance_a7 * cost_per_km))
a8 = W8 * ((P8 - sourceA) - (distance_a8 * cost_per_km))
a9 = W9 * ((P9 - sourceA) - (distance_a9 * cost_per_km))
a10 = W10 * ((P10 - sourceA) - (distance_a10 * cost_per_km))

b1 = W1 * ((P1 - sourceB) - (distance_b1 * cost_per_km))
b2 = W2 * ((P2 - sourceB) - (distance_b2 * cost_per_km))
b3 = W3 * ((P3 - sourceB) - (distance_b3 * cost_per_km))
b4 = W4 * ((P4 - sourceB) - (distance_b4 * cost_per_km))
b5 = W5 * ((P5 - sourceB) - (distance_b5 * cost_per_km))
b6 = W6 * ((P6 - sourceB) - (distance_b6 * cost_per_km))
b7 = W7 * ((P7 - sourceB) - (distance_b7 * cost_per_km))
b8 = W8 * ((P8 - sourceB) - (distance_b8 * cost_per_km))
b9 = W9 * ((P9 - sourceB) - (distance_b9 * cost_per_km))
b10 = W10 * ((P10 - sourceB) - (distance_b10 * cost_per_km))

c1 = W1 * ((P1 - sourceC) - (distance_c1 * cost_per_km))
c2 = W2 * ((P2 - sourceC) - (distance_c2 * cost_per_km))
c3 = W3 * ((P3 - sourceC) - (distance_c3 * cost_per_km))
c4 = W4 * ((P4 - sourceC) - (distance_c4 * cost_per_km))
c5 = W5 * ((P5 - sourceC) - (distance_c5 * cost_per_km))
c6 = W6 * ((P6 - sourceC) - (distance_c6 * cost_per_km))
c7 = W7 * ((P7 - sourceC) - (distance_c7 * cost_per_km))
c8 = W8 * ((P8 - sourceC) - (distance_c8 * cost_per_km))
c9 = W9 * ((P9 - sourceC) - (distance_c9 * cost_per_km))
c10 = W10 * ((P10 - sourceC) - (distance_c10 * cost_per_km))

d1 = W1 * ((P1 - sourceD) - (distance_d1 * cost_per_km))
d2 = W2 * ((P2 - sourceD) - (distance_d2 * cost_per_km))
d3 = W3 * ((P3 - sourceD) - (distance_d3 * cost_per_km))
d4 = W4 * ((P4 - sourceD) - (distance_d4 * cost_per_km))
d5 = W5 * ((P5 - sourceD) - (distance_d5 * cost_per_km))
d6 = W6 * ((P6 - sourceD) - (distance_d6 * cost_per_km))
d7 = W7 * ((P7 - sourceD) - (distance_d7 * cost_per_km))
d8 = W8 * ((P8 - sourceD) - (distance_d8 * cost_per_km))
d9 = W9 * ((P9 - sourceD) - (distance_d9 * cost_per_km))
d10 = W10 * ((P10 - sourceD) - (distance_d10 * cost_per_km))

e1 = W1 * ((P1 - sourceE) - (distance_e1 * cost_per_km))
e2 = W2 * ((P2 - sourceE) - (distance_e2 * cost_per_km))
e3 = W3 * ((P3 - sourceE) - (distance_e3 * cost_per_km))
e4 = W4 * ((P4 - sourceE) - (distance_e4 * cost_per_km))
e5 = W5 * ((P5 - sourceE) - (distance_e5 * cost_per_km))
e6 = W6 * ((P6 - sourceE) - (distance_e6 * cost_per_km))
e7 = W7 * ((P7 - sourceE) - (distance_e7 * cost_per_km))
e8 = W8 * ((P8 - sourceE) - (distance_e8 * cost_per_km))
e9 = W9 * ((P9 - sourceE) - (distance_e9 * cost_per_km))
e10 = W10 * ((P10 - sourceE) - (distance_e10 * cost_per_km))

### possible assignments for each customer
cus001 = [a1,b1,c1,d1,e1]
cus002 = [a2,b2,c2,d2,e2]
cus003 = [a3,b3,c3,d3,e3]
cus004 = [a4,b4,c4,d4,e4]
cus005 = [a5,b5,c5,d5,e5]
cus006 = [a6,b6,c6,d6,e6]
cus007 = [a7,b7,c7,d7,e7]
cus008 = [a8,b8,c8,d8,e8]
cus009 = [a9,b9,c9,d9,e9]
cus010 = [a10,b10,c10,d10,e10]

C001 = np.array(cus001)
C002 = np.array(cus002)
C003 = np.array(cus003)
C004 = np.array(cus004)
C005 = np.array(cus005)
C006 = np.array(cus006)
C007 = np.array(cus007)
C008 = np.array(cus008)
C009 = np.array(cus009)
C010 = np.array(cus010)


cuspriority = []





# customer 1 (C001 max-only)
#   facA.append('x')
#   facB.append('x')
#   facC.append('x')
#   facD.append('x')
#   facE.append('x')

### opportunity cost of moving from best choice to second best choice
op1cost001 = max(cus001) - max2(cus001)
op1cost002 = max(cus002) - max2(cus002)
op1cost003 = max(cus003) - max2(cus003)
op1cost004 = max(cus004) - max2(cus004)
op1cost005 = max(cus005) - max2(cus005)
op1cost006 = max(cus006) - max2(cus006)
op1cost007 = max(cus007) - max2(cus007)
op1cost008 = max(cus008) - max2(cus008)
op1cost009 = max(cus009) - max2(cus009)
op1cost010 = max(cus010) - max2(cus010)

op_cost = [op1cost001, op1cost002, op1cost003, op1cost004, op1cost005, op1cost006, op1cost007, op1cost008, op1cost009, op1cost010]

facA = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]
facB = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10]
facC = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
facD = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10]
facE = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]



WfacA = np.array([W1 * Xa1, W2 * Xa2, W3 * Xa3, W4 * Xa4, W5 * Xa5, W6 * Xa6, W7 * Xa7, W8 * Xa8, W9 * Xa9, W10 * Xa10])
WfacB = np.array([W1 * Xb1, W2 * Xb2, W3 * Xb3, W4 * Xb4, W5 * Xb5, W6 * Xb6, W7 * Xb7, W8 * Xb8, W9 * Xb9, W10 * Xb10])
WfacC = np.array([W1 * Xc1, W2 * Xc2, W3 * Xc3, W4 * Xc4, W5 * Xc5, W6 * Xc6, W7 * Xc7, W8 * Xc8, W9 * Xc9, W10 * Xc10])
WfacD = np.array([W1 * Xd1, W2 * Xd2, W3 * Xd3, W4 * Xd4, W5 * Xd5, W6 * Xd6, W7 * Xd7, W8 * Xd8, W9 * Xd9, W10 * Xd10])
WfacE = np.array([W1 * Xe1, W2 * Xe2, W3 * Xe3, W4 * Xe4, W5 * Xe5, W6 * Xe6, W7 * Xe7, W8 * Xe8, W9 * Xe9, W10 * Xe10])


print op_cost
print \

op_cost.sort(reverse= True)

print op_cost
print \

Xset1 = [Xa1, Xb1, Xc1, Xd1, Xe1]
Xset2 = [Xa2, Xb2, Xc2, Xd2, Xe2]
Xset3 = [Xa3, Xb3, Xc3, Xd3, Xe3]
Xset4 = [Xa4, Xb4, Xc4, Xd4, Xe4]
Xset5 = [Xa5, Xb5, Xc5, Xd5, Xe5]
Xset6 = [Xa6, Xb6, Xc6, Xd6, Xe6]
Xset7 = [Xa7, Xb7, Xc7, Xd7, Xe7]
Xset8 = [Xa8, Xb8, Xc8, Xd8, Xe8]
Xset9 = [Xa9, Xb9, Xc9, Xd9, Xe9]
Xset10 = [Xa10, Xb10, Xc10, Xd10, Xe10]

assign_set_vert = np.array([Xset1, Xset2, Xset3, Xset4, Xset5, Xset6, Xset7, Xset8, Xset9, Xset10])

print assign_set_vert

##################################################################################################
for i in assign_set_vert:
    while sum(i) < 1:
        if op1cost001 - 0.0001 < op_cost[0] < op1cost001 + 0.0001:
            for cus in cus001:
                if max(cus001) - 0.0001 < cus < max(cus001) + 0.0001:
                    if cus is facA[0]:
                        Xa1 = 1
                    elif cus is facB[0]:
                        Xb1 = 1
                    elif cus is facC[0]:
                        Xc1 = 1
                    elif cus is facD[0]:
                        Xd1 = 1
                    elif cus is facE[0]:
                        Xe1 = 1

        elif op1cost002 - 0.0001 < op_cost[0] < op1cost002 + 0.0001:
            for cus in cus002:
                if max(cus002) - 0.0001 < cus < max(cus002) + 0.0001:
                    if cus is facA[1]:
                        Xa2 = 1
                    elif cus is facB[1]:
                        Xb2 = 1
                    elif cus is facC[1]:
                        Xc2 = 1
                    elif cus is facD[1]:
                        Xd2 = 1
                    elif cus is facE[1]:
                        Xe2 = 1

        elif op1cost003 - 0.0001 < op_cost[0] < op1cost003 + 0.0001:
            for cus in cus003:
                if max(cus003) - 0.0001 < cus < max(cus003) + 0.0001:
                    if cus is facA[2]:
                        Xa3 = 1
                    elif cus is facB[2]:
                        Xb3 = 1
                    elif cus is facC[2]:
                        Xc3 = 1
                    elif cus is facD[2]:
                        Xd3 = 1
                    elif cus is facE[2]:
                        Xe3 = 1

        elif op1cost004 - 0.0001 < op_cost[0] < op1cost004 + 0.0001:
            for cus in cus004:
                if max(cus004) - 0.0001 < cus < max(cus004) + 0.0001:
                    if cus is facA[3]:
                        Xa4 = 1
                    elif cus is facB[3]:
                        Xb4 = 1
                    elif cus is facC[3]:
                        Xc4 = 1
                    elif cus is facD[3]:
                        Xd4 = 1
                    elif cus is facE[3]:
                        Xe4 = 1

        elif op1cost005 - 0.0001 < op_cost[0] < op1cost005 + 0.0001:
            for cus in cus005:
                if max(cus005) - 0.0001 < cus < max(cus005) + 0.0001:
                    if cus is facA[4]:
                        Xa5 = 1
                    elif cus is facB[4]:
                        Xb5 = 1
                    elif cus is facC[4]:
                        Xc5 = 1
                    elif cus is facD[4]:
                        Xd5 = 1
                    elif cus is facE[4]:
                        Xe5 = 1

        elif op1cost006 - 0.0001 < op_cost[0] < op1cost006 + 0.0001:
            for cus in cus006:
                if max(cus006) - 0.0001 < cus < max(cus006) + 0.0001:
                    if cus is facA[5]:
                        Xa6 = 1
                    elif cus is facB[5]:
                        Xb6 = 1
                    elif cus is facC[5]:
                        Xc6 = 1
                    elif cus is facD[5]:
                        Xd6 = 1
                    elif cus is facE[5]:
                        Xe6 = 1

        elif op1cost007 - 0.0001 < op_cost[0] < op1cost007 + 0.0001:
            for cus in cus007:
                if max(cus007) - 0.0001 < cus < max(cus007) + 0.0001:
                    if cus is facA[6]:
                        Xa7 = 1
                    elif cus is facB[6]:
                        Xb7 = 1
                    elif cus is facC[6]:
                        Xc7 = 1
                    elif cus is facD[6]:
                        Xd7 = 1
                    elif cus is facE[6]:
                        Xe7 = 1

        elif op1cost008 - 0.0001 < op_cost[0] < op1cost008 + 0.0001:
            for cus in cus008:
                if max(cus008) - 0.0001 < cus < max(cus008) + 0.0001:
                    if cus is facA[7]:
                        Xa8 = 1
                    elif cus is facB[7]:
                        Xb8 = 1
                    elif cus is facC[7]:
                        Xc8 = 1
                    elif cus is facD[7]:
                        Xd8 = 1
                    elif cus is facE[7]:
                        Xe8 = 1

        elif op1cost009 - 0.0001 < op_cost[0] < op1cost009 + 0.0001:
            for cus in cus009:
                if max(cus009) - 0.0001 < cus < max(cus009) + 0.0001:
                    if cus is facA[8]:
                        Xa9 = 1
                    elif cus is facB[8]:
                        Xb9 = 1
                    elif cus is facC[8]:
                        Xc9 = 1
                    elif cus is facD[8]:
                        Xd9 = 1
                    elif cus is facE[8]:
                        Xe9 = 1

        elif op1cost010 - 0.0001 < op_cost[0] < op1cost010 + 0.0001:
            for cus in cus010:
                if max(cus010) - 0.0001 < cus < max(cus010) + 0.0001:
                    if cus is facA[9]:
                        Xa10 = 1
                    elif cus is facB[9]:
                        Xb10 = 1
                    elif cus is facC[9]:
                        Xc10 = 1
                    elif cus is facD[9]:
                        Xd10 = 1
                    elif cus is facE[9]:
                        Xe10 = 1

        ##################################################################################################

        if op1cost001 - 0.0001 < op_cost[1] < op1cost001 + 0.0001:
            for cus in cus001:
                if max(cus001) - 0.0001 < cus < max(cus001) + 0.0001:
                    if cus is facA[0]:
                        Xa1 = 1
                    elif cus is facB[0]:
                        Xb1 = 1
                    elif cus is facC[0]:
                        Xc1 = 1
                    elif cus is facD[0]:
                        Xd1 = 1
                    elif cus is facE[0]:
                        Xe1 = 1

        elif op1cost002 - 0.0001 < op_cost[1] < op1cost002 + 0.0001:
            for cus in cus002:
                if max(cus002) - 0.0001 < cus < max(cus002) + 0.0001:
                    if cus is facA[1]:
                        Xa2 = 1
                    elif cus is facB[1]:
                        Xb2 = 1
                    elif cus is facC[1]:
                        Xc2 = 1
                    elif cus is facD[1]:
                        Xd2 = 1
                    elif cus is facE[1]:
                        Xe2 = 1

        elif op1cost003 - 0.0001 < op_cost[1] < op1cost003 + 0.0001:
            for cus in cus003:
                if max(cus003) - 0.0001 < cus < max(cus003) + 0.0001:
                    if cus is facA[2]:
                        Xa3 = 1
                    elif cus is facB[2]:
                        Xb3 = 1
                    elif cus is facC[2]:
                        Xc3 = 1
                    elif cus is facD[2]:
                        Xd3 = 1
                    elif cus is facE[2]:
                        Xe3 = 1

        elif op1cost004 - 0.0001 < op_cost[1] < op1cost004 + 0.0001:
            for cus in cus004:
                if max(cus004) - 0.0001 < cus < max(cus004) + 0.0001:
                    if cus is facA[3]:
                        Xa4 = 1
                    elif cus is facB[3]:
                        Xb4 = 1
                    elif cus is facC[3]:
                        Xc4 = 1
                    elif cus is facD[3]:
                        Xd4 = 1
                    elif cus is facE[3]:
                        Xe4 = 1

        elif op1cost005 - 0.0001 < op_cost[1] < op1cost005 + 0.0001:
            for cus in cus005:
                if max(cus005) - 0.0001 < cus < max(cus005) + 0.0001:
                    if cus is facA[4]:
                        Xa5 = 1
                    elif cus is facB[4]:
                        Xb5 = 1
                    elif cus is facC[4]:
                        Xc5 = 1
                    elif cus is facD[4]:
                        Xd5 = 1
                    elif cus is facE[4]:
                        Xe5 = 1

        elif op1cost006 - 0.0001 < op_cost[1] < op1cost006 + 0.0001:
            for cus in cus006:
                if max(cus006) - 0.0001 < cus < max(cus006) + 0.0001:
                    if cus is facA[5]:
                        Xa6 = 1
                    elif cus is facB[5]:
                        Xb6 = 1
                    elif cus is facC[5]:
                        Xc6 = 1
                    elif cus is facD[5]:
                        Xd6 = 1
                    elif cus is facE[5]:
                        Xe6 = 1

        elif op1cost007 - 0.0001 < op_cost[1] < op1cost007 + 0.0001:
            for cus in cus007:
                if max(cus007) - 0.0001 < cus < max(cus007) + 0.0001:
                    if cus is facA[6]:
                        Xa7 = 1
                    elif cus is facB[6]:
                        Xb7 = 1
                    elif cus is facC[6]:
                        Xc7 = 1
                    elif cus is facD[6]:
                        Xd7 = 1
                    elif cus is facE[6]:
                        Xe7 = 1

        elif op1cost008 - 0.0001 < op_cost[1] < op1cost008 + 0.0001:
            for cus in cus008:
                if max(cus008) - 0.0001 < cus < max(cus008) + 0.0001:
                    if cus is facA[7]:
                        Xa8 = 1
                    elif cus is facB[7]:
                        Xb8 = 1
                    elif cus is facC[7]:
                        Xc8 = 1
                    elif cus is facD[7]:
                        Xd8 = 1
                    elif cus is facE[7]:
                        Xe8 = 1

        elif op1cost009 - 0.0001 < op_cost[1] < op1cost009 + 0.0001:
            for cus in cus009:
                if max(cus009) - 0.0001 < cus < max(cus009) + 0.0001:
                    if cus is facA[8]:
                        Xa9 = 1
                    elif cus is facB[8]:
                        Xb9 = 1
                    elif cus is facC[8]:
                        Xc9 = 1
                    elif cus is facD[8]:
                        Xd9 = 1
                    elif cus is facE[8]:
                        Xe9 = 1

        elif op1cost010 - 0.0001 < op_cost[1] < op1cost010 + 0.0001:
            for cus in cus010:
                if max(cus010) - 0.0001 < cus < max(cus010) + 0.0001:
                    if cus is facA[9]:
                        Xa10 = 1
                    elif cus is facB[9]:
                        Xb10 = 1
                    elif cus is facC[9]:
                        Xc10 = 1
                    elif cus is facD[9]:
                        Xd10 = 1
                    elif cus is facE[9]:
                        Xe10 = 1

        ##################################################################################################

        if op1cost001 - 0.0001 < op_cost[2] < op1cost001 + 0.0001:
            for cus in cus001:
                if max(cus001) - 0.0001 < cus < max(cus001) + 0.0001:
                    if cus is facA[0]:
                        Xa1 = 1
                    elif cus is facB[0]:
                        Xb1 = 1
                    elif cus is facC[0]:
                        Xc1 = 1
                    elif cus is facD[0]:
                        Xd1 = 1
                    elif cus is facE[0]:
                        Xe1 = 1

        elif op1cost002 - 0.0001 < op_cost[2] < op1cost002 + 0.0001:
            for cus in cus002:
                if max(cus002) - 0.0001 < cus < max(cus002) + 0.0001:
                    if cus is facA[1]:
                        Xa2 = 1
                    elif cus is facB[1]:
                        Xb2 = 1
                    elif cus is facC[1]:
                        Xc2 = 1
                    elif cus is facD[1]:
                        Xd2 = 1
                    elif cus is facE[1]:
                        Xe2 = 1

        elif op1cost003 - 0.0001 < op_cost[2] < op1cost003 + 0.0001:
            for cus in cus003:
                if max(cus003) - 0.0001 < cus < max(cus003) + 0.0001:
                    if cus is facA[2]:
                        Xa3 = 1
                    elif cus is facB[2]:
                        Xb3 = 1
                    elif cus is facC[2]:
                        Xc3 = 1
                    elif cus is facD[2]:
                        Xd3 = 1
                    elif cus is facE[2]:
                        Xe3 = 1

        elif op1cost004 - 0.0001 < op_cost[2] < op1cost004 + 0.0001:
            for cus in cus004:
                if max(cus004) - 0.0001 < cus < max(cus004) + 0.0001:
                    if cus is facA[3]:
                        Xa4 = 1
                    elif cus is facB[3]:
                        Xb4 = 1
                    elif cus is facC[3]:
                        Xc4 = 1
                    elif cus is facD[3]:
                        Xd4 = 1
                    elif cus is facE[3]:
                        Xe4 = 1

        elif op1cost005 - 0.0001 < op_cost[2] < op1cost005 + 0.0001:
            for cus in cus005:
                if max(cus005) - 0.0001 < cus < max(cus005) + 0.0001:
                    if cus is facA[4]:
                        Xa5 = 1
                    elif cus is facB[4]:
                        Xb5 = 1
                    elif cus is facC[4]:
                        Xc5 = 1
                    elif cus is facD[4]:
                        Xd5 = 1
                    elif cus is facE[4]:
                        Xe5 = 1

        elif op1cost006 - 0.0001 < op_cost[2] < op1cost006 + 0.0001:
            for cus in cus006:
                if max(cus006) - 0.0001 < cus < max(cus006) + 0.0001:
                    if cus is facA[5]:
                        Xa6 = 1
                    elif cus is facB[5]:
                        Xb6 = 1
                    elif cus is facC[5]:
                        Xc6 = 1
                    elif cus is facD[5]:
                        Xd6 = 1
                    elif cus is facE[5]:
                        Xe6 = 1

        elif op1cost007 - 0.0001 < op_cost[2] < op1cost007 + 0.0001:
            for cus in cus007:
                if max(cus007) - 0.0001 < cus < max(cus007) + 0.0001:
                    if cus is facA[6]:
                        Xa7 = 1
                    elif cus is facB[6]:
                        Xb7 = 1
                    elif cus is facC[6]:
                        Xc7 = 1
                    elif cus is facD[6]:
                        Xd7 = 1
                    elif cus is facE[6]:
                        Xe7 = 1

        elif op1cost008 - 0.0001 < op_cost[2] < op1cost008 + 0.0001:
            for cus in cus008:
                if max(cus008) - 0.0001 < cus < max(cus008) + 0.0001:
                    if cus is facA[7]:
                        Xa8 = 1
                    elif cus is facB[7]:
                        Xb8 = 1
                    elif cus is facC[7]:
                        Xc8 = 1
                    elif cus is facD[7]:
                        Xd8 = 1
                    elif cus is facE[7]:
                        Xe8 = 1

        elif op1cost009 - 0.0001 < op_cost[2] < op1cost009 + 0.0001:
            for cus in cus009:
                if max(cus009) - 0.0001 < cus < max(cus009) + 0.0001:
                    if cus is facA[8]:
                        Xa9 = 1
                    elif cus is facB[8]:
                        Xb9 = 1
                    elif cus is facC[8]:
                        Xc9 = 1
                    elif cus is facD[8]:
                        Xd9 = 1
                    elif cus is facE[8]:
                        Xe9 = 1

        elif op1cost010 - 0.0001 < op_cost[2] < op1cost010 + 0.0001:
            for cus in cus010:
                if max(cus010) - 0.0001 < cus < max(cus010) + 0.0001:
                    if cus is facA[9]:
                        Xa10 = 1
                    elif cus is facB[9]:
                        Xb10 = 1
                    elif cus is facC[9]:
                        Xc10 = 1
                    elif cus is facD[9]:
                        Xd10 = 1
                    elif cus is facE[9]:
                        Xe10 = 1
        ##################################################################################################

        if op1cost001 - 0.0001 < op_cost[3] < op1cost001 + 0.0001:
            for cus in cus001:
                if max(cus001) - 0.0001 < cus < max(cus001) + 0.0001:
                    if cus is facA[0]:
                        Xa1 = 1
                    elif cus is facB[0]:
                        Xb1 = 1
                    elif cus is facC[0]:
                        Xc1 = 1
                    elif cus is facD[0]:
                        Xd1 = 1
                    elif cus is facE[0]:
                        Xe1 = 1

        elif op1cost002 - 0.0001 < op_cost[3] < op1cost002 + 0.0001:
            for cus in cus002:
                if max(cus002) - 0.0001 < cus < max(cus002) + 0.0001:
                    if cus is facA[1]:
                        Xa2 = 1
                    elif cus is facB[1]:
                        Xb2 = 1
                    elif cus is facC[1]:
                        Xc2 = 1
                    elif cus is facD[1]:
                        Xd2 = 1
                    elif cus is facE[1]:
                        Xe2 = 1

        elif op1cost003 - 0.0001 < op_cost[3] < op1cost003 + 0.0001:
            for cus in cus003:
                if max(cus003) - 0.0001 < cus < max(cus003) + 0.0001:
                    if cus is facA[2]:
                        Xa3 = 1
                    elif cus is facB[2]:
                        Xb3 = 1
                    elif cus is facC[2]:
                        Xc3 = 1
                    elif cus is facD[2]:
                        Xd3 = 1
                    elif cus is facE[2]:
                        Xe3 = 1

        elif op1cost004 - 0.0001 < op_cost[3] < op1cost004 + 0.0001:
            for cus in cus004:
                if max(cus004) - 0.0001 < cus < max(cus004) + 0.0001:
                    if cus is facA[3]:
                        Xa4 = 1
                    elif cus is facB[3]:
                        Xb4 = 1
                    elif cus is facC[3]:
                        Xc4 = 1
                    elif cus is facD[3]:
                        Xd4 = 1
                    elif cus is facE[3]:
                        Xe4 = 1

        elif op1cost005 - 0.0001 < op_cost[3] < op1cost005 + 0.0001:
            for cus in cus005:
                if max(cus005) - 0.0001 < cus < max(cus005) + 0.0001:
                    if cus is facA[4]:
                        Xa5 = 1
                    elif cus is facB[4]:
                        Xb5 = 1
                    elif cus is facC[4]:
                        Xc5 = 1
                    elif cus is facD[4]:
                        Xd5 = 1
                    elif cus is facE[4]:
                        Xe5 = 1

        elif op1cost006 - 0.0001 < op_cost[3] < op1cost006 + 0.0001:
            for cus in cus006:
                if max(cus006) - 0.0001 < cus < max(cus006) + 0.0001:
                    if cus is facA[5]:
                        Xa6 = 1
                    elif cus is facB[5]:
                        Xb6 = 1
                    elif cus is facC[5]:
                        Xc6 = 1
                    elif cus is facD[5]:
                        Xd6 = 1
                    elif cus is facE[5]:
                        Xe6 = 1

        elif op1cost007 - 0.0001 < op_cost[3] < op1cost007 + 0.0001:
            for cus in cus007:
                if max(cus007) - 0.0001 < cus < max(cus007) + 0.0001:
                    if cus is facA[6]:
                        Xa7 = 1
                    elif cus is facB[6]:
                        Xb7 = 1
                    elif cus is facC[6]:
                        Xc7 = 1
                    elif cus is facD[6]:
                        Xd7 = 1
                    elif cus is facE[6]:
                        Xe7 = 1

        elif op1cost008 - 0.0001 < op_cost[3] < op1cost008 + 0.0001:
            for cus in cus008:
                if max(cus008) - 0.0001 < cus < max(cus008) + 0.0001:
                    if cus is facA[7]:
                        Xa8 = 1
                    elif cus is facB[7]:
                        Xb8 = 1
                    elif cus is facC[7]:
                        Xc8 = 1
                    elif cus is facD[7]:
                        Xd8 = 1
                    elif cus is facE[7]:
                        Xe8 = 1

        elif op1cost009 - 0.0001 < op_cost[3] < op1cost009 + 0.0001:
            for cus in cus009:
                if max(cus009) - 0.0001 < cus < max(cus009) + 0.0001:
                    if cus is facA[8]:
                        Xa9 = 1
                    elif cus is facB[8]:
                        Xb9 = 1
                    elif cus is facC[8]:
                        Xc9 = 1
                    elif cus is facD[8]:
                        Xd9 = 1
                    elif cus is facE[8]:
                        Xe9 = 1

        elif op1cost010 - 0.0001 < op_cost[3] < op1cost010 + 0.0001:
            for cus in cus010:
                if max(cus010) - 0.0001 < cus < max(cus010) + 0.0001:
                    if cus is facA[9]:
                        Xa10 = 1
                    elif cus is facB[9]:
                        Xb10 = 1
                    elif cus is facC[9]:
                        Xc10 = 1
                    elif cus is facD[9]:
                        Xd10 = 1
                    elif cus is facE[9]:
                        Xe10 = 1

        ##################################################################################################

        if op1cost001 - 0.0001 < op_cost[4] < op1cost001 + 0.0001:
            for cus in cus001:
                if max(cus001) - 0.0001 < cus < max(cus001) + 0.0001:
                    if cus is facA[0]:
                        Xa1 = 1
                    elif cus is facB[0]:
                        Xb1 = 1
                    elif cus is facC[0]:
                        Xc1 = 1
                    elif cus is facD[0]:
                        Xd1 = 1
                    elif cus is facE[0]:
                        Xe1 = 1

        elif op1cost002 - 0.0001 < op_cost[4] < op1cost002 + 0.0001:
            for cus in cus002:
                if max(cus002) - 0.0001 < cus < max(cus002) + 0.0001:
                    if cus is facA[1]:
                        Xa2 = 1
                    elif cus is facB[1]:
                        Xb2 = 1
                    elif cus is facC[1]:
                        Xc2 = 1
                    elif cus is facD[1]:
                        Xd2 = 1
                    elif cus is facE[1]:
                        Xe2 = 1

        elif op1cost003 - 0.0001 < op_cost[4] < op1cost003 + 0.0001:
            for cus in cus003:
                if max(cus003) - 0.0001 < cus < max(cus003) + 0.0001:
                    if cus is facA[2]:
                        Xa3 = 1
                    elif cus is facB[2]:
                        Xb3 = 1
                    elif cus is facC[2]:
                        Xc3 = 1
                    elif cus is facD[2]:
                        Xd3 = 1
                    elif cus is facE[2]:
                        Xe3 = 1

        elif op1cost004 - 0.0001 < op_cost[4] < op1cost004 + 0.0001:
            for cus in cus004:
                if max(cus004) - 0.0001 < cus < max(cus004) + 0.0001:
                    if cus is facA[3]:
                        Xa4 = 1
                    elif cus is facB[3]:
                        Xb4 = 1
                    elif cus is facC[3]:
                        Xc4 = 1
                    elif cus is facD[3]:
                        Xd4 = 1
                    elif cus is facE[3]:
                        Xe4 = 1

        elif op1cost005 - 0.0001 < op_cost[4] < op1cost005 + 0.0001:
            for cus in cus005:
                if max(cus005) - 0.0001 < cus < max(cus005) + 0.0001:
                    if cus is facA[4]:
                        Xa5 = 1
                    elif cus is facB[4]:
                        Xb5 = 1
                    elif cus is facC[4]:
                        Xc5 = 1
                    elif cus is facD[4]:
                        Xd5 = 1
                    elif cus is facE[4]:
                        Xe5 = 1

        elif op1cost006 - 0.0001 < op_cost[4] < op1cost006 + 0.0001:
            for cus in cus006:
                if max(cus006) - 0.0001 < cus < max(cus006) + 0.0001:
                    if cus is facA[5]:
                        Xa6 = 1
                    elif cus is facB[5]:
                        Xb6 = 1
                    elif cus is facC[5]:
                        Xc6 = 1
                    elif cus is facD[5]:
                        Xd6 = 1
                    elif cus is facE[5]:
                        Xe6 = 1

        elif op1cost007 - 0.0001 < op_cost[4] < op1cost007 + 0.0001:
            for cus in cus007:
                if max(cus007) - 0.0001 < cus < max(cus007) + 0.0001:
                    if cus is facA[6]:
                        Xa7 = 1
                    elif cus is facB[6]:
                        Xb7 = 1
                    elif cus is facC[6]:
                        Xc7 = 1
                    elif cus is facD[6]:
                        Xd7 = 1
                    elif cus is facE[6]:
                        Xe7 = 1

        elif op1cost008 - 0.0001 < op_cost[4] < op1cost008 + 0.0001:
            for cus in cus008:
                if max(cus008) - 0.0001 < cus < max(cus008) + 0.0001:
                    if cus is facA[7]:
                        Xa8 = 1
                    elif cus is facB[7]:
                        Xb8 = 1
                    elif cus is facC[7]:
                        Xc8 = 1
                    elif cus is facD[7]:
                        Xd8 = 1
                    elif cus is facE[7]:
                        Xe8 = 1

        elif op1cost009 - 0.0001 < op_cost[4] < op1cost009 + 0.0001:
            for cus in cus009:
                if max(cus009) - 0.0001 < cus < max(cus009) + 0.0001:
                    if cus is facA[8]:
                        Xa9 = 1
                    elif cus is facB[8]:
                        Xb9 = 1
                    elif cus is facC[8]:
                        Xc9 = 1
                    elif cus is facD[8]:
                        Xd9 = 1
                    elif cus is facE[8]:
                        Xe9 = 1

        elif op1cost010 - 0.0001 < op_cost[4] < op1cost010 + 0.0001:
            for cus in cus010:
                if max(cus010) - 0.0001 < cus < max(cus010) + 0.0001:
                    if cus is facA[9]:
                        Xa10 = 1
                    elif cus is facB[9]:
                        Xb10 = 1
                    elif cus is facC[9]:
                        Xc10 = 1
                    elif cus is facD[9]:
                        Xd10 = 1
                    elif cus is facE[9]:
                        Xe10 = 1

        ##################################################################################################

        if op1cost001 - 0.0001 < op_cost[5] < op1cost001 + 0.0001:
            for cus in cus001:
                if max(cus001) - 0.0001 < cus < max(cus001) + 0.0001:
                    if cus is facA[0]:
                        Xa1 = 1
                    elif cus is facB[0]:
                        Xb1 = 1
                    elif cus is facC[0]:
                        Xc1 = 1
                    elif cus is facD[0]:
                        Xd1 = 1
                    elif cus is facE[0]:
                        Xe1 = 1

        elif op1cost002 - 0.0001 < op_cost[5] < op1cost002 + 0.0001:
            for cus in cus002:
                if max(cus002) - 0.0001 < cus < max(cus002) + 0.0001:
                    if cus is facA[1]:
                        Xa2 = 1
                    elif cus is facB[1]:
                        Xb2 = 1
                    elif cus is facC[1]:
                        Xc2 = 1
                    elif cus is facD[1]:
                        Xd2 = 1
                    elif cus is facE[1]:
                        Xe2 = 1

        elif op1cost003 - 0.0001 < op_cost[5] < op1cost003 + 0.0001:
            for cus in cus003:
                if max(cus003) - 0.0001 < cus < max(cus003) + 0.0001:
                    if cus is facA[2]:
                        Xa3 = 1
                    elif cus is facB[2]:
                        Xb3 = 1
                    elif cus is facC[2]:
                        Xc3 = 1
                    elif cus is facD[2]:
                        Xd3 = 1
                    elif cus is facE[2]:
                        Xe3 = 1

        elif op1cost004 - 0.0001 < op_cost[5] < op1cost004 + 0.0001:
            for cus in cus004:
                if max(cus004) - 0.0001 < cus < max(cus004) + 0.0001:
                    if cus is facA[3]:
                        Xa4 = 1
                    elif cus is facB[3]:
                        Xb4 = 1
                    elif cus is facC[3]:
                        Xc4 = 1
                    elif cus is facD[3]:
                        Xd4 = 1
                    elif cus is facE[3]:
                        Xe4 = 1

        elif op1cost005 - 0.0001 < op_cost[5] < op1cost005 + 0.0001:
            for cus in cus005:
                if max(cus005) - 0.0001 < cus < max(cus005) + 0.0001:
                    if cus is facA[4]:
                        Xa5 = 1
                    elif cus is facB[4]:
                        Xb5 = 1
                    elif cus is facC[4]:
                        Xc5 = 1
                    elif cus is facD[4]:
                        Xd5 = 1
                    elif cus is facE[4]:
                        Xe5 = 1

        elif op1cost006 - 0.0001 < op_cost[5] < op1cost006 + 0.0001:
            for cus in cus006:
                if max(cus006) - 0.0001 < cus < max(cus006) + 0.0001:
                    if cus is facA[5]:
                        Xa6 = 1
                    elif cus is facB[5]:
                        Xb6 = 1
                    elif cus is facC[5]:
                        Xc6 = 1
                    elif cus is facD[5]:
                        Xd6 = 1
                    elif cus is facE[5]:
                        Xe6 = 1

        elif op1cost007 - 0.0001 < op_cost[5] < op1cost007 + 0.0001:
            for cus in cus007:
                if max(cus007) - 0.0001 < cus < max(cus007) + 0.0001:
                    if cus is facA[6]:
                        Xa7 = 1
                    elif cus is facB[6]:
                        Xb7 = 1
                    elif cus is facC[6]:
                        Xc7 = 1
                    elif cus is facD[6]:
                        Xd7 = 1
                    elif cus is facE[6]:
                        Xe7 = 1

        elif op1cost008 - 0.0001 < op_cost[5] < op1cost008 + 0.0001:
            for cus in cus008:
                if max(cus008) - 0.0001 < cus < max(cus008) + 0.0001:
                    if cus is facA[7]:
                        Xa8 = 1
                    elif cus is facB[7]:
                        Xb8 = 1
                    elif cus is facC[7]:
                        Xc8 = 1
                    elif cus is facD[7]:
                        Xd8 = 1
                    elif cus is facE[7]:
                        Xe8 = 1

        elif op1cost009 - 0.0001 < op_cost[5] < op1cost009 + 0.0001:
            for cus in cus009:
                if max(cus009) - 0.0001 < cus < max(cus009) + 0.0001:
                    if cus is facA[8]:
                        Xa9 = 1
                    elif cus is facB[8]:
                        Xb9 = 1
                    elif cus is facC[8]:
                        Xc9 = 1
                    elif cus is facD[8]:
                        Xd9 = 1
                    elif cus is facE[8]:
                        Xe9 = 1

        elif op1cost010 - 0.0001 < op_cost[5] < op1cost010 + 0.0001:
            for cus in cus010:
                if max(cus010) - 0.0001 < cus < max(cus010) + 0.0001:
                    if cus is facA[9]:
                        Xa10 = 1
                    elif cus is facB[9]:
                        Xb10 = 1
                    elif cus is facC[9]:
                        Xc10 = 1
                    elif cus is facD[9]:
                        Xd10 = 1
                    elif cus is facE[9]:
                        Xe10 = 1

        ##################################################################################################

        if op1cost001 - 0.0001 < op_cost[6] < op1cost001 + 0.0001:
            for cus in cus001:
                if max(cus001) - 0.0001 < cus < max(cus001) + 0.0001:
                    if cus is facA[0]:
                        Xa1 = 1
                    elif cus is facB[0]:
                        Xb1 = 1
                    elif cus is facC[0]:
                        Xc1 = 1
                    elif cus is facD[0]:
                        Xd1 = 1
                    elif cus is facE[0]:
                        Xe1 = 1

        elif op1cost002 - 0.0001 < op_cost[6] < op1cost002 + 0.0001:
            for cus in cus002:
                if max(cus002) - 0.0001 < cus < max(cus002) + 0.0001:
                    if cus is facA[1]:
                        Xa2 = 1
                    elif cus is facB[1]:
                        Xb2 = 1
                    elif cus is facC[1]:
                        Xc2 = 1
                    elif cus is facD[1]:
                        Xd2 = 1
                    elif cus is facE[1]:
                        Xe2 = 1

        elif op1cost003 - 0.0001 < op_cost[6] < op1cost003 + 0.0001:
            for cus in cus003:
                if max(cus003) - 0.0001 < cus < max(cus003) + 0.0001:
                    if cus is facA[2]:
                        Xa3 = 1
                    elif cus is facB[2]:
                        Xb3 = 1
                    elif cus is facC[2]:
                        Xc3 = 1
                    elif cus is facD[2]:
                        Xd3 = 1
                    elif cus is facE[2]:
                        Xe3 = 1

        elif op1cost004 - 0.0001 < op_cost[6] < op1cost004 + 0.0001:
            for cus in cus004:
                if max(cus004) - 0.0001 < cus < max(cus004) + 0.0001:
                    if cus is facA[3]:
                        Xa4 = 1
                    elif cus is facB[3]:
                        Xb4 = 1
                    elif cus is facC[3]:
                        Xc4 = 1
                    elif cus is facD[3]:
                        Xd4 = 1
                    elif cus is facE[3]:
                        Xe4 = 1

        elif op1cost005 - 0.0001 < op_cost[6] < op1cost005 + 0.0001:
            for cus in cus005:
                if max(cus005) - 0.0001 < cus < max(cus005) + 0.0001:
                    if cus is facA[4]:
                        Xa5 = 1
                    elif cus is facB[4]:
                        Xb5 = 1
                    elif cus is facC[4]:
                        Xc5 = 1
                    elif cus is facD[4]:
                        Xd5 = 1
                    elif cus is facE[4]:
                        Xe5 = 1

        elif op1cost006 - 0.0001 < op_cost[6] < op1cost006 + 0.0001:
            for cus in cus006:
                if max(cus006) - 0.0001 < cus < max(cus006) + 0.0001:
                    if cus is facA[5]:
                        Xa6 = 1
                    elif cus is facB[5]:
                        Xb6 = 1
                    elif cus is facC[5]:
                        Xc6 = 1
                    elif cus is facD[5]:
                        Xd6 = 1
                    elif cus is facE[5]:
                        Xe6 = 1

        elif op1cost007 - 0.0001 < op_cost[6] < op1cost007 + 0.0001:
            for cus in cus007:
                if max(cus007) - 0.0001 < cus < max(cus007) + 0.0001:
                    if cus is facA[6]:
                        Xa7 = 1
                    elif cus is facB[6]:
                        Xb7 = 1
                    elif cus is facC[6]:
                        Xc7 = 1
                    elif cus is facD[6]:
                        Xd7 = 1
                    elif cus is facE[6]:
                        Xe7 = 1

        elif op1cost008 - 0.0001 < op_cost[6] < op1cost008 + 0.0001:
            for cus in cus008:
                if max(cus008) - 0.0001 < cus < max(cus008) + 0.0001:
                    if cus is facA[7]:
                        Xa8 = 1
                    elif cus is facB[7]:
                        Xb8 = 1
                    elif cus is facC[7]:
                        Xc8 = 1
                    elif cus is facD[7]:
                        Xd8 = 1
                    elif cus is facE[7]:
                        Xe8 = 1

        elif op1cost009 - 0.0001 < op_cost[6] < op1cost009 + 0.0001:
            for cus in cus009:
                if max(cus009) - 0.0001 < cus < max(cus009) + 0.0001:
                    if cus is facA[8]:
                        Xa9 = 1
                    elif cus is facB[8]:
                        Xb9 = 1
                    elif cus is facC[8]:
                        Xc9 = 1
                    elif cus is facD[8]:
                        Xd9 = 1
                    elif cus is facE[8]:
                        Xe9 = 1

        elif op1cost010 - 0.0001 < op_cost[6] < op1cost010 + 0.0001:
            for cus in cus010:
                if max(cus010) - 0.0001 < cus < max(cus010) + 0.0001:
                    if cus is facA[9]:
                        Xa10 = 1
                    elif cus is facB[9]:
                        Xb10 = 1
                    elif cus is facC[9]:
                        Xc10 = 1
                    elif cus is facD[9]:
                        Xd10 = 1
                    elif cus is facE[9]:
                        Xe10 = 1

        ##################################################################################################

        if op1cost001 - 0.0001 < op_cost[7] < op1cost001 + 0.0001:
            for cus in cus001:
                if max(cus001) - 0.0001 < cus < max(cus001) + 0.0001:
                    if cus is facA[0]:
                        Xa1 = 1
                    elif cus is facB[0]:
                        Xb1 = 1
                    elif cus is facC[0]:
                        Xc1 = 1
                    elif cus is facD[0]:
                        Xd1 = 1
                    elif cus is facE[0]:
                        Xe1 = 1

        elif op1cost002 - 0.0001 < op_cost[7] < op1cost002 + 0.0001:
            for cus in cus002:
                if max(cus002) - 0.0001 < cus < max(cus002) + 0.0001:
                    if cus is facA[1]:
                        Xa2 = 1
                    elif cus is facB[1]:
                        Xb2 = 1
                    elif cus is facC[1]:
                        Xc2 = 1
                    elif cus is facD[1]:
                        Xd2 = 1
                    elif cus is facE[1]:
                        Xe2 = 1

        elif op1cost003 - 0.0001 < op_cost[7] < op1cost003 + 0.0001:
            for cus in cus003:
                if max(cus003) - 0.0001 < cus < max(cus003) + 0.0001:
                    if cus is facA[2]:
                        Xa3 = 1
                    elif cus is facB[2]:
                        Xb3 = 1
                    elif cus is facC[2]:
                        Xc3 = 1
                    elif cus is facD[2]:
                        Xd3 = 1
                    elif cus is facE[2]:
                        Xe3 = 1

        elif op1cost004 - 0.0001 < op_cost[7] < op1cost004 + 0.0001:
            for cus in cus004:
                if max(cus004) - 0.0001 < cus < max(cus004) + 0.0001:
                    if cus is facA[3]:
                        Xa4 = 1
                    elif cus is facB[3]:
                        Xb4 = 1
                    elif cus is facC[3]:
                        Xc4 = 1
                    elif cus is facD[3]:
                        Xd4 = 1
                    elif cus is facE[3]:
                        Xe4 = 1

        elif op1cost005 - 0.0001 < op_cost[7] < op1cost005 + 0.0001:
            for cus in cus005:
                if max(cus005) - 0.0001 < cus < max(cus005) + 0.0001:
                    if cus is facA[4]:
                        Xa5 = 1
                    elif cus is facB[4]:
                        Xb5 = 1
                    elif cus is facC[4]:
                        Xc5 = 1
                    elif cus is facD[4]:
                        Xd5 = 1
                    elif cus is facE[4]:
                        Xe5 = 1

        elif op1cost006 - 0.0001 < op_cost[7] < op1cost006 + 0.0001:
            for cus in cus006:
                if max(cus006) - 0.0001 < cus < max(cus006) + 0.0001:
                    if cus is facA[5]:
                        Xa6 = 1
                    elif cus is facB[5]:
                        Xb6 = 1
                    elif cus is facC[5]:
                        Xc6 = 1
                    elif cus is facD[5]:
                        Xd6 = 1
                    elif cus is facE[5]:
                        Xe6 = 1

        elif op1cost007 - 0.0001 < op_cost[7] < op1cost007 + 0.0001:
            for cus in cus007:
                if max(cus007) - 0.0001 < cus < max(cus007) + 0.0001:
                    if cus is facA[6]:
                        Xa7 = 1
                    elif cus is facB[6]:
                        Xb7 = 1
                    elif cus is facC[6]:
                        Xc7 = 1
                    elif cus is facD[6]:
                        Xd7 = 1
                    elif cus is facE[6]:
                        Xe7 = 1

        elif op1cost008 - 0.0001 < op_cost[7] < op1cost008 + 0.0001:
            for cus in cus008:
                if max(cus008) - 0.0001 < cus < max(cus008) + 0.0001:
                    if cus is facA[7]:
                        Xa8 = 1
                    elif cus is facB[7]:
                        Xb8 = 1
                    elif cus is facC[7]:
                        Xc8 = 1
                    elif cus is facD[7]:
                        Xd8 = 1
                    elif cus is facE[7]:
                        Xe8 = 1

        elif op1cost009 - 0.0001 < op_cost[7] < op1cost009 + 0.0001:
            for cus in cus009:
                if max(cus009) - 0.0001 < cus < max(cus009) + 0.0001:
                    if cus is facA[8]:
                        Xa9 = 1
                    elif cus is facB[8]:
                        Xb9 = 1
                    elif cus is facC[8]:
                        Xc9 = 1
                    elif cus is facD[8]:
                        Xd9 = 1
                    elif cus is facE[8]:
                        Xe9 = 1

        elif op1cost010 - 0.0001 < op_cost[7] < op1cost010 + 0.0001:
            for cus in cus010:
                if max(cus010) - 0.0001 < cus < max(cus010) + 0.0001:
                    if cus is facA[9]:
                        Xa10 = 1
                    elif cus is facB[9]:
                        Xb10 = 1
                    elif cus is facC[9]:
                        Xc10 = 1
                    elif cus is facD[9]:
                        Xd10 = 1
                    elif cus is facE[9]:
                        Xe10 = 1

        ##################################################################################################

        if op1cost001 - 0.0001 < op_cost[8] < op1cost001 + 0.0001:
            for cus in cus001:
                if max(cus001) - 0.0001 < cus < max(cus001) + 0.0001:
                    if cus is facA[0]:
                        Xa1 = 1
                    elif cus is facB[0]:
                        Xb1 = 1
                    elif cus is facC[0]:
                        Xc1 = 1
                    elif cus is facD[0]:
                        Xd1 = 1
                    elif cus is facE[0]:
                        Xe1 = 1

        elif op1cost002 - 0.0001 < op_cost[8] < op1cost002 + 0.0001:
            for cus in cus002:
                if max(cus002) - 0.0001 < cus < max(cus002) + 0.0001:
                    if cus is facA[1]:
                        Xa2 = 1
                    elif cus is facB[1]:
                        Xb2 = 1
                    elif cus is facC[1]:
                        Xc2 = 1
                    elif cus is facD[1]:
                        Xd2 = 1
                    elif cus is facE[1]:
                        Xe2 = 1

        elif op1cost003 - 0.0001 < op_cost[8] < op1cost003 + 0.0001:
            for cus in cus003:
                if max(cus003) - 0.0001 < cus < max(cus003) + 0.0001:
                    if cus is facA[2]:
                        Xa3 = 1
                    elif cus is facB[2]:
                        Xb3 = 1
                    elif cus is facC[2]:
                        Xc3 = 1
                    elif cus is facD[2]:
                        Xd3 = 1
                    elif cus is facE[2]:
                        Xe3 = 1

        elif op1cost004 - 0.0001 < op_cost[8] < op1cost004 + 0.0001:
            for cus in cus004:
                if max(cus004) - 0.0001 < cus < max(cus004) + 0.0001:
                    if cus is facA[3]:
                        Xa4 = 1
                    elif cus is facB[3]:
                        Xb4 = 1
                    elif cus is facC[3]:
                        Xc4 = 1
                    elif cus is facD[3]:
                        Xd4 = 1
                    elif cus is facE[3]:
                        Xe4 = 1

        elif op1cost005 - 0.0001 < op_cost[8] < op1cost005 + 0.0001:
            for cus in cus005:
                if max(cus005) - 0.0001 < cus < max(cus005) + 0.0001:
                    if cus is facA[4]:
                        Xa5 = 1
                    elif cus is facB[4]:
                        Xb5 = 1
                    elif cus is facC[4]:
                        Xc5 = 1
                    elif cus is facD[4]:
                        Xd5 = 1
                    elif cus is facE[4]:
                        Xe5 = 1

        elif op1cost006 - 0.0001 < op_cost[8] < op1cost006 + 0.0001:
            for cus in cus006:
                if max(cus006) - 0.0001 < cus < max(cus006) + 0.0001:
                    if cus is facA[5]:
                        Xa6 = 1
                    elif cus is facB[5]:
                        Xb6 = 1
                    elif cus is facC[5]:
                        Xc6 = 1
                    elif cus is facD[5]:
                        Xd6 = 1
                    elif cus is facE[5]:
                        Xe6 = 1

        elif op1cost007 - 0.0001 < op_cost[8] < op1cost007 + 0.0001:
            for cus in cus007:
                if max(cus007) - 0.0001 < cus < max(cus007) + 0.0001:
                    if cus is facA[6]:
                        Xa7 = 1
                    elif cus is facB[6]:
                        Xb7 = 1
                    elif cus is facC[6]:
                        Xc7 = 1
                    elif cus is facD[6]:
                        Xd7 = 1
                    elif cus is facE[6]:
                        Xe7 = 1

        elif op1cost008 - 0.0001 < op_cost[8] < op1cost008 + 0.0001:
            for cus in cus008:
                if max(cus008) - 0.0001 < cus < max(cus008) + 0.0001:
                    if cus is facA[7]:
                        Xa8 = 1
                    elif cus is facB[7]:
                        Xb8 = 1
                    elif cus is facC[7]:
                        Xc8 = 1
                    elif cus is facD[7]:
                        Xd8 = 1
                    elif cus is facE[7]:
                        Xe8 = 1

        elif op1cost009 - 0.0001 < op_cost[8] < op1cost009 + 0.0001:
            for cus in cus009:
                if max(cus009) - 0.0001 < cus < max(cus009) + 0.0001:
                    if cus is facA[8]:
                        Xa9 = 1
                    elif cus is facB[8]:
                        Xb9 = 1
                    elif cus is facC[8]:
                        Xc9 = 1
                    elif cus is facD[8]:
                        Xd9 = 1
                    elif cus is facE[8]:
                        Xe9 = 1

        elif op1cost010 - 0.0001 < op_cost[8] < op1cost010 + 0.0001:
            for cus in cus010:
                if max(cus010) - 0.0001 < cus < max(cus010) + 0.0001:
                    if cus is facA[9]:
                        Xa10 = 1
                    elif cus is facB[9]:
                        Xb10 = 1
                    elif cus is facC[9]:
                        Xc10 = 1
                    elif cus is facD[9]:
                        Xd10 = 1
                    elif cus is facE[9]:
                        Xe10 = 1

        ##################################################################################################

        if op1cost001 - 0.0001 < op_cost[9] < op1cost001 + 0.0001:
            for cus in cus001:
                if max(cus001) - 0.0001 < cus < max(cus001) + 0.0001:
                    if cus is facA[0]:
                        Xa1 = 1
                    elif cus is facB[0]:
                        Xb1 = 1
                    elif cus is facC[0]:
                        Xc1 = 1
                    elif cus is facD[0]:
                        Xd1 = 1
                    elif cus is facE[0]:
                        Xe1 = 1

        elif op1cost002 - 0.0001 < op_cost[9] < op1cost002 + 0.0001:
            for cus in cus002:
                if max(cus002) - 0.0001 < cus < max(cus002) + 0.0001:
                    if cus is facA[1]:
                        Xa2 = 1
                    elif cus is facB[1]:
                        Xb2 = 1
                    elif cus is facC[1]:
                        Xc2 = 1
                    elif cus is facD[1]:
                        Xd2 = 1
                    elif cus is facE[1]:
                        Xe2 = 1

        elif op1cost003 - 0.0001 < op_cost[9] < op1cost003 + 0.0001:
            for cus in cus003:
                if max(cus003) - 0.0001 < cus < max(cus003) + 0.0001:
                    if cus is facA[2]:
                        Xa3 = 1
                    elif cus is facB[2]:
                        Xb3 = 1
                    elif cus is facC[2]:
                        Xc3 = 1
                    elif cus is facD[2]:
                        Xd3 = 1
                    elif cus is facE[2]:
                        Xe3 = 1

        elif op1cost004 - 0.0001 < op_cost[9] < op1cost004 + 0.0001:
            for cus in cus004:
                if max(cus004) - 0.0001 < cus < max(cus004) + 0.0001:
                    if cus is facA[3]:
                        Xa4 = 1
                    elif cus is facB[3]:
                        Xb4 = 1
                    elif cus is facC[3]:
                        Xc4 = 1
                    elif cus is facD[3]:
                        Xd4 = 1
                    elif cus is facE[3]:
                        Xe4 = 1

        elif op1cost005 - 0.0001 < op_cost[9] < op1cost005 + 0.0001:
            for cus in cus005:
                if max(cus005) - 0.0001 < cus < max(cus005) + 0.0001:
                    if cus is facA[4]:
                        Xa5 = 1
                    elif cus is facB[4]:
                        Xb5 = 1
                    elif cus is facC[4]:
                        Xc5 = 1
                    elif cus is facD[4]:
                        Xd5 = 1
                    elif cus is facE[4]:
                        Xe5 = 1

        elif op1cost006 - 0.0001 < op_cost[9] < op1cost006 + 0.0001:
            for cus in cus006:
                if max(cus006) - 0.0001 < cus < max(cus006) + 0.0001:
                    if cus is facA[5]:
                        Xa6 = 1
                    elif cus is facB[5]:
                        Xb6 = 1
                    elif cus is facC[5]:
                        Xc6 = 1
                    elif cus is facD[5]:
                        Xd6 = 1
                    elif cus is facE[5]:
                        Xe6 = 1

        elif op1cost007 - 0.0001 < op_cost[9] < op1cost007 + 0.0001:
            for cus in cus007:
                if max(cus007) - 0.0001 < cus < max(cus007) + 0.0001:
                    if cus is facA[6]:
                        Xa7 = 1
                    elif cus is facB[6]:
                        Xb7 = 1
                    elif cus is facC[6]:
                        Xc7 = 1
                    elif cus is facD[6]:
                        Xd7 = 1
                    elif cus is facE[6]:
                        Xe7 = 1

        elif op1cost008 - 0.0001 < op_cost[9] < op1cost008 + 0.0001:
            for cus in cus008:
                if max(cus008) - 0.0001 < cus < max(cus008) + 0.0001:
                    if cus is facA[7]:
                        Xa8 = 1
                    elif cus is facB[7]:
                        Xb8 = 1
                    elif cus is facC[7]:
                        Xc8 = 1
                    elif cus is facD[7]:
                        Xd8 = 1
                    elif cus is facE[7]:
                        Xe8 = 1

        elif op1cost009 - 0.0001 < op_cost[9] < op1cost009 + 0.0001:
            for cus in cus009:
                if max(cus009) - 0.0001 < cus < max(cus009) + 0.0001:
                    if cus is facA[8]:
                        Xa9 = 1
                    elif cus is facB[8]:
                        Xb9 = 1
                    elif cus is facC[8]:
                        Xc9 = 1
                    elif cus is facD[8]:
                        Xd9 = 1
                    elif cus is facE[8]:
                        Xe9 = 1

        elif op1cost010 - 0.0001 < op_cost[9] < op1cost010 + 0.0001:
            for cus in cus010:
                if max(cus010) - 0.0001 < cus < max(cus010) + 0.0001:
                    if cus is facA[9]:
                        Xa10 = 1
                    elif cus is facB[9]:
                        Xb10 = 1
                    elif cus is facC[9]:
                        Xc10 = 1
                    elif cus is facD[9]:
                        Xd10 = 1
                    elif cus is facE[9]:
                        Xe10 = 1


####################################################################################################

Xset1 = [Xa1, Xb1, Xc1, Xd1, Xe1]
Xset2 = [Xa2, Xb2, Xc2, Xd2, Xe2]
Xset3 = [Xa3, Xb3, Xc3, Xd3, Xe3]
Xset4 = [Xa4, Xb4, Xc4, Xd4, Xe4]
Xset5 = [Xa5, Xb5, Xc5, Xd5, Xe5]
Xset6 = [Xa6, Xb6, Xc6, Xd6, Xe6]
Xset7 = [Xa7, Xb7, Xc7, Xd7, Xe7]
Xset8 = [Xa8, Xb8, Xc8, Xd8, Xe8]
Xset9 = [Xa9, Xb9, Xc9, Xd9, Xe9]
Xset10 = [Xa10, Xb10, Xc10, Xd10, Xe10]

#print Xa1, Xb1, Xc1, Xd1, Xe1
#print facA, facB, facC, facD, facE




base_set = np.array ([[a1, a2, a3, a4, a5, a6, a7, a8, a9, a10],
                      [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10],
                      [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10],
                      [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10],
                      [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]])


print base_set
print \

Profit_facA = np.array([a1 * Xa1, a2 * Xa2, a3 * Xa3, a4 * Xa4, a5 * Xa5, a6 * Xa6, a7 * Xa7, a8 * Xa8, a9 * Xa9, a10 * Xa10])
Profit_facB = np.array([b1 * Xb1, b2 * Xb2, b3 * Xb3, b4 * Xb4, b5 * Xb5, b6 * Xb6, b7 * Xb7, b8 * Xb8, b9 * Xb9, b10 * Xb10])
Profit_facC = np.array([c1 * Xc1, c2 * Xc2, c3 * Xc3, c4 * Xc4, c5 * Xc5, c6 * Xc6, c7 * Xc7, c8 * Xc8, c9 * Xc9, c10 * Xc10])
Profit_facD = np.array([d1 * Xd1, d2 * Xd2, d3 * Xd3, d4 * Xd4, d5 * Xd5, d6 * Xd6, d7 * Xd7, d8 * Xd8, d9 * Xd9, d10 * Xd10])
Profit_facE = np.array([e1 * Xe1, e2 * Xe2, e3 * Xe3, e4 * Xe4, e5 * Xe5, e6 * Xe6, e7 * Xe7, e8 * Xe8, e9 * Xe9, e10 * Xe10])




optimal_set = np.array((Profit_facA, Profit_facB, Profit_facC, Profit_facD, Profit_facE))


print optimal_set
print \

# XfacA = [Xa1, Xa2, Xa3, Xa4, Xa5, Xa6, Xa7, Xa8, Xa9, Xa10]
# XfacB = [Xb1, Xb2, Xb3, Xb4, Xb5, Xb6, Xb7, Xb8, Xb9, Xb10]
# XfacC = [Xc1, Xc2, Xc3, Xc4, Xc5, Xc6, Xc7, Xc8, Xc9, Xc10]
# XfacD = [Xd1, Xd2, Xd3, Xd4, Xd5, Xd6, Xd7, Xd8, Xd9, Xd10]
# XfacE = [Xe1, Xe2, Xe3, Xe4, Xe5, Xe6, Xe7, Xe8, Xe9, Xe10]

WfacA = np.array([W1 * Xa1, W2 * Xa2, W3 * Xa3, W4 * Xa4, W5 * Xa5, W6 * Xa6, W7 * Xa7, W8 * Xa8, W9 * Xa9, W10 * Xa10])
WfacB = np.array([W1 * Xb1, W2 * Xb2, W3 * Xb3, W4 * Xb4, W5 * Xb5, W6 * Xb6, W7 * Xb7, W8 * Xb8, W9 * Xb9, W10 * Xb10])
WfacC = np.array([W1 * Xc1, W2 * Xc2, W3 * Xc3, W4 * Xc4, W5 * Xc5, W6 * Xc6, W7 * Xc7, W8 * Xc8, W9 * Xc9, W10 * Xc10])
WfacD = np.array([W1 * Xd1, W2 * Xd2, W3 * Xd3, W4 * Xd4, W5 * Xd5, W6 * Xd6, W7 * Xd7, W8 * Xd8, W9 * Xd9, W10 * Xd10])
WfacE = np.array([W1 * Xe1, W2 * Xe2, W3 * Xe3, W4 * Xe4, W5 * Xe5, W6 * Xe6, W7 * Xe7, W8 * Xe8, W9 * Xe9, W10 * Xe10])

weight_set = np.array([WfacA, WfacB, WfacC, WfacD, WfacE])

print weight_set
print \

XfacA = [Xa1, Xa2, Xa3, Xa4, Xa5, Xa6, Xa7, Xa8, Xa9, Xa10]
XfacB = [Xb1, Xb2, Xb3, Xb4, Xb5, Xb6, Xb7, Xb8, Xb9, Xb10]
XfacC = [Xc1, Xc2, Xc3, Xc4, Xc5, Xc6, Xc7, Xc8, Xc9, Xc10]
XfacD = [Xd1, Xd2, Xd3, Xd4, Xd5, Xd6, Xd7, Xd8, Xd9, Xd10]
XfacE = [Xe1, Xe2, Xe3, Xe4, Xe5, Xe6, Xe7, Xe8, Xe9, Xe10]


assign_set_hori = np.array((XfacA, XfacB, XfacC, XfacD, XfacE))

print assign_set_hori
print \

#Xset1 = [Xa1, Xb1, Xc1, Xd1, Xe1]
#Xset2 = [Xa2, Xb2, Xc2, Xd2, Xe2]
#Xset3 = [Xa3, Xb3, Xc3, Xd3, Xe3]
#Xset4 = [Xa4, Xb4, Xc4, Xd4, Xe4]
#Xset5 = [Xa5, Xb5, Xc5, Xd5, Xe5]
#Xset6 = [Xa6, Xb6, Xc6, Xd6, Xe6]
#Xset7 = [Xa7, Xb7, Xc7, Xd7, Xe7]
#Xset8 = [Xa8, Xb8, Xc8, Xd8, Xe8]
#Xset9 = [Xa9, Xb9, Xc9, Xd9, Xe9]
#Xset10 = [Xa10, Xb10, Xc10, Xd10, Xe10]


assign_set_vert = np.array([Xset1, Xset2, Xset3, Xset4, Xset5, Xset6, Xset7, Xset8, Xset9, Xset10])



calc_set = np.array ((C001, C002, C003, C004, C005, C006, C007, C008, C009, C010))
op_cost = np.array ([op1cost001, op1cost002, op1cost003, op1cost004, op1cost005, op1cost006, op1cost007, op1cost008, op1cost009, op1cost010])

print op_cost

print sum(WfacA)
print sum(WfacB)
print sum(WfacC)
print sum(WfacD)
print sum(WfacE)
print \


print assign_set_vert

### make new set [xij * pij]
###
#### weight constraint how?
#### set1 = np.array [Xa1, Xb1, Xc1, Xd1, Xe1]
### while sum(set1) <= 1:
### while