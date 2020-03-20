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

	print(f'Simulating map {map_.name}')

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
	vid = vehicle.id

	for step in range(10):
		world_snapshot = world.wait_for_tick()
		print('\n', world_snapshot.timestamp)
		print(f'Number of Actors: {len(world_snapshot)}')
		for actor_snapshot in world_snapshot:
			if actor_snapshot.id == vid:
				print(actor_snapshot.get_transform())
				print(actor_snapshot.get_velocity())
				print(actor_snapshot.get_angular_velocity())
				print(actor_snapshot.get_acceleration())
		print(vehicle.get_transform())  # transform received from last tick

if __name__ == '__main__':
	main()
	