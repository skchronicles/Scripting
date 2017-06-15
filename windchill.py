# Skyler Kuhn
# Creates a windchill table from a pre-determined range of temperatures and wind velocities
filename = "windchill_output.txt"
with open(filename,"w") as wind:
    wind.write("\t5\t10\t15\t20\t25\t30\t35\t40\t45\t50")
    for t in range(-20,81,10):
        wind.write("\n{}   \t".format(t))
        for v in range(5,51,5):
            windChill = round(35.74 + (0.6215*t) - (35.75 * (v**0.16)) + (0.4275*t*(v**0.16)),2)
            wind.write("{} \t".format(windChill))
        wind.write("\n".format())
wind.close()
