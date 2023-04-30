def thai_area(rai, ngan, wa2):

    Asqwa = 400*rai + 100*ngan + wa2
    Asqm = 4*Asqwa

    return Asqm


if __name__ == '__main__':
    Asqm = thai_area(40, 3, 80)
    print('Total area = {} sq. m.'.format(Asqm))
