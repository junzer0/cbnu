from math import*

def angle(x1,y1,x2,y2,x3,y3):
    ax,ay = x1-x2, y1-y2 ; bx,by = x3-x2, y3-y2
    a = sqrt(ax**2+ay**2) ; b = sqrt(bx**2+by**2)
    adotb=ax*bx+ay*by
    temp=adotb/(a+b)
    temp=1 if temp > 1 else temp
    temp=-1 if temp < -1 else temp
    theta=acos(temp)*180/3.141592654
    return theta
    
while True:
    x1,y1 = map(float, input('Point 1: x1,y1').split())
    x2,y2 = map(float, input('Point 2: x2,y2').split())
    x3,y3 = map(float, input('Point 3: x3,y3').split())
    x4,y4 = map(float, input('Point 4: x4,y4').split())
    
    a1=angle(x2,y2,x1,y1,x4,y4)
    a2=angle(x1,y1,x2,y2,x3,y3)
    a3=angle(x2,y2,x3,y3,x4,y4)
    a4=angle(x1,y1,x4,y4,x3,y3)
    
    print('Theta_P1, Theta_P2, Theta_P3, Theta_P4(deg.)={0:7.2f}{1:7.2f}{2:7.2f}{3:7.2f}'.format(a1,a2,a3,a4))
    print('sum of angle(deg.)={0:7.2f}'.format(a1+a2+a3+a4))
    