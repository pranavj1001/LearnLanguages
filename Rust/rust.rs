// Chapter 1
// ------------------ print macros start ------------------
// Macros: Macros look like functions, except that their name ends with a bang !, 
// but instead of generating a function call, macros are expanded into source code 
// that gets compiled with the rest of the program. eg. println!
// println! -> prints statement to console in a new line

// !!!--- start uncommenting from line below ---!!!
// fn main() {
//     println!("April has {} days.", 31);
//     println!("{month} has {numberOfDays} days.", 
//         month = "January",
//         numberOfDays = "31");
//     // Special formating is used here
//     // {:b} -> converts 2 to 10 (binary form)
//     println!("{} of {:b} people know binary, the other half doesn't", 1, 2);
//     let width = 6;
//     println!("{number:>width$} {spaces} spaces and {number}", number = 1, width = width, spaces = width - 1);
//     println!("{}", format!("{:05}", 12));

//     // rounds off the number
//     let pi = 3.141592;
//     println!("Pi is roughly {:.3}", pi);
// }
// !!!--- end uncommenting from line above ---!!!
// ------------------ print macros end ------------------

// Chapter 2
// ------------------ Debugging start ------------------
// In JS we use console.log() for logging and debugging purposes. 
// console.log() can be used to print pretty any type of object.
// However, in Rust this is not possible as all types which want to use 
// std::fmt formatting traits require an implementation to be printable. 
// The fmt::Debug trait makes this very straightforward. 
// All types can derive (automatically create) the fmt::Debug implementation. 
// This is not true for fmt::Display which must be manually implemented.

// !!!--- start uncommenting from line below ---!!!
#[derive(Debug)]
struct Person<'a> {
    name: &'a str,
    age: u8
}
fn main() {
    let name = "Peter";
    let age = 27;
    let peter = Person { name, age };

    // Pretty print
    println!("{:#?}", peter);
}
// !!!--- end uncommenting from line above ---!!!
// ------------------ Debugging end ------------------