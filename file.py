# Python 3 code to demonstrate
# working of assert
# Application

# initializing list of foods temperatures
batch = [ 40, 26, 39, 30, 25, 21]

# initializing cut temperature
cut = 40

# using assert to check for temperature greater than cut
for i in batch:
	assert i >= cut, "Batch is Rejected"
	print (str(i) + " is O.K" )
