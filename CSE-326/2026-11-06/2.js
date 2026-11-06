let employee ={
    name: "Rahul",
    age:30,
    salary:40000
};
console.log("employee details: ",employee)
//display keys
console.log("Keys: ", Object.keys(employee));
//Display values
console.log("values: ", Object.values(employee))
//disolay key-value pairs
console.log("Entries: ", Object.entries(employee))
//check properties
console.log("Has name: ",Object.hasOwn(employee,"name"));
// add properties
employee.department = "IT"
// update properties
employee.salary = 50000;
// delete properties
delete employee.age;
// final emmployee object
console.log(employee)