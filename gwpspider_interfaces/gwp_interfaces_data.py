# TOPICS
# Arduino
GRIPPER_STATES_TOPIC = 'grippers_states'
BNO_DATA_TOPIC = 'bno_data_topic'
BATTERY_VOLTAGE_TOPIC = 'battery_voltage_topic'

# Controller
LEGS_STATES_TOPIC = 'legs_states_topic'
COMMANDED_JOINTS_VELOCITIES_TOPIC = 'commanded_joint_velocities_topic'

# Dynamixel
DYNAMIXEL_MOTORS_DATA_TOPIC = 'dynamixel_motors_data'

# App
SPIDER_POSE_TOPIC = 'spider_pose_topic'


# SERVICES
# Arduino
MOVE_GRIPPER_SERVICE = 'move_gripper_service'
WATER_PUMP_SERVICE = 'water_pump_service'
STOP_WATER_PUMP_SERVICE = 'stop_water_pump_service'
INIT_BNO_SERVICE = 'init_bno_service'
BREAKS_SERVICE = 'breaks_service'
TUBE_HOLDER_SERVICE = 'tube_holder_service'

# Controller
MOVE_LEG_SERVICE = 'move_leg_service'
MOVE_SPIDER_SERVICE = 'move_spider_service'
TOGGLE_CONTROLLER_SERVICE = 'toggle_controller_service'
DISTRIBUTE_FORCES_SERVICE = 'distribute_forces_service'
APPLY_FORCES_ON_LEGS_SERVICE = 'apply_forces_on_legs_service'
UPDATE_LAST_LEGS_POSITIONS_SERVICE = 'update_last_legs_positions_service'
GET_SPIDER_POSE_SERVICE = 'get_spider_pose_service'
MOVE_LEG_VELOCITY_MODE_SERVICE = 'move_leg_velocity_mode_service'
TOGGLE_ADDITIONAL_CONTROLLER_MODE_SERVICE = 'toggle_additional_controller_mode_service'
STOP_LEGS_SERVICE = 'stop_legs_service'

#Server
SEND_GOAL_SERVICE = 'spider_goal_service'
SET_WATERING_SUCCESS_SERVICE = 'set_watering_success_service'
MESSAGE_SERVICE = 'message_service'

# Dynamixel
TOGGLE_MOTORS_TORQUE_SERVICE = 'toggle_motors_torque_service'
SET_BUS_WATCHDOG_SERVICE = 'set_bus_watchdog_service'
REBOOT_MOTORS_SERVICE = 'reboot_motors_service'

# Planning
GET_WALKING_INSTRUCTIONS_SERVICE = 'get_walking_instructions_service'
GET_MODIFIED_WALKING_INSTRUCTION_SERVICE = 'get_modified_walking_instructions_service'
GET_LEG_TRAJECTORY_SERVICE = 'get_leg_trajectory_service'
GET_OFFSETS_TO_CHARGING_POSITION_SERVICE = 'get_offsets_to_charging_position_service'

# Offset Predictor
GET_CORRECTION_OFFSET_SERVICE = 'get_correction_offset_service'

# App
STATES_MANAGER_SERVICE = 'states_manager_service'
IMMEDIATE_STOP_SERVICE = 'idle_state_service'

# Safety
TOGGLE_BATTERY_VOLTAGE_MONITORING_SERVICE = 'monitor_battery_voltage_service'
TOGGLE_HW_ERRORS_MONITORING_SERVICE = 'monitor_hw_errors_service'
BATTERY_VOLTAGE_TRIGGER_SERVICE = 'battery_voltage_service'
TOGGLE_GRIPPERS_MONITORING_SERVICE = 'monitor_gripper_errors_service'
