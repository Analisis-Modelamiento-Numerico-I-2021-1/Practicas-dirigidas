#!/usr/bin/julia

println(1e20 + 1 -1e20)

x = fill(0.1, 10)

println(x)

println(sum(x))

using Xsum

println(xsum(x))