# get number of tower visibility from left to right
def getNoTowerVisbility(imap):
    counter = 1
    imap_v = imap.values()
    imap_len = len(imap)
    max_so_far = "t"+str(imap_len) # last key of map
    omap = {"t"+str(imap_len):0} # put last key of map with value 0

    # loop the map backward
    for i in range(imap_len-1,0,-1):
        # preparing index to access map directly
        cidx = "t"+str(i)
        nidx = "t"+str(i+1)
        # print("imap[cidx] > imap[nidx]",imap[cidx],imap[nidx],"index:",cidx,nidx)
        if imap[cidx] > imap[nidx]:
            if imap[cidx] > imap[max_so_far]:
                omap[cidx] = counter + omap[max_so_far]
                max_so_far = cidx
                counter = 1
            else:
                omap[cidx] = counter - 1
                counter += 1
        else:
            omap[cidx] = 0
            counter += 1
        # print("max_so_far:",max_so_far,"counter:",counter)

    return omap

    
# {"towername":"number of floor"}
# imap={"t1":18,"t2":10,"t3":8,"t4":2,"t5":15,"t6":2,"t7":6,"t8":11}
imap={"t1":18,"t2":10,"t3":8,"t4":2,"t5":15,"t6":2,"t7":6,"t8":11,"t9":2,"t10":6,"t11":2}
print(imap)
print("omap",getNoTowerVisbility(imap))
