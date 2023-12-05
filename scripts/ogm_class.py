# import
# class
# ogm.show() return img
# ogm.update(values)
#ogm
#!/usr/bin/env python3

import rospy
from nav_msgs.msg import OccupancyGrid
from std_msgs.msg import PoseStamped
import matplotlib.pyplot as plt
import numpy as np
from std_msgs.msg import Header

class OccupancyGridMap:
    def __init__(self,resolution=0.15,width = 100 ,height = 100, **kwargs):
        rospy.init_node('occupancy_grid_map_node')
        self.grid_map = None
        #self.resolution = kwargs.get('resolution', 0.15)
        self.resolution = resolution  
        self.width = width  
        self.height = height  

        self.pub = rospy.Publisher('map', OccupancyGrid, queue_size=10)
        self.setup_occupancy_grid()
    
    def setup_occupancy_grid(self):
        self.occupancy_grid = OccupancyGrid()
        self.occupancy_grid.header = Header()
        self.occupancy_grid.header.frame_id = "map"
        self.occupancy_grid.info.resolution = self.resolution
        self.occupancy_grid.info.width = self.width
        self.occupancy_grid.info.height = self.height
        self.occupancy_grid.data = [0] * (self.width * self.height)

    def publish_occupancy_grid(self):
        # Update the timestamp before publishing
        self.occupancy_grid.header.stamp = rospy.Time.now()

        # Publish the occupancy grid map
        self.pub.publish(self.occupancy_grid)
            #rate.sleep()
        rospy.signal_shutdown("Occupancy grid map was published.")

    def modify_occupancy_grid(self, indices, values):
        """
        Modify the occupancy grid map using a list of indices and values.

        :param indices: List of indices to modify.
        :param values: List of values corresponding to the indices.
        """
        if len(indices) != len(values):
            rospy.logerr("Number of indices must be equal to the number of values.")
            return

        for index, value in zip(indices, values):
            if 0 <= index < len(self.occupancy_grid.data):
                self.occupancy_grid.data[index] = value
            else:
                rospy.logwarn("Index {} is out of bounds for the occupancy grid map.".format(index))


        plt.ion()
        self.fig, self.ax = plt.subplots()
        self.im = self.ax.imshow(np.zeros((self.height, self.width)), cmap='gray', origin='lower', vmin=0, vmax=100)
        plt.colorbar(self.im, ax=self.ax, orientation='vertical')
        plt.title('Occupancy Grid Map')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')

    def map_callback(self, data):
        self.grid_map = np.array(data.data).reshape((data.info.height, data.info.width))
        self.grid_map = np.flipud(self.grid_map)
        self.update_plot()

    def update_plot(self):
        if self.grid_map is not None:
            self.im.set_array(self.grid_map)
            plt.draw()
            plt.pause(0.01)  # Add a small pause to allow for visualization update

    def run(self):
        rospy.spin()


if __name__ == '__main__':
    try:
        occupancy_grid_map = OccupancyGridMap()
        
        # Example: Modify occupancy grid map at specific indices
        indices_to_modify = [10, 20, 30]
        values_to_set = [50, 75, 90]

        occupancy_grid_map.modify_occupancy_grid(indices_to_modify, values_to_set)

        # Publish the modified occupancy grid map
        occupancy_grid_map.publish_occupancy_grid()

    except rospy.ROSInterruptException:
        pass