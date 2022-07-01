# rcj_soccer_player controller - ROBOT B1

# Feel free to import built-in libraries
import math  # noqa: F401

# You can also import scripts that you put into the folder with controller
import utils
from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP


class MyRobot1(RCJSoccerRobot):
    def run(self):
        while self.robot.step(TIME_STEP) != -1:
            if self.is_new_data():
                data = self.get_new_data()  # noqa: F841
                I =0
                while self.is_new_team_data():
                    team_data = self.get_new_team_data()  # noqa: F841
                    # Do something with team data

                if self.is_new_ball_data():
                    ball_data = self.get_new_ball_data()
                else:
                    # If the robot does not see the ball, stop motors
                    self.left_motor.setVelocity(0)
                    self.right_motor.setVelocity(0)
                    continue

                # Get data from compass
                heading = self.get_compass_heading()  # noqa: F841
                
                # Get GPS coordinates of the robot
                robot_pos = self.get_gps_coordinates()  # noqa: F841
                print(robot_pos)
                # Get data from sonars
                sonar_values = self.get_sonar_values()  # noqa: F841
                
                angle_desire = (3.14/2)
                x_desire =0.5
                y_desire =0.5


                posx_error =  robot_pos[1] - x_desire
                k1=20
                I = I + posx_error
                v1 = k1*posx_error + I

                self.left_motor.setVelocity(v1)
                self.right_motor.setVelocity(v1)

                if(abs(posx_error)<0.05):
                    angle_error =  heading- angle_desire
                    k0=10
                    v0 = k0*angle_error
                    self.left_motor.setVelocity(0)
                    self.right_motor.setVelocity(v0)

                    if(abs(angle_error)<(0.01*3.14)):
                        posy_error =  robot_pos[0] - y_desire
                        k2=10
                        v2 = k2*posy_error 

                        self.left_motor.setVelocity(v2)
                        self.right_motor.setVelocity(v2)