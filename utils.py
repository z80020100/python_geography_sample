# https://geographiclib.sourceforge.io/html/python/code.html
from geographiclib.geodesic import Geodesic


def cal_great_circle_distance_m(lat1, lon1, lat2, lon2):
    geo_dict = Geodesic.WGS84.Inverse(
        lat1, lon1, lat2, lon2, Geodesic.DISTANCE)
    return geo_dict['s12']


def cal_azimuth(lat_start, lon_start, lat_end, lon_end):
    geo_dict = Geodesic.WGS84.Inverse(
        lat_start, lon_start, lat_end, lon_end, Geodesic.AZIMUTH)
    # azi1 represents the initial azimuth of the great circle track from point 1 to point 2
    # azi2 represents the final azimuth of the great circle track from point 1 to point 2
    return geo_dict['azi1']


def cal_bounding_box_vertices(lat, lon, length_m, azimuth):
    bearings = [
        (azimuth + 45) % 360,
        (azimuth + 135) % 360,
        (azimuth + 225) % 360,
        (azimuth + 315) % 360
    ]
    vertices = [
        Geodesic.WGS84.Direct(lat, lon, b, length_m,
                              Geodesic.LATITUDE | Geodesic.LONGITUDE)
        for b in bearings
    ]
    return [(v['lat2'], v['lon2']) for v in vertices]
