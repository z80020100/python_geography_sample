#!/usr/bin/env python3

import utils


def main():
    # Sample coordinates
    lat1, lon1 = 34.96820120833333, 136.99216098333332
    lat2, lon2 = 34.968202855, 136.99216208666667

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


if __name__ == "__main__":
    main()
