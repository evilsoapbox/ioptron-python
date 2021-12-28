import ioptron.ioptron as iopt 

scope = iopt.ioptron('COM5')
print("Version #:  {}".format(scope.mount_version))

# Get the time(s)
scope.get_time_information()
print("Offset #:  {}".format(scope.time.utc_offset))
print("DST #:  {}".format(scope.time.dst))
print("J2000 #:  {}".format(scope.time.jd))
print("Unix #:  {}".format(scope.time.unix))
print("Formatted #:  {}".format(scope.time.formatted))

# Set the time(s)
scope.set_timezone_offset()
scope.set_daylight_savings(False)
scope.set_time()

# Get the time(s)
scope.get_time_information()
print("Offset #:  {}".format(scope.time.utc_offset))
print("DST #:  {}".format(scope.time.dst))
print("J2000 #:  {}".format(scope.time.jd))
print("Unix #:  {}".format(scope.time.unix))
print("Formatted #:  {}".format(scope.time.formatted))