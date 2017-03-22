def main():
    print ('enter the number of phibonacci ')
    a = input()
    if type(a) is not type(1):
        print "error"
        print type(a)
        return
    if a == 0:
        print 0
        return
    elif a == 1:
        print 1
        return
    print 0
    a_prev = 1
    a_next = 1
    print a_prev
    # print a_next
    counter = 2  # cause 3 numbers are already put
    for i in range(a):
        print a_prev
        counter += 1
        if counter > a:
            return
        a_next += a_prev
        counter += 1
        if counter > a:
            return
        print a_next
        a_prev += a_next
    return


main()
