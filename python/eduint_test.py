from eduint import EduInt

v = 2
ei = EduInt(v)

print "TEST START " + str(ei)
print "TEST[1] 2 = " + str((v ** 1) % 3) + " = " + str(ei.powm(1, 3))
print "TEST[2] 4 = " + str((v ** 2) % 10) + " = " + str(ei.powm(2, 10))
print "TEST[3] 8 = " + str((v ** 3) % 10) + " = " + str(ei.powm(3, 10))
print "TEST[3] 0 = " + str((v ** 3) % 8) + " = " + str(ei.powm(3, 8))
print "TEST FINISH"

v = -1
ei = EduInt(v)

print "TEST START " + str(ei)
print "TEST[1] 2 = " + str((v ** 1) % 3) + " = " + str(ei.powm(1, 3))
print "TEST[2] 1 = " + str((v ** 2) % 10) + " = " + str(ei.powm(2, 10))
print "TEST[3] 9 = " + str((v ** 3) % 10) + " = " + str(ei.powm(3, 10))
print "TEST[3] 7 = " + str((v ** 3) % 8) + " = " + str(ei.powm(3, 8))
print "TEST FINISH"