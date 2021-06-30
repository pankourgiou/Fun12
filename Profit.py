def profit(p1,p2,c1):
    if p1 > p2:
        profits = 0
    elif p1 == p2:
        profits = 0.5*total_demand(p1)*(p1-c1)
    else:
        profits = total_demand(p1)*(p1-c1)
    return profits

def reaction(p2,c1):
    if p2 > c1:
        reaction = c1+10*(p2-c1)
    else:
        reaction = c1
    return reaction
