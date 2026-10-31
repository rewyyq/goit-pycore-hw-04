def get_cats_info(path: str) -> list:
    try:
        with open(path, "r") as f:
            res = []
            for line in f:
                line = line.strip().split(',')
                res.append({"id": line[0], "name": line[1], "age": line[2]})
            return res
    except (FileNotFoundError, IndexError):
        return []