def decompose(link:str) -> tuple[str, str, str]:
    prevalue = ""
    midvalue = link
    postvalue = ""
    if "/" in link:
        prevalue = midvalue[:len(link) - midvalue[-1::-1].index("/")]
        midvalue = midvalue[len(link) - midvalue[-1::-1].index("/"):]
    if "." in link:
        postvalue = midvalue[midvalue.index("."):]
        midvalue = midvalue[:midvalue.index(".")]
    return prevalue, midvalue, postvalue