#!/usr/bin/env python3

import utils


def main():
    # Sample coordinates
    lat1, lon1 = 34.96820120833333, 136.99216098333332
    lat2, lon2 = 34.968202855, 136.99216208666667
    print(f"Start point: ({lat1}, {lon1})")
    print(f"End point: ({lat2}, {lon2})")

    # Calculate distance
    distance_m = utils.cal_great_circle_distance_m(lat1, lon1, lat2, lon2)
    print(f"Distance: {distance_m} meters")

    # Calculate azimuth
    azimuth = utils.cal_azimuth(lat1, lon1, lat2, lon2)
    print(f"Azimuth: {azimuth} degrees")

    # Calculate bounding box vertices
    bounding_box_length_m = 4
    vertices = utils.cal_bounding_box_vertices(
        lat1, lon1, bounding_box_length_m, azimuth)
    print("Bounding box vertices:")
    for i, vertex in enumerate(vertices):
        print(f"  Vertex {i+1}: {vertex}")

    # Check if a point is inside the polygon
    inside_test_point = 34.96820584615509, 136.99218306145594
    outside_test_point = 34.96823584615509, 136.99220306145594
    if utils.is_point_inside_polygon(vertices, inside_test_point[0], inside_test_point[1]):
        print(
            f"Inside test point {inside_test_point} is inside the bounding box")
    else:
        raise Exception(
            f"Inside test point {inside_test_point} is outside the bounding box")

    if utils.is_point_inside_polygon(vertices, outside_test_point[0], outside_test_point[1]):
        raise Exception(
            f"Outside test point {outside_test_point} is inside the bounding box")
    else:
        print(
            f"Outside test point {outside_test_point} is outside the bounding box")


if __name__ == "__main__":
    main()
