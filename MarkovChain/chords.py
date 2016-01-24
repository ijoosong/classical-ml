

major = [4, 3, 5]
major7 = [4, 3, 4]
major65 = [3, 4, 1]
major43 = [4, 1, 4]
major42 = [1, 4, 3]
major6 = [3, 5]
major64 = [5, 4, 3]

minor = [3, 4, 5]
minor7 = [3, 4, 3]
minor65 = [4, 3, 2]
minor43 = [3, 2, 3]
minor42 = [2, 3, 4]
minor6 = [4, 5]

dom = major
dom7 = [4, 3, 3]
dom65 = [3, 3, 2]
dom43 = [3, 2, 4]
dom42 = [2, 4, 3]
dom6 = major6

dim = [3, 3, 6]
dimmaj7 = [3, 3, 5]
dimhalf7 = [3, 3, 4]
dimfull7 = [3, 3, 3]

notes = {
     'a1':1,  'bb1':2,  'b1':3,  'c1':4,  'db1':5,  'd1':6,  'eb1':7,  'e1':8,  'f1':9,  'gb1':10, 'g1':11, 'ab1':12,
     'a2':13, 'bb2':14, 'b2':15, 'c2':16, 'db2':17, 'd2':18, 'eb2':19, 'e2':20, 'f2':21, 'gb2':22, 'g2':23, 'ab2':24,
     'a3':25, 'bb3':26, 'b3':27, 'c3':28, 'db3':29, 'd3':30, 'eb3':31, 'e3':32, 'f3':33, 'gb3':34, 'g3':35, 'ab3':36,
     'a4':37, 'bb4':38, 'b4':39, 'c4':40, 'db4':41, 'd4':42, 'eb4':43, 'e4':44, 'f4':45, 'gb4':46, 'g4':47, 'ab4':48,
     'a5':49, 'bb5':50, 'b5':51, 'c5':52, 'db5':53, 'd5':54, 'eb5':55, 'e5':56, 'f5':57, 'gb5':58, 'g5':59, 'ab5':60,
     'a6':61, 'bb6':62, 'b6':63, 'c6':64, 'db6':65, 'd6':66, 'eb6':67, 'e6':68, 'f6':69, 'gb6':70, 'g6':71, 'ab6':72,
     'a7':73, 'bb7':74, 'b7':75, 'c7':76, 'db7':77, 'd7':78, 'eb7':79, 'e7':80, 'f7':81, 'gb7':82, 'g7':83, 'ab7':84,
     'a8':85, 'bb8':86, 'b8':87, 'c8':88,  'r':0
     }
# 1=whole, 2=half, 4=quarter, 8=eight
beethoven_1 = [['I', 1], ['I', 1], ['V65', 1], ['V65', 1], ['I7', 1], ['I7', 1], ['V43', 1], ['I6', 2], ['iidim7', 2], ['V', 1]]


# add augmented chords, augmented sixths, neopolitan iis
duration = {'2w':512*3, 'w':256*3, 'h':128*3, 'q':64*3, 'e':32*3, 's':16*3, '64':8*3, '128':4*3,
            'dw':(256+128)*3, 'dh':(128+64)*3, 'dq':(64+32)*3, 'de':(32+16)*3, 'd64':(8+4)*3,
            '3w':256, '3h':128, '3q':64, '3e':32, '3s':16, '364':8}

# the code goes as such each [] is a measure, each one within it is a phrase with an end.
# the values are: note from tonal center (i.e. if in the key of F, F is 1, A is 3, C is 5 etc.),
# length(quarter, half, dottedquarter, whole, eigth, etc.), where it is on the piano (c4 is middle c, a5 is the a
# above middle c, a4 is the a below it.
b_sonata_op2no1_in_f = [['q c4 I'], ['1 q f4 I', '3 q a5 I', '5 q c5 I', '1 q f5 I'], ['3 dq a6']]