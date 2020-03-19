#!/usr/bin/env python

import carla
import random

HOST = 'localhost'
PORT = 2000

def main():

	# Initialize CARLA client
	client = carla.Client(HOST, PORT)
	client.set_timeout(2.0)

	# Retrieve world, map, and blueprint library
	world = client.get_world()
	map_ = world.get_map()
	blueprint_library = world.get_blueprint_library()

	# Set to asynchronous with a fixed timestep
	settings = world.get_settings()
	settings.fixed_delta_seconds = 0.05
	settings.synchronous_mode = False
	world.apply_settings(settings)

	# Randomly spawn a vehicle
	bp = random.choice(blueprint_library.filter('vehicle'))
	if bp.has_attribute('color'):
		color = random.choice(bp.get_attribute('color').recommended_values)
		bp.set_attribute('color', color)
	transform = random.choice(map_.get_spawn_points())
	vehicle = world.spawn_actor(bp, transform)

	for step in range(10):
		print(f'\nTimestep: {step}\n')
		snapshot = world.wait_for_tick()
		print(snapshot)

if __name__ == '__main__':
	main()
	