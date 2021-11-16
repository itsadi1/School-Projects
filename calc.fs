namespace myprojects

open System

module simple_calc = 

    Console.WriteLine("Fsharp Calculator\n")

    Console.Write("Enter first number: ")
    let a = int (Console.ReadLine())

    Console.Write("Enter second number: ")
    let b = int (Console.ReadLine())

    let add a b = printfn "\nAddition       :%i " (a + b)
    let sub a b = printfn "Subtraction    :%i " (a - b)
    let mul a b = printfn "Multiplication :%i " (a * b)
    let div a b = printfn "Division       :%f \n" (float a /float b)

    
    add a b
    sub a b
    mul a b
    div a b
