import math
import rclpy
from rclpy.node import Node
from angle_interface.srv import Data

L1 = 69.5  # mm
L2 = 71.5  # mm

def Rx(a):
    c, s = math.cos(a), math.sin(a)
    return [[1,0,0,0],
            [0,c,-s,0],
            [0,s, c,0],
            [0,0,0,1]]

def Ry(a):
    c, s = math.cos(a), math.sin(a)
    return [[ c,0, s,0],
            [ 0,1, 0,0],
            [-s,0, c,0],
            [ 0,0, 0,1]]

def Tz(d):
    return [[1,0,0,0],
            [0,1,0,0],
            [0,0,1,d],
            [0,0,0,1]]

def mmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]

class ServidorFK(Node):
    def __init__(self):
        super().__init__('servidor_fk_aibo')
        self.srv = self.create_service(Data, 'Data', self.compute_fk)
        self.get_logger().info('Servicio /Data listo.')

    def compute_fk(self, req, resp):
        # grados -> radianes
        i1 = math.radians(req.i1)
        i2 = math.radians(req.i2)
        i3 = math.radians(req.i3)

        M = Rx(i1)
        M = mmul(M, Ry(i2))
        M = mmul(M, Tz(-L1))
        M = mmul(M, Ry(i3))
        M = mmul(M, Tz(-L2))

        resp.ox = M[0][3]
        resp.oy = M[1][3]
        resp.oz = M[2][3]

        self.get_logger().info(f"θ=[{req.i1:.1f}, {req.i2:.1f}, {req.i3:.1f}]  -> "
                               f"p=[{resp.ox:.2f}, {resp.oy:.2f}, {resp.oz:.2f}] mm")
        return resp

def main(args=None):
    rclpy.init(args=args)
    node = ServidorFK()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()