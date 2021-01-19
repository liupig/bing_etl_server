import geohash2


def geo_decode(code):
    """

    :param code:
    :return:
    """
    try:
        result = geohash2.decode(code)
        return {"lat": float(result[0]), "lon": float(result[1])}
    except:
        return {}


def geo_encode(latitude_and_longitude):
    """

    :param latitude:
    :param longitude:
    :return:
    """
    return geohash2.encode(latitude_and_longitude["lat"], latitude_and_longitude["lon"])
