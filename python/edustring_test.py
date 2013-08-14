from edustring import EduString

es = EduString("TEST STRING 1")
ts = str(es)

print "TEST START \"" 	+ ts + "\"; LEN : " 		+ str(len(ts))
print "TEST[1]: 0 = " 	+ str(ts.find("TEST")) 		+ " = " + str(es.simpleSearch("TEST"));
print "TEST[2]: 1 = " 	+ str(ts.find("EST")) 		+ " = " + str(es.simpleSearch("EST"));
print "TEST[3]: -1 = " 	+ str(ts.find("0EST")) 		+ " = " + str(es.simpleSearch("0TEST"));
print "TEST[4]: -1 = " 	+ str(ts.find("STRTEST")) 	+ " = " + str(es.simpleSearch("STRTEST"));
print "TEST[5]: 12 = " 	+ str(ts.find("1")) 		+ " = " + str(es.simpleSearch("1"));
print "TEST[5]: 0 = " 	+ str(ts.find("")) 			+ " = " + str(es.simpleSearch(""));
print "TEST FINISH"