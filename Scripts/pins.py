# take in the number
n = input()

# calculate answer
def find_pos(pin_frame):
    star_pos = []
    for i in range(len(pin_frame)):
        if pin_frame[i] == "*":
            star_pos.append(i)
    return star_pos

def brute_single(pos, pin_frame):
    def _isAdj(i):
        length = len(pin_frame)
        front_i = pos + 1
        back_i = pos - 1
        if front_i < len(pin_frame):
            if i == pin_frame[pos+1]:
                return True
        if back_i >= 0:
            if i == pin_frame[pos-1]:
                return True
        return False
    pins = []
    _pin = list(pin_frame)
    for i in range(10):
        if _isAdj(str(i)):
            continue
        _pin[pos] = str(i)
        pins.append("".join(_pin))
    return pins

pins = [n]
pos = find_pos(n)
for p in pos:
    tmp_pins = []
    for pin in pins:
        tmp_pins += brute_single(p, pin)
    pins = tmp_pins 
for p in pins:
    print(p)
