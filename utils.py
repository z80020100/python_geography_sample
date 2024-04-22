# https://geographiclib.sourceforge.io/html/python/code.html
from geographiclib.geodesic import Geodesic


def cal_great_circle_distance_m(lat1, lon1, lat2, lon2):
    geo_dict = Geodesic.WGS84.Inverse(
        lat1, lon1, lat2, lon2, Geodesic.DISTANCE)
    return geo_dict['s12']
