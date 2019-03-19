def main():
    person={'name':'ayead','age':67, 'id':3242554353};
    print(person,type(person))
    print(person['name'])
    print(person['age'])
    print(person['id'])
    del person['name']
    print(person)
   ## person.clear()
    print(person)
    person['name']="ahmed"
    print(person)
   ## person.clear()
    student=dict(name='ebthal',id='3426')
    print(student)
    student['name','id']='arwa',3427
    print(student)
   ## student['name'] = "ahmeed"
    ##del student['name']
    print(student,type(student))
    unvirsty=dict(name='almarj',pro='libya')
    print(unvirsty,type(unvirsty))
    unvirsty['name']="fiesal king"
    print(unvirsty)
    unvirsty["pro"]='ksa'
    print(unvirsty,type(unvirsty))
    del unvirsty['name']
    print(unvirsty)
    unvirsty.clear()
    print(unvirsty)
    per=dict(name="ahmed")

    print(id(per))
    per['name']='mohmed'
   ## per=dict(name="mohmed")
    print(id(per))

    l={1,2,3,4,5,7}
    ##print(l)
    l[1:2]
    print(l)

if __name__ == '__main__':main()
