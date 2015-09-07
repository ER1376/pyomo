def pysp_aggregategetter_callback(scenario_tree_manager,
                                  scenario_tree,
                                  scenario,
                                  data):

    data.setdefault('names',[]).append(scenario._name)
    print("aggregategetter callback1: "+str(scenario._name)+", "
          +str(data))
    print("")

    # **IMPT**: Must also return aggregate data in a singleton tuple
    #           to work with bundles
    return (data,)