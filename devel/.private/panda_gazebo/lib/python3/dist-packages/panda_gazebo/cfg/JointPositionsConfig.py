## *********************************************************
##
## File autogenerated for the panda_gazebo package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'name': 'Default', 'type': '', 'state': True, 'cstate': 'true', 'id': 0, 'parent': 0, 'parameters': [], 'groups': [{'name': 'arm', 'type': '', 'state': True, 'cstate': 'true', 'id': 1, 'parent': 0, 'parameters': [{'name': 'joint1_position', 'type': 'double', 'default': 0.0, 'level': 0, 'description': 'Joint 1 position control command', 'min': -2.8973, 'max': 2.8973, 'srcline': 12, 'srcfile': '/workspaces/ros-gazebo-gym-ws/src/rosdeps/panda_gazebo/panda_gazebo/cfg/dyn_reconf/PositionControlTestDynReconf.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'joint2_position', 'type': 'double', 'default': 0.0, 'level': 1, 'description': 'Joint 2 position control command', 'min': -1.7628, 'max': 1.7628, 'srcline': 13, 'srcfile': '/workspaces/ros-gazebo-gym-ws/src/rosdeps/panda_gazebo/panda_gazebo/cfg/dyn_reconf/PositionControlTestDynReconf.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'joint3_position', 'type': 'double', 'default': 0.0, 'level': 2, 'description': 'Joint 3 position control command', 'min': -2.8973, 'max': 2.8973, 'srcline': 14, 'srcfile': '/workspaces/ros-gazebo-gym-ws/src/rosdeps/panda_gazebo/panda_gazebo/cfg/dyn_reconf/PositionControlTestDynReconf.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'joint4_position', 'type': 'double', 'default': 0.0, 'level': 3, 'description': 'Joint 4 position control command', 'min': -3.0718, 'max': -0.0698, 'srcline': 15, 'srcfile': '/workspaces/ros-gazebo-gym-ws/src/rosdeps/panda_gazebo/panda_gazebo/cfg/dyn_reconf/PositionControlTestDynReconf.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'joint5_position', 'type': 'double', 'default': 0.0, 'level': 4, 'description': 'Joint 5 position control command', 'min': -2.8973, 'max': 2.8973, 'srcline': 16, 'srcfile': '/workspaces/ros-gazebo-gym-ws/src/rosdeps/panda_gazebo/panda_gazebo/cfg/dyn_reconf/PositionControlTestDynReconf.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'joint6_position', 'type': 'double', 'default': 0.0, 'level': 5, 'description': 'Joint 6 position control command', 'min': -0.0175, 'max': 3.7525, 'srcline': 17, 'srcfile': '/workspaces/ros-gazebo-gym-ws/src/rosdeps/panda_gazebo/panda_gazebo/cfg/dyn_reconf/PositionControlTestDynReconf.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'joint7_position', 'type': 'double', 'default': 0.0, 'level': 6, 'description': 'Joint 7 position control command', 'min': -2.8973, 'max': 2.8973, 'srcline': 18, 'srcfile': '/workspaces/ros-gazebo-gym-ws/src/rosdeps/panda_gazebo/panda_gazebo/cfg/dyn_reconf/PositionControlTestDynReconf.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}], 'groups': [], 'srcline': 124, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT::ARM', 'parentclass': 'DEFAULT', 'parentname': 'Default', 'field': 'DEFAULT::arm', 'upper': 'ARM', 'lower': 'arm'}, {'name': 'hand', 'type': '', 'state': True, 'cstate': 'true', 'id': 2, 'parent': 0, 'parameters': [{'name': 'width', 'type': 'double', 'default': 0.0, 'level': 7, 'description': 'Gripper width', 'min': 0.0, 'max': 0.08, 'srcline': 22, 'srcfile': '/workspaces/ros-gazebo-gym-ws/src/rosdeps/panda_gazebo/panda_gazebo/cfg/dyn_reconf/PositionControlTestDynReconf.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'speed', 'type': 'double', 'default': 0.2, 'level': 8, 'description': 'Gripper speed', 'min': 0.0, 'max': 0.2, 'srcline': 31, 'srcfile': '/workspaces/ros-gazebo-gym-ws/src/rosdeps/panda_gazebo/panda_gazebo/cfg/dyn_reconf/PositionControlTestDynReconf.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}], 'groups': [], 'srcline': 124, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT::HAND', 'parentclass': 'DEFAULT', 'parentname': 'Default', 'field': 'DEFAULT::hand', 'upper': 'HAND', 'lower': 'hand'}], 'srcline': 246, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT', 'parentclass': '', 'parentname': 'Default', 'field': 'default', 'upper': 'DEFAULT', 'lower': 'groups'}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

