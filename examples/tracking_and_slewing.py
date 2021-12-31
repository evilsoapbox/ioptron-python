import ioptron as iom
import ioptron.ioptron as iopt 

scope = iopt.ioptron('COM5')
# Get custom tracking rate
scope.get_custom_tracking_rate()
print("TRACKING: custom rate:: {}".format(scope.tracking_rate.custom))

# Get custom tracking rate
print("SLEWING: max speed:: {}".format(scope.get_max_slewing_speed()))

# Get altitude limit
scope.get_altitude_limit()
print("ALTITUDE: max limit:: {}".format(scope.altitude_limit))

# Get ra and dec guiding rates
scope.get_guiding_rate()
print("GUIDING RATE: RA:: {}".format(scope.guiding_rate.right_ascention))
print("GUIDING RATE: DEC:: {}".format(scope.guiding_rate.declination))

# Get the meredian treatment
scope.get_meredian_treatment()
print("MEREDIAN: code:: {}".format(scope.meredian.code))
print("MEREDIAN: description:: {}".format(scope.meredian.description))
print("MEREDIAN: degree limit:: {}".format(scope.meredian.degree_limit))