from functools import singledispatch
import math
import IO as io
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return "point:({0},{1})".format(self.x,self.y)
    def __add__(self, other):
        x=self.x+other.x
        y=self.y+other.y
        return Point(x,y)
    def __sub__(self, other):
        x=self.x-other.x
        y=self.y-other.y
        return Point(x,y)
    def __mul__(self, other):
        return Point(self.x*other,self.y*other)
    # 右乘 实例在乘数位置
    def __rmul__(self, other):
        return self.__mul__(other)
    def __eq__(self, other):
        return math.fabs(self.x-other.x)<1e-10 and math.fabs(self.y-other.y)<1e-10
    def abs(self):
        return math.sqrt(self.norm())
    def norm(self):
        return self.x*self.x+self.y*self.y

# 相对原点的向量
class Vector:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return "vector:({0},{1})".format(self.x,self.y)
    def __add__(self, other):
        x=self.x+other.x
        y=self.y+other.y
        return Vector(x,y)
    def __sub__(self, other):
        x=self.x-other.x
        y=self.y-other.y
        return Vector(x,y)
    def __mul__(self, other):
        return Point(self.x*other,self.y*other)
    # 右乘 实例在乘数位置
    def __rmul__(self, other):
        return self.__mul__(other)
    def __neg__(self):
        return Vector(-self.x,-self.y)
    def __truediv__(self, other):
        return Vector(self.x/other,self.y/other)
    # 模
    def abs(self):
        return math.sqrt(self.norm())
    # 范数
    def norm(self):
        return self.x*self.x+self.y*self.y

# 线段
class Segment:
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2

# 直线
class Line:
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2

class Circle:
    def __init__(self,center,radius):
        self.center=center
        self.radius=radius

# 多边形 点的序列表示
class Polygon:
    def __init__(self,points):
        self.points=points

def dot(v1,v2):
    return v1.x*v2.x+v1.y*v2.y
def cross(v1,v2):
    return v1.x*v2.y-v1.y*v2.x

@singledispatch
def equals(f1,f2):
    # 默认float
    return math.fabs(f1-f2)<1e-10
@equals.register(Vector)
def _(v1,v2):
    # vector
    return (v1-v2).abs()<1e-10
@equals.register(Point)
def _(p1,p2):
    return math.fabs(p1.x-p2.x)<1e-10 and math.fabs(p1.y-p2.y)<1e-10

def isOrthogonal_vector(v1,v2):
    return equals(dot(v1,v2),0.0)

def isOrthogonal_point(p1,p2,p3,p4):
    return equals(dot(p2-p1,p4-p3),0.0)

def isOrthogonal_segment(s1,s2):
    return equals(dot(s1.p2-s1.p1,s2.p2-s2.p1),0.0)

def isParallel_vector(v1,v2):
    return equals(cross(v1,v2),0.0)

def isParallel_point(p1,p2,p3,p4):
    v1=Vector(p2.x-p1.x,p2.y-p1.y)
    v2=Vector(p4.x-p3.x,p4.y-p3.y)
    return isParallel_vector(v1,v2)

def isParallel_segment(s1,s2):
    return isParallel_point(s1.p1,s1.p2,s2.p1,s2.p2)

def project(s,p):
    base=Vector((s.p2-s.p1).x,(s.p2-s.p1).y)
    hypo=Vector((p-s.p1).x,(p-s.p1).y)
    k=float(dot(base,hypo)/base.norm())
    return s.p1+base*k

def reflect(s,p):
    return p+(project(s,p)-p)*2.0

@singledispatch
def distance(p1,p2):
    # 点到点之间距离
    v=Vector(p2.x-p1.x,p2.y-p1.y)
    return v.abs()
@distance.register(Line)
def _(l,p):
    # 点到直线距离
    p1=l.p1
    p2=l.p2
    vb=Vector(p2.x-p1.x,p2.y-p1.y)
    v=Vector(p.x-p1.x,p.y-p1.y)
    return math.fabs(cross(vb,v)/vb.abs())
