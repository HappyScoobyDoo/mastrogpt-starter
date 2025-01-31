import sys 
sys.path.append("packages/reverse/reverse")
import reverse

def test_reverse():
    res = reverse.reverse({})
    assert res["output"] == "Try to reverse! This is a reverse provider!"
