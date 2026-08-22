"""Reference solution for assigning and reassigning basic variables."""

# The same name can be assigned a new value later.
station_name = "Assembly station"
station_name = "Quality control station"

sample_count = 24
motor_temperature_celsius = 42.5
status_message = "Ready"
emergency_stop_active = False

# type() reveals the type of the value currently stored in a variable.
sample_count_type = type(sample_count)
motor_temperature_type = type(motor_temperature_celsius)
status_message_type = type(status_message)
emergency_stop_type = type(emergency_stop_active)

# Multiple assignment can set two variables in one readable statement.
left_sensor_state, right_sensor_state = "blocked", "clear"
left_sensor_state, right_sensor_state = right_sensor_state, left_sensor_state

# Uppercase names are the Python convention for values that should stay fixed.
MAX_MOTOR_SPEED_RPM = 3000
