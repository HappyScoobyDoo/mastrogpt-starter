import os, requests as req
def test_reverse():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/reverse/reverse"
    res = req.get(url).json()

    assert res.get("output") == "Try to reverse! This is a reverse provider!"
