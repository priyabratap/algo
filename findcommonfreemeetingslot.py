# //Find the common free slot for the employees

def parseSlot(list_of_slots):
    # print("list_of_slots",list_of_slots)
    result = []
    for j in range(0,len(list_of_slots)):
        start_time = int(list_of_slots[j].split("-")[0])
        end_time = int(list_of_slots[j].split("-")[1])
        k = 0
        # print("start_time-end_time",start_time,end_time)
        while (start_time + k) < end_time:
            result.append(str(start_time+k) + "-" + str(start_time+k+1))
            k += 1
        # print("result",result)
    return result
    
e_1 = ["1-3"] # // can have more slots in this way for e_1 = ["1-3", "5-6"]
e_2 = ["2-4"]
e_3 = ["6-8"]
e_4 = ["9-12"]
allemp = [e_1, e_2, e_3, e_4]
print("allemp",allemp)

allTimeSlots = []
for j in range(1,12): # //can change 0,24 for 24 hours, I mean more slots
    allTimeSlots.append(str(j) + "-" + str(j+1))
print("allTimeSlots",allTimeSlots)

commonFreeSlots = []
for j in range(0,len(allTimeSlots)):
    timeSlotOk = True
    # print("-----j-----",j,"allemp",len(allemp))
    for k in range(0,len(allemp)):
        person_occ_slots = parseSlot(allemp[k])
        # print("k",k,"person_occ_slots",person_occ_slots)
        if allTimeSlots[j]  in person_occ_slots:
            timeSlotOk = False
            break
    if timeSlotOk:
        commonFreeSlots.append(allTimeSlots[j])

print("commonFreeSlots",commonFreeSlots)


# // output
# // allemp [['1-3'], ['2-4'], ['6-8'], ['9-12']]
# // allTimeSlots ['1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-8', '8-9', '9-10', '10-11', '11-12']
# // commonFreeSlots ['4-5', '5-6', '8-9']
