filename = "windchill_output.txt"
with open(filename,"w") as wind:
    wind.write("\t\t5\t\t10\t\t15\t\t20\t\t25\t\t30\t\t35\t\t40\t\t45\t\t50")
    for t in range(-20,81,10):
        wind.write("\n{}   \t".format(t))
        for v in range(5,51,5):
            windChill = round(35.74 + (0.6215*t) - (35.75 * (v**0.16)) + (0.4275*t*(v**0.16)),2)
            wind.write("{} \t".format(windChill))
        wind.write("\n".format())
wind.close()