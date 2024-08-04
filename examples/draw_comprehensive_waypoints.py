import roar_py_carla
import roar_py_interface
import carla
import numpy as np
import asyncio
import matplotlib.pyplot as plt
import transforms3d as tr3d

# Define section indices and colors
section_indices = [198, 438, 547, 691, 803, 884, 1287, 1508, 1854, 1968, 2264, 2592, 2770]
section_colors = [
    'r', 'g', 'b', 'c', 'm', 'y', 'k', '#ff5733', '#33ff57', '#3357ff', '#57ff33', '#ff33a1', '#a133ff'
]





async def main():
    carla_client = carla.Client('localhost', 2000)
    carla_client.set_timeout(15.0)
    roar_py_instance = roar_py_carla.RoarPyCarlaInstance(carla_client)
    
    carla_world = roar_py_instance.world
    carla_world.set_asynchronous(True)
    carla_world.set_control_steps(0.00, 0.005)

    comprehensive_waypoints = roar_py_instance.world.comprehensive_waypoints
    spawn_points = roar_py_instance.world.spawn_points
    roar_py_instance.close()
    
    lap_length = len(next(iter(comprehensive_waypoints.values())))  # Get the length of waypoints in one lap
    print(f"Lap length: {lap_length}")  # Print lap length  2974

    
    # Plot spawn points
    with plt.ion():
        # for spawn_point in spawn_points:
        #     spawn_point_heading = tr3d.euler.euler2mat(0,0,spawn_point[1][2]) @ np.array([1,0,0])
        #     plt.arrow(
        #         spawn_point[0][0], 
        #         spawn_point[0][1], 
        #         spawn_point_heading[0] * 50, 
        #         spawn_point_heading[1] * 50, 
        #         width=10, 
        #         color='r'
        #     )
        points = 0 
        for lane_id, waypoint_list in comprehensive_waypoints.items():
            for waypoint in waypoint_list:


                rep_line = waypoint.line_representation
                rep_line = np.asarray(rep_line)
                waypoint_heading = tr3d.euler.euler2mat(*waypoint.roll_pitch_yaw) @ np.array([1,0,0])
                plt.arrow(
                    waypoint.location[0], 
                    waypoint.location[1], 
                    waypoint_heading[0] * 0.5, 
                    waypoint_heading[1] * 0.5, 
                    width=0.5, 
                    color='r'
                )
                if lane_id == 1:
                    plt.plot(rep_line[:,0], rep_line[:,1], label="Lane {}".format(lane_id), color='r')
                else:
                    plt.plot(rep_line[:,0], rep_line[:,1], label="Lane {}".format(lane_id), color='b')
    
    plt.plot(-248.960205078125,	773.6961669921875, 'go')
    plt.plot(210.42477416992188,	906.4281005859375, 'go')
    plt.plot(396.6437683105469,	989.9536743164062, 'go')
    plt.plot(670.3635864257812,	1080.6585693359375, 'go')
    plt.plot(758.5154418945312,	886.81201171875, 'go')
    plt.plot(751.64453125,	725.7698364257812, 'go')
    plt.plot(114.87178802490234	,223.9172821044922, 'go')
    plt.plot(-76.38444519042969	,-144.82717895507812, 'go')
    plt.plot(-106.93980407714844, -833.9811401367188, 'go')
    plt.plot(-153.56297302246094, -1047.9649649606927, 'go')
    plt.plot(-369.275146484375	-583.85791015625, 'go', color = 'y')
    plt.plot(-343.258935546875, 67.59391784667969, 'go', color = 'y')
    plt.plot(-278.21466064453125, 381.3706665039063, 'go', color = 'y')
        
    plt.show()

if __name__ == '__main__':
    asyncio.run(main())
