from datetime import datetime
import pytz

# Get current time in UTC
utc_now = datetime.now(pytz.utc)

# Convert UTC to EST
est_timezone = pytz.timezone('US/Eastern')
est_now = utc_now.astimezone(est_timezone)

# Print the results
print('\n')

print("Current time in EST:", est_now.strftime('%Y-%m-%d %H:%M:%S %Z'))

print('\n')

print("Current time in UTC:", utc_now.strftime('%Y-%m-%d %H:%M:%S %Z'))

print('\n')