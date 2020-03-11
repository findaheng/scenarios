from scenic.simulators.carla.map import setMapPath
setMapPath(__file__, 'OpenDrive/Town01.xodr')
from scenic.simulators.carla.road_model import *

ego = Car
spot = OrientedPoint on visible curb
badAngle = Uniform(1.0, -1.0) * (10, 20) deg
Car left on spot by 0.5, facing badAngle relative to roadDirection

# NOTE: might need to adjust spot according to map -- currently based on code in Scenic paper
