import math
def ex4(x,y):
    y={'a1':11,'b1':21,'c1':31,'d1':41,'e1':51,'f1':61,'g1':71,'h1':81
    ,'a2':12,'b2':22,'c2':32,'d2':42,'e2':52,'f2':62,'g2':72,'h2':82
    ,'a3':13,'b3':23,'c3':33,'d3':43,'e3':53,'f3':63,'g3':73,'h3':83
    ,'a4':14,'b4':24,'c4':34,'d4':44,'e4':54,'f4':64,'g4':74,'h4':84
    ,'a5':15,'b5':25,'c5':35,'d5':45,'e5':55,'f5':65,'g5':75,'h5':85
    ,'a6':16,'b6':26,'c6':36,'d6':46,'e6':56,'f6':66,'g6':76,'h6':86
    ,'a7':17,'b7':27,'c7':37,'d7':47,'e7':57,'f7':67,'g7':77,'h7':87
    ,'a8':18,'b8':28,'c8':38,'d8':48,'e8':58,'f8':68,'g8':78,'h8':88}
    x={'a1':11,'b1':21,'c1':31,'d1':41,'e1':51,'f1':61,'g1':71,'h1':81
    ,'a2':12,'b2':22,'c2':32,'d2':42,'e2':52,'f2':62,'g2':72,'h2':82
    ,'a3':13,'b3':23,'c3':33,'d3':43,'e3':53,'f3':63,'g3':73,'h3':83
    ,'a4':14,'b4':24,'c4':34,'d4':44,'e4':54,'f4':64,'g4':74,'h4':84
    ,'a5':15,'b5':25,'c5':35,'d5':45,'e5':55,'f5':65,'g5':75,'h5':85
    ,'a6':16,'b6':26,'c6':36,'d6':46,'e6':56,'f6':66,'g6':76,'h6':86
    ,'a7':17,'b7':27,'c7':37,'d7':47,'e7':57,'f7':67,'g7':77,'h7':87
    ,'a8':18,'b8':28,'c8':38,'d8':48,'e8':58,'f8':68,'g8':78,'h8':88}
    if (x-y)%11 == 0:
        print('Bishop can attack knight')
    else:
        print("Bishop can't attack knight")
    if abs(x-y) == 21 or abs(x-y) == 12 :
        print('knight can attack Bishop')
    else:
        print("knight can't attack Bishop")
print(ex4('d4','f5'))
