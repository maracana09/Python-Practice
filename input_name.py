applicant = raw_input("Enter the applicant's name: ")
interviewer = raw_input("Enter the interviewer's name: ")
time = raw_input("Enter the appointment time: ")
print(interviewer + ' will interview ' + applicant + ' at ' + time +'.')
print(interviewer, ' will interview ', applicant, ' at ', time, '.')
print('{} will interview {} at {}.'.format(interviewer, applicant, time))

name = "Andy"
print name[0]
print name[1]
print name[2]
print name[3]
for i in range(4):
    print name[i]
