import rclpy
from rclpy.node import Node
from rclpy.logging import get_logger
from time import sleep
import time

from .driver.packet import *
from .driver.port import *

class GrobotMotorSettingNode(Node):
  def __init__(self):
    super().__init__('grobot_motor_setting')

    # Get parameter values
    _port_name = self.get_parameter_or('/port/name', Parameter('/port/name', Parameter.Type.STRING, '/dev/ttyMotor')).get_parameter_value().string_value ## MCU -> USB0 -> Motor
    _port_baudrate = self.get_parameter_or('/port/baudrate', Parameter('/port/baudrate', Parameter.Type.INTEGER, 115200)).get_parameter_value().integer_value

    self.motor_gear_ratio = self.get_parameter_or('/motor/gear_ratio', Parameter('/motor/gear_ratio', Parameter.Type.INTEGER, 213)).get_parameter_value().integer_value
    self.wheel_separation = self.get_parameter_or('/wheel/separation', Parameter('/wheel/separation', Parameter.Type.DOUBLE, 0.17)).get_parameter_value().double_value # 0.085 cm x 2
    self.wheel_radius = self.get_parameter_or('/wheel/radius', Parameter('/wheel/radius', Parameter.Type.DOUBLE, 0.0335)).get_parameter_value().double_value
    self.sensor_enc_pulse = self.get_parameter_or('/sensor/enc_pulse', Parameter('/sensor/enc_pulse', Parameter.Type.INTEGER, 44)).get_parameter_value().integer_value

    self.packet = Packet(Port(_port_name, _port_baudrate))

    # Set gear ratio
    self.set_gear_ratio()

    # Get gear ratio
    print(self.get_gear_ratio())

    # Run robot
    self.run_motors()

  def set_gear_ratio(self):
    self.packet.write_data('GEAR', {'ratio': self.gear_ratio})

  def get_gear_ratio(self):
    return self.packet.read_data('GEAR')['ratio']

  def run_motors(self):
    cnt = 0
    while cnt < 6000:
      cnt += 1
      sleep(0.01)
      self.packet.write_data('RPM', {'left': 12, 'right':12})

def main(args=None):
  # rclpy.init(args=args) // 여기부터
  # GrobotMotorSettingNode = GrobotMotorSettingNode()
  # try:
  #   rclpy.spin(GrobotMotorSettingNode)
  # finally:
  #   GrobotMotorSettingNode.destroy_node()
  #   rclpy.shutdown() // 여기까지 진짜
  rclpy.init(args=args) # 여기도 추가
  grobotMotorSettingNode = GrobotMotorSettingNode()
  rclpy.spin(grobotMotorSettingNode)
  
  grobotMotorSettingNode.destroy_node()
  rclpy.shutdown() # 여기가 추가
if __name__ == '__main__':
  main()
