#g_sandbox
from common import *
gc = gspread.login('gluefish@gmail.com','G0ldenFr0nd')
wks = gc.open('Jeld-Wen Canada')
global ws
ws = wks.worksheet('Suite')
global base_url
results_to = gsfind(ws, "Results To:", "Steps")
first_setup = ws.find("SETUP").row + 1
last_setup = ws.find("TESTS").row -1
first_test = ws.find("TESTS").row + 1
last_test = ws.find("TEARDOWN").row
first_teardown = ws.find("TEARDOWN").row + 1
last_teardown = ws.row_count + 1
import time

#print the time stamp to the output and to the sheet
dt = datetime.date.today()
tm = time.strftime("%H:%M:%S")
dttm = str(dt)+" "+str(tm)
print dttm
ws.update_cell(ws.find("Last Test:").row, ws.find("Steps").col, dttm)

#clear out the results column
for n in range(first_test,last_teardown):
    ws.update_cell(n, 6, '')
    
suite_name = "Suite " + gsfind(ws, "Suite Name:", "Steps")

print '###############################################'
print '#       ' + suite_name
print '###############################################'
print ''

#looping through the tests in the suite
tlist = []
global a
for a in range (first_test,last_test):
    if(ws.cell(a,2).value == 'Y'):
        tested = False
        ta=""+str(a)+",6'"
        tlist.extend([ta])
        ws.update_cell(a,6,'Testing')
        
#tracking the test result location on the suite sheet
        tname = ws.cell(a,1).value
        tcmd = "test_" + tname
        print ""
        print "************"
        print "SETUP"
        print "************"
        
#looping through the setup        
        for s in range (first_setup, last_setup):
            print ws.cell(s, 1).value + " " + ws.cell(s,4).value
            cmdexec = ws.cell(s, 5).value
            exec(cmdexec)
        tst = ws.cell(a, 4).value
        tstsht = "ts = wks.worksheet('" + tname + "')"
        exec(tstsht)
        #print "Test Worksheet: " + ts.title
        
        print ""
        print "************"
        print "TEST " + tcmd + ": " + tst
        print "************"
        
#looping through the tests        
        for tstep in range(2, ts.row_count + 1):
            print ts.cell(tstep, 1).value + " " + ts.cell(tstep, 4).value
            tcmd = ts.cell(tstep, 5).value
            if tcmd != "":
                tested = True
                try:
                    exec(tcmd)
                except:
                    print "Step failed"
                    ws.update_cell(a,6,'FAIL')
                    #fail_text = ts.cell(tstep,1).value + ": " + ts.cell(tstep,4).value
                    #ws.update_cell(a,5, fail_text)
        print ""
        print "************"
        print "TEARDOWN"
        print "************"
        print ""
        
#writing result back to the sheet
        if tested:
            if (ws.cell(a,6).value != 'FAIL'):
                ws.update_cell(a,6,'PASS')
        else:
            ws.update_cell(a,6,'ok')
                
#looping through the teardown        
        for t in range(first_teardown, last_teardown):
            print ws.cell(t, 1).value + " " + ws.cell(t, 4).value
            cmdexec = ws.cell(t,5).value
            exec(cmdexec)

xyzzy()

def is_in(obj, string):
    try:
        assert string in obj
        print '...PASS'
    except:
        print '...FAIL'
        ws.update_cell(a,6,'FAIL')

def xyzzy():
    print "plugh"