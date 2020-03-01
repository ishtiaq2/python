from my_module import Student

std_1 = Student('Abbas', '2')
std_1.add_marks(100)
std_1.add_marks(50)
print std_1
print 'Total Student: {}'.format(Student.student().get_total_stds())

print '\n\n################################'
print '######### adding one more std ##'
print '################################\n'

std_2 = Student('Waqas', '2')
std_2.add_marks(200)
std_2.add_marks(150)
print std_2
print 'Total Student: {}'.format(Student.student().get_total_stds())

print '\n######################################'
print '######### adding one more std ends####'
print '######################################'