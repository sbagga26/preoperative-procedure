#!/usr/bin/python2

print("content-type: text/html")
print("\n")

import cgi
form=cgi.FieldStorage()
sg=form.getvalue('sg')
age=form.getvalue('age')
diabetes=form.getvalue('diabetes')
hypertension=form.getvalue('hypertension')
thyroid=form.getvalue('thyroid')
asthma=form.getvalue('asthma')
copd=form.getvalue('copd')
meds=form.getvalue('meds')
asa=form.getvalue('asa')
reg=form.getvalue('reg')
print(age)
fh=open('/etc/variables.py',"w+")
fh.write("#!/usr/bin/python2\n\nsg={}\nage={}\ndiabetes={}\nhypertension={}\nthyroid={}\nasthma={}\ncopd={}\nmeds={}\nasa={}\nreg={}\n".format(sg,age,diabetes,hypertension,thyroid,asthma,copd,meds,asa,reg))
fh.close()
