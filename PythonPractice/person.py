class Person:
    def __init__(self, name, age):
        self.name = name;
        self.age = age;

    def is_adult(self):
        return self.age >= 18;
    
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old.";

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id;

    def get_student_id(self):
        return self.student_id,self.name,self.age;

person1 = Person("Ivan", 25);
person2 = Person("Maria", 16);

student1 = Student("Georgi", 20, "S12345");
student2 = Student("Elena", 22, "S67890");

if __name__ == "__main__":
    print(person1.is_adult());
    print(person2.is_adult());

    print(person1.greet());
    print(person2.greet());
    print(student1.get_student_id());
    print(student2.get_student_id());