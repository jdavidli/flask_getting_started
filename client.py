import requests
import json

def test():
    """Returns response of each of the APIs written for the previous miniproject
    """

    r = requests.get("http://vcm-3476.vm.duke.edu:5000/name")
    print(r.text)
    r2 = requests.get("http://vcm-3476.vm.duke.edu:5000/hello/David")
    print(r2.text)
    r3 = requests.post("http://vcm-3476.vm.duke.edu:5000/distance", json={"a": [0, 5], "b": [0, 10]})
    dist = r3.json()
    print(json.dumps(dist))


if __name__ == '__main__':
    test()
