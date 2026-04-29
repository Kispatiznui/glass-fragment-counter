def build_response(result):

    sizes = result["sizes"]

    if len(sizes) > 0:
        avg = sum(sizes) / len(sizes)
        mx = max(sizes)
        mn = min(sizes)
    else:
        avg = mx = mn = 0

    return {
        "fragmentos": result["count"],
        "promedio": avg,
        "maximo": mx,
        "minimo": mn
    }
