from scenic.simulators.carla.map import setMapPath
setMapPath(__file__, 'OpenDrive/Town01.xodr')
from scenic.simulators.carla.road_model import *

wiggle = (-10 deg, 10 deg)
ego = Car with roadDeviation wiggle
Car visible, with roadDeviation resample(wiggle)
Car visible, with roadDeviation resample(wiggle)
