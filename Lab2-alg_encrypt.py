#   Nicolas Callier
#   CSCI - 102 Section H
#   Time: 45 mins

list_1 = input("LIST1> ")
final = list_1[-2:] + list_1[:-2]
print(final)
list_2 = input("LIST2> ")
final2 = list_2[0:len(list_2)-2]
print(final2)
list_3 = input("LIST3> ")
final3 = list_3[round(len(list_3)/2):len(list_3)]
print(final3)
list_4 = input("LIST4> ")
final4 = list_4[0:2] + list_4[4] + list_4[3] + list_4[2] + list_4[5:len(list_4)]
print(final4)
list_5 = input("LIST5> ")
print("The encrypted message is")
final5 = list_5[0:2] + (" ") + final + final2 + final3 + final4 + (" ") + list_5[2:4]
print("OUTPUT " + final5) 