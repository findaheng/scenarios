import carla

def prologue():
	settings = world.get_settings()
	settings.synchronous_mode = True
	world.apply_settings(settings)

def extract_ground_truths(objects=[], numTimesteps=100):
	''' Extracts ground truths at each timestep of Carla'''

	f