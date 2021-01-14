#!/usr/bin/env python3
# Generate using ft8_lib : https://github.com/kgoba/ft8_lib

message="3140652320652537530266365644000014103140652300564763703632706435672612273140652"

# use https://github.com/louisabraham/beep on macos

import random
base_freq = 1400 + random.randrange(200, 2500)

tone_spacing = 6.25
keying_rate = 6.25
duration = 1/keying_rate

print("#!/bin/sh")
print("play -q -n ", end='')
synths = []
for code in message:
    tone = int(code)
    freq = base_freq + (tone * tone_spacing)
    synths.append("synth {duration} sine {freq}".format(duration = duration, freq = freq))
print(" : ".join(synths))
