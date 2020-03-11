from scenic.simulators.carla.map import setMapPath
setMapPath(__file__, 'Town01.xodr')
from scenic.simulators.carla.road_model import *

ego = Car
spot = OrientedPoint on visible curb  # NOTE: getting error 'curb' not a keyword
badAngle = Uniform(1.0, -1.0) * (10, 20) deg
Car left of spot by 0.5, facing badAngle relative to roadDirection
