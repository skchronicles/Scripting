
def files2dictionary(filename, countryID, supp_dict):
    """Creates a dictionary to hold all the information for each biological sex below.
        It has following structure
        {"Sex1_mdlt2450": 
          {"0":
               {"1":datavalue, "2":dataValue...}, 
           "2.5":
               {"1":datavalue, "2":dataValue...}
          }
         }
        -- where: [Sex#countryID][Age][ICDcode] = one_datapoint"""

    fh = open(filename)
    header = next(fh)

    data_dict = {}
    data_dict[countryID] = {}

    numlist = range(1, 36)
    agelist = []
    for line in fh:
        linelist = line.strip().split(",")
        age = linelist[4]
        agelist.append(age)
        for icdrep in numlist:
            if str(age) not in data_dict[countryID]:
                data_dict[countryID][str(age)] = {}
                data_dict[countryID][str(age)][str(icdrep)] = float(linelist[icdrep+8])
            else:
                data_dict[countryID][str(age)][str(icdrep)] = float(linelist[icdrep+8]) 
            
    fh.close()
    supp_dict.update(support_counter(header.split(","), agelist, supp_dict))
    return data_dict, supp_dict
