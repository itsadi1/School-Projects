namespace myprojects

open System

module password = 
    let mutable pass = false
    let mutable i = 0
    Console.WriteLine(Random().Next(10))
    while pass = false && i <> 3 do 

        i <- (i + 1)

        Console.Write("Enter password:")
        let password = Console.ReadLine()

        if password <> "p@ss1234" then

            Console.WriteLine("Acess Denied!")
            Console.WriteLine(pass)

        else

            Console.WriteLine("Access Authorised!")
            pass <- true

    if pass = false then
        Console.WriteLine("Acess Locked!")
