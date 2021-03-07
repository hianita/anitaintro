def avg(data):
    nums=0
    salarySum=0
    salaryAvg=0
    list=data['employees']
    for i in range(0,int(data['count'])):
        nums=nums+1
    
    for j in range(0,nums):
        person=(list[j])
        personSalary=person['salary']
        salarySum+=personSalary
        j+=1
    
    salaryAvg=salarySum/nums
    print('Average Salary: '+str(salaryAvg))
    
avg({
"count":3,
"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
}
]
})