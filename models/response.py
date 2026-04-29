def build_response(result):

    sizes = result.get("sizes", [])

    if len(sizes) > 0:
        avg = sum(sizes) / len(sizes)
        mx = max(sizes)
        mn = min(sizes)
    else:
        avg = mx = mn = 0

    return {
        "fragmentos": result["count"],
        "promedio": int(avg),
        "maximo": int(mx),
        "minimo": int(mn),
        "density": result.get("density"),
        "min_area": result.get("min_area"),
        "dist_ratio": result.get("dist_ratio"),
        "morph_iter": result.get("morph_iter")
    }