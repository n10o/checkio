def flatten(dictionary):
    stack = [((), dictionary)]
    result = {}
    while stack:
        path, current = stack.pop()
        for k, v in current.items():
            comppath = "/".join((path + (k,)))
            if isinstance(v, dict):
                stack.append((path + (k,), v))
                # Memo: dictが空の場合にelseに入って欲しいが、デフォルトだとdictと認識されて
                # else節に最後まで入らず、うまくいかない。
                # そのため、dictが空の場合にresultを別途返せば良い
                if not v:
                        result[comppath] = ""
            else:
                # Memo: tuple + tuple = fusion
                result[comppath] = v
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}
