cmake_minimum_required(VERSION 3.8)
project(gwpspider_interfaces)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(std_msgs REQUIRED)

set(msg_files
  "msg/GripperCommand.msg"
  "msg/WaterPumpCommand.msg"
  "msg/BnoData.msg"
  "msg/DynamixelMotorsData.msg"
  "msg/WalkingInstructions.msg"
  "msg/LegTrajectory.msg"
  "msg/LegsStates.msg"
  "msg/GripperState.msg"
  "msg/GrippersStates.msg"
)

set(srv_files
  "srv/MoveGripper.srv"
  "srv/ControlWaterPump.srv"
  "srv/InitBno.srv"
  "srv/ToggleMotorsTorque.srv"
  "srv/SetBusWatchdog.srv"
  "srv/GetWalkingInstructions.srv"
  "srv/GetModifiedWalkingInstructions.srv"
  "srv/GetLegTrajectory.srv"
  "srv/RebootMotors.srv"
  "srv/MoveLeg.srv"
  "srv/MoveSpider.srv"
  "srv/ToggleController.srv"
  "srv/DistributeForces.srv"
  "srv/ApplyForcesOnLegs.srv"
  "srv/GetSpiderPose.srv"
  "srv/MoveLegVelocityMode.srv"
  "srv/ToggleAdditionalControllerMode.srv"
  "srv/SpiderGoal.srv"
  "srv/GetCorrectionOffset.srv"
  "srv/BreaksControl.srv"
  "srv/Messages.srv"
  "srv/GetOffsetsToChargingPosition.srv"
  "srv/SendStringCommand.srv"
)

rosidl_generate_interfaces(${PROJECT_NAME}
  ${msg_files}
  ${srv_files}
  DEPENDENCIES std_msgs
)

ament_export_dependencies(rosidl_default_runtime)

# ament_python_install_package(${PROJECT_NAME})

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
