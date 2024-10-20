import math
a = 6378137.0
c = 6356752.314245
R = 6371000
e2 = 1 - (c**2 / a**2)
e = math.sqrt(e2)
S_ellipsoid = 2 * math.pi * a**2 * (1 + (1 - e2) / e * math.atanh(e))
S_sphere = 4 * math.pi * R**2
print(f"Площадь поверхности эллипсоида WGS-84: {S_ellipsoid:.2f} м^2")
print(f"Площадь поверхности сферы: {S_sphere:.2f} м^2")
