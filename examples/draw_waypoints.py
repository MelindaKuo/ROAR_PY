import roar_py_carla
import roar_py_interface
import carla
import numpy as np
import asyncio
from typing import Optional, Dict, Any
import matplotlib.pyplot as plt
import transforms3d as tr3d


def new_x_y(x, y):
        new_location = np.array([x, y, 0])
        return roar_py_interface.RoarPyWaypoint(location=new_location, 
                                                roll_pitch_yaw=np.array([0,0,0]), 
                                                lane_width=5)
startInd_8 = 1800
endInd_8 = 2006
startInd_12 = 2586


async def main():
    carla_client = carla.Client('localhost', 2000)
    carla_client.set_timeout(15.0)
    roar_py_instance = roar_py_carla.RoarPyCarlaInstance(carla_client)
    
    carla_world = roar_py_instance.world
    carla_world.set_asynchronous(True)
    carla_world.set_control_steps(0.00, 0.005)
    
    print("Map Name", carla_world.map_name)
    waypoints = roar_py_instance.world.maneuverable_waypoints
    spawn_points = roar_py_instance.world.spawn_points
    roar_py_instance.close()
    
    with plt.ion():

        for waypoint in (waypoints[:] if waypoints is not None else []):
            rep_line = waypoint.line_representation
            rep_line = np.asarray(rep_line)
            waypoint_heading = tr3d.euler.euler2mat(*waypoint.roll_pitch_yaw) @ np.array([1,0,0])
            plt.arrow(
                waypoint.location[0], 
                waypoint.location[1], 
                waypoint_heading[0] * 1, 
                waypoint_heading[1] * 1, 
                width=0.5, 
                color='r'
            )
            plt.plot(rep_line[:,0], rep_line[:,1])
            plt.pause(0.0001)
        for spawn_point in spawn_points:
            spawn_point_heading = tr3d.euler.euler2mat(0,0,spawn_point[1][2]) @ np.array([1,0,0])
            plt.arrow(
                spawn_point[0][0], 
                spawn_point[0][1], 
                spawn_point_heading[0] * 20, 
                spawn_point_heading[1] * 20, 
                width=5, 
                color='r'
            )

    plt.plot(-248.960205078125,	773.6961669921875, 'go', color = 'r')
    plt.plot(210.42477416992188,	906.4281005859375, 'go', color = 'r')
    plt.plot(396.6437683105469,	989.9536743164062,'go', color = 'r')
    plt.plot(670.3635864257812,	1080.6585693359375, 'go',color = 'r')
    plt.plot(758.5154418945312,	886.81201171875, 'go',color = 'r')
    plt.plot(751.64453125,	725.7698364257812, 'go',color = 'r')
    plt.plot(114.87178802490234, 223.9172821044922, 'go',color = 'r')
    plt.plot(-76.38444519042969, -144.82717895507812, 'go',color = 'r')
    plt.plot(-109.53840637207031, -835.9786987304688,'go', color = 'r')
    plt.plot(-162.36941528320312, -1052.62744140625,'go', color = 'r')
    plt.plot(-369.08758544921875, -579.8623046875, 'go',color = 'r')
    plt.plot(-342.70880126953125, 73.59059143066406, 'go', color = 'r')
    plt.plot(-281.25653076171875, 383.2958679199219, 'go', color = 'r')
    plt.show()

if __name__ == '__main__':
    asyncio.run(main())