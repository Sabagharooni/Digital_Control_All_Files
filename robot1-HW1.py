# rcj_soccer_player controller - ROBOT B1

import math  # noqa: F401
import utils
from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP


class MyRobot1(RCJSoccerRobot):
    def run(self):
        while self.robot.step(TIME_STEP) != -1:
            if self.is_new_data():
                data = self.get_new_data()  # noqa: F841
                I =0   #I=0 the first time - it will be updated for PID controller

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

                # Get data from compass (ANGLE)-------------------------------------------------------
                heading = self.get_compass_heading()  # noqa: F841
                
                # Get GPS coordinates of the robot (X,Y)----------------------------------------------
                robot_pos = self.get_gps_coordinates()  # noqa: F841
                #print(robot_pos)

                # Get data from sonars----------------------------------------------------------------
                sonar_values = self.get_sonar_values()  # noqa: F841
                
                
                # x position is in robot_pos[1]-------------------------------------------------------
                x_desire =-0.5
                posx_error =  robot_pos[1] - x_desire

                # Controller design -----------------------------------------------------------------
                k1=10  #Gain

                I = I + posx_error  #Update of I value
                v1 = k1*posx_error + I
              
                self.left_motor.setVelocity(v1)
                self.right_motor.setVelocity(v1)
