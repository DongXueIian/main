import time
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix
from geographiclib.geodesic import Geodesic
apmControllernNameSpace='/apm_drone'
class GPSPublisherNode(Node):
    def __init__(self):
        super().__init__('gps_publisher_node')

        # # 原始坐标
        # original_latitude = -35.3632622
        # original_longitude = 149.1652373
        # original_altitude = 584.09

        # # 计算北边10米的目标坐标
        # geod = Geodesic.WGS84
        # target_location = geod.Direct(original_latitude, original_longitude,50, -50)
        # # 创建NavSatFix消息
        # msg = NavSatFix()
        # msg.header.stamp = self.get_clock().now().to_msg()
        # msg.header.frame_id = 'world'
        # msg.latitude = target_location['lat2']
        # msg.longitude = target_location['lon2']
        # msg.altitude = original_altitude
        
        # # 创建NavSatFix消息
        # msg = NavSatFix()
        # msg.header.stamp = self.get_clock().now().to_msg()
        # msg.header.frame_id = 'world'
        # msg.latitude = self.dms_to_dd(12,12,12)
        # msg.longitude = self.dms_to_dd(14,14,14)
        # msg.altitude = original_altitude

        # 创建NavSatFix消息
        msg = NavSatFix()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'world'
        msg.latitude = 30.3097368

        msg.longitude = 120.3822239

        msg.altitude = 100.0

        # 创建发布者
        self.publisher_ = self.create_publisher(NavSatFix, apmControllernNameSpace+'/target_gps_location', 10)
        time.sleep(0.5)
        count =0
        while count<20000:
            count=count+1
            # 发布消息
            self.publisher_.publish(msg)
            self.get_logger().info('Published target GPS location: lat={}, lon={}, alt={}'.format(msg.latitude, msg.longitude, msg.altitude))
            time.sleep(0.2)

    def dms_to_dd(degrees, minutes, seconds):
        return degrees + minutes / 60 + seconds / 3600

def main(args=None):
    rclpy.init(args=args)
    node = GPSPublisherNode()
    rclpy.spin_once(node, timeout_sec=0)  # 只执行一次
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
