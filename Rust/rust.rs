fn main() {

    // ------------------ print macros start ------------------
    // Macros: Macros look like functions, except that their name ends with a bang !, 
    // but instead of generating a function call, macros are expanded into source code 
    // that gets compiled with the rest of the program. eg. println!
    // println! -> prints statement to console in a new line

    println!("April has {} days.", 31);
    println!("{month} has {numberOfDays} days.", 
        month = "January",
        numberOfDays = "31");
    // Special formating is used here
    // {:b} -> converts 2 to 10 (binary form)
    println!("{} of {:b} people know binary, the other half doesn't", 1, 2);
    let width = 6;
    println!("{number:>width$} {spaces} spaces and {number}", number = 1, width = width, spaces = width - 1);
    println!("{}", format!("{:05}", 12));

    // rounds off the number
    let pi = 3.141592;
    println!("Pi is roughly {:.3}", pi);
    // ------------------ print macros end ------------------

}