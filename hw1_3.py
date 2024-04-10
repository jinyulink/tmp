def hw1_3():
    output = ""
    #-------------------------------
    output = "\n==\n".join("\n".join(f"{i} * {j} = {i*j}" for j in range(2, 10)) for i in range(2, 10)) + '\n'
    #-------------------------------
    return output