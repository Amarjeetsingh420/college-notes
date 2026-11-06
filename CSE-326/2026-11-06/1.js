// object manupulation in js
let student = {
    name: "Aman",
    age:20,
    marks:80
}
//Display the object
console.log("original object: ", student)
// Access property
console.log("Name: ",student.name)
// add a new property
student.course = "BCA"
// update a property 
student.marks=95;
// Delete a property
delete student.age;
//display modified object
console.log(student)
//important manupulation method