@distance.register(Segment)
def _(s,p):
    # 点到线段距离
    p1=s.p1
    p2=s.p2
    vb=Vector(p2.x-p1.x,p2.y-p1.y)
    v1=Vector(p.x-p1.x,p.y-p1.y)
    v2=Vector(p.x-p2.x,p.y-p2.y)
    if dot(vb,v1)<0:return v1.abs()
    elif dot(-vb,v2)<0:return v2.abs()
    else:
        return distance(Line(p1, p2), p)

# 线段与线段之间的距离
def distance_segment(s1,s2):
    if intersect_segment(s1,s2):
        return 0.0
    return min(distance(s1,s2.p1),distance(s1,s2.p2),distance(s2,s1.p1),distance(s2,s1.p2))

def ccw(p1,p2,p):
    vb=Vector(p2.x-p1.x,p2.y-p1.y)
    v=Vector(p.x-p1.x,p.y-p1.y)
    if cross(vb,v)>1e-10:return 1
    elif cross(vb,v)<-1e-10:return -1
    elif dot(vb,v)<-1e-10:return 2
    elif vb.norm()<v.norm():return -2
    else: return 0

def intersect(p1,p2,p3,p4):
    return ccw(p1,p2,p3)*ccw(p1,p2,p4)<=0 and ccw(p3,p4,p1)*ccw(p3,p4,p2)<=0

def intersect_segment(s1,s2):
    return intersect(s1.p1,s1.p2,s2.p1,s2.p2)

def intersect_point(s1,s2):
    base=Vector((s2.p2-s2.p1).x,(s2.p2-s2.p1).y)
    v1=Vector((s1.p1-s2.p1).x,(s1.p1-s2.p1).y)
    v2=Vector((s1.p2-s2.p1).x,(s1.p2-s2.p1).y)
    d1=math.fabs(cross(base,v1))/base.abs()
    d2=math.fabs(cross(base,v2))/base.abs()
    t=d1/(d1+d2)
    return s1.p1+(s1.p2-s1.p1)*t

# 求直线和圆的交点坐标
# 如果只有一个交点返回两次
@singledispatch
def intersect_circle_point(l,c):
    d=distance(l,c.center)
    assert c.radius>=d,"no intersection"
    pr=project(l,c.center)
    vl=Vector((l.p2-l.p1).x,(l.p2-l.p1).y)
    e=vl/vl.abs()
    base=math.sqrt(c.radius*c.radius-d*d)
    p1,p2= pr + e * base, pr - e * base
    # 按字典序排序 (x优先, y次之)
    if (p1.x, p1.y) > (p2.x, p2.y):
        p1, p2 = p2, p1
    return p1,p2
# 圆与圆的交点
def polar(a,r):
    return Point(math.cos(r)*a,math.sin(r)*a)
@intersect_circle_point.register(Circle)
def _(c1,c2):
    d=distance(c1.center,c2.center) # 圆心之间距离
    assert d<=c1.radius+c2.radius,"no intersection"
    alpha=math.acos((c1.radius*c1.radius+d*d-c2.radius*c2.radius)/(2*c1.radius*d))
    theta=math.atan2((c2.center-c1.center).y,(c2.center-c1.center).x)
    p1,p2=c1.center+polar(c1.radius,theta+alpha),c1.center+polar(c1.radius,theta-alpha)
    if (p1.x, p1.y) > (p2.x, p2.y):
        p1, p2 = p2, p1
    return p1,p2

def main():
    c1 = Circle(Point(io.read_int(), io.read_int()), io.read_int())
    c2 = Circle(Point(io.read_int(), io.read_int()), io.read_int())
    p1,p2=intersect_circle_point(c1,c2)
    print(f"{p1.x:.8f} {p1.y:.8f} {p2.x:.8f} {p2.y:.8f}")

if __name__== "__main__":
    main()
