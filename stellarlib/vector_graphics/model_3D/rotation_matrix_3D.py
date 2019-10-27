from math import sin, cos, radians


class RotationMatrix3D(object):

    @staticmethod
    def rotate((vx, vy, vz), angle):

        th = radians(angle)

        #vx, vy, vz = RotationMatrix3D.rotate_about_x_axis((vx, vy, vz), th)
        vx, vy, vz = RotationMatrix3D.rotate_about_y_axis((vx, vy, vz), th)
        #vx, vy, vz = RotationMatrix3D.rotate_about_z_axis((vx, vy, vz), th)

        return vx, vy, vz

    @staticmethod
    def rotate_about_x_axis((vx, vy, vz), th):

        y = vy * cos(th) + vz * sin(th)
        z = vy * -sin(th) + vz * cos(th)

        return vx, y, z

    @staticmethod
    def rotate_about_y_axis((vx, vy, vz), th):

        x = vx * cos(th) - vz * sin(th)
        z = vx * sin(th) + vz * cos(th)

        return x, vy, z

    @staticmethod
    def rotate_about_z_axis((vx, vy, vz), th):

        x = vx * cos(th) + vy * sin(th)
        y = vx * -sin(th) + vy * cos(th)

        return x, y, vz
