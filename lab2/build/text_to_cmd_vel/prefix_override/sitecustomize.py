import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/alex/robot/ros/ROSNSU/lab2/install/text_to_cmd_vel'
