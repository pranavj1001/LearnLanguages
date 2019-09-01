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
// Below given example shows automatic derive(Debug) implementation
// and manual Display implementation.

// !!!--- start uncommenting from line below ---!!!
// Import (via `use`) the `fmt` module to make it available.
// use std::fmt::{self, Formatter, Display};
// #[derive(Debug)]
// struct Person<'a> {
//     name: &'a str,
//     age: u8
// }

// // Implement `Display` for `Person`.
// impl<'a> fmt::Display for Person<'a> {
//     fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
//         // Try `write!` to see if it errors. If it errors, return
//         // the error. Otherwise continue.
//         write!(f, "(Name is {} and Age is {})", self.name, self.age)?;
//         write!(f, "")
//     }
// }

// #[derive(Debug)]
// struct Color {
//     red: u8,
//     green: u8,
//     blue: u8,
// }

// impl Display for Color {
//     // `f` is a buffer, this method must write the formatted string into it
//     fn fmt(&self, f: &mut Formatter) -> fmt::Result {
//         // `write!` is like `format!`, but it will write the formatted string
//         // into a buffer (the first argument)
//         write!(f, "RGB ({}, {}, {}) 0x{:02.X}{:02.X}{:02.X}", 
//             self.red, self.green, self.blue, self.red, self.green, self.blue)
//     }
// }

// fn main() {
//     let name = "Peter";
//     let age = 27;
//     let peter = Person { name, age };

//     println!("Compare Person");
//     println!("Debug: Normal {:?}", peter);
//     println!("Debug: Pretty {:#?}", peter);
//     println!("Display: {}", peter);

//     for color in [
//         Color { red: 128, green: 255, blue: 90 },
//         Color { red: 0, green: 3, blue: 254 },
//         Color { red: 0, green: 0, blue: 0 },
//     ].iter() {
//         // Switch this to use {} once you've added an implementation
//         // for fmt::Display
//         println!("{:}", *color);
//     }
// }
// !!!--- end uncommenting from line above ---!!!
// ------------------ Debugging end ------------------

// Chapter 3
// ------------------ Primitives start ------------------
// Rust provides access to a wide variety of primitives.

// !!!--- start uncommenting from line below ---!!!
// use std::fmt;
// use std::mem;

// #[derive(Debug)]
// struct Matrix(f32, f32, f32, f32);

// impl fmt::Display for Matrix {
//     // `f` is a buffer, this method must write the formatted string into it
//     fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
//         write!(f, "( {} {} ) \n( {} {} )", self.0, self.1, self.2, self.3)
//     }
// }

// fn transpose(matrix: Matrix) -> Matrix {
//     Matrix(matrix.0, matrix.2, matrix.1, matrix.3)
// }

// // This function borrows a slice
// fn analyze_slice(slice: &[i32]) {
//     println!("first element of the slice: {}", slice[0]);
//     println!("the slice has {} elements", slice.len());
// }

// fn main() {
//     // Variables can be type annotated.
//     let logical: bool = true;

//     let a_float: f64 = 1.0;  // Regular annotation
//     let an_integer   = 5i32; // Suffix annotation

//     // Or a default will be used.
//     let default_float   = 3.0; // `f64`
//     let default_integer = 7;   // `i32`
    
//     // A type can also be inferred from context 
//     let mut inferred_type = 12; // Type i64 is inferred from another line
//     inferred_type = 4294967296i64;
    
//     // A mutable variable's value can be changed.
//     let mut mutable = 12; // Mutable `i32`
//     mutable = 21;
    
//     // Error! The type of a variable can't be changed.
//     //mutable = true;
    
//     // Variables can be overwritten with shadowing.
//     let mutable = true;

//     // Integer addition
//     // We need to tell the compiler the type of the literals we use.
//     println!("1 + 2 = {}", 1u32 + 2);

//     // Integer subtraction
//     // We need to tell the compiler the type of the literals we use.
//     println!("1 - 2 = {}", 1i32 - 2);

//     // Short-circuiting boolean logic
//     println!("true AND false is {}", true && false);
//     println!("true OR false is {}", true || false);
//     println!("NOT true is {}", !true);

//     // Bitwise operations
//     println!("0011 AND 0101 is {:04b}", 0b0011u32 & 0b0101);
//     println!("0011 OR 0101 is {:04b}", 0b0011u32 | 0b0101);
//     println!("0011 XOR 0101 is {:04b}", 0b0011u32 ^ 0b0101);
//     println!("1 << 5 is {}", 1u32 << 5);
//     println!("0x80 >> 2 is 0x{:x}", 0x80u32 >> 2);

//     // Use underscores to improve readability!
//     println!("One million is written as {}", 1_000_000u32);

//     // A tuple with a bunch of different types
//     let long_tuple = (1u8, 2u16, 3u32, 4u64,
//                       -1i8, -2i16, -3i32, -4i64,
//                       0.1f32, 0.2f64,
//                       'a', true);

//     // Values can be extracted from the tuple using tuple indexing
//     println!("long tuple first value: {}", long_tuple.0);
//     println!("long tuple second value: {}", long_tuple.1);

//     // Tuples can be tuple members
//     let tuple_of_tuples = ((1u8, 2u16, 2u32), (4u64, -1i8), -2i16);

//     // Tuples are printable
//     println!("tuple of tuples: {:?}", tuple_of_tuples);
    
//     // But long Tuples cannot be printed
//     // let too_long_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13);
//     // println!("too long tuple: {:?}", too_long_tuple);
//     // TODO ^ Uncomment the above 2 lines to see the compiler error

//     // To create one element tuples, the comma is required to tell them apart
//     // from a literal surrounded by parentheses
//     println!("one element tuple: {:?}", (5u32,));
//     println!("just an integer: {:?}", (5u32));

//     //tuples can be destructured to create bindings
//     let tuple = (1, "hello", 4.5, true);

//     let (a, b, c, d) = tuple;
//     println!("{:?}, {:?}, {:?}, {:?}", a, b, c, d);

//     let matrix = Matrix(1.1, 1.2, 2.1, 2.2);
//     println!("{:?}", matrix);
//     println!("{}", matrix);
//     println!("{}", transpose(matrix));

//     // Fixed-size array (type signature is superfluous)
//     let xs: [i32; 5] = [1, 2, 3, 4, 5];

//     // All elements can be initialized to the same value
//     let ys: [i32; 500] = [0; 500];

//     // Indexing starts at 0
//     println!("first element of the array: {}", xs[0]);
//     println!("second element of the array: {}", xs[1]);

//     // `len` returns the size of the array
//     println!("array size: {}", ys.len());

//     // Arrays are stack allocated
//     println!("array occupies {} bytes", mem::size_of_val(&ys));

//     // Arrays can be automatically borrowed as slices
//     println!("borrow the whole array as a slice");
//     analyze_slice(&xs);

//     // Slices can point to a section of an array
//     println!("borrow a section of the array as a slice");
//     analyze_slice(&ys[1 .. 4]);

//     // Out of bound indexing causes compile error
//     // println!("{}", xs[5]);
// }
// !!!--- end uncommenting from line above ---!!!
// ------------------ Primitives end ------------------

// Chapter 4
// ------------------ Custom Types start ------------------
// Rust custom data types are formed mainly through the two keywords:

// struct: define a structure
// enum: define an enumeration
// Constants can also be created via the const and static keywords.

// !!!--- start uncommenting from line below ---!!!

// !!!--- end uncommenting from line above ---!!!

// ------------------ Custom Types end --------------------