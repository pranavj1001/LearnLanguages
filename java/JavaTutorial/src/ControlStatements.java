public class ControlStatements {
    public static void main(String args[]){
        /*
        * if-else-if statement
        * The `if` statements are executed from the top down.
        * As soon as one of the conditions controlling the `if` is true, the statement associated with that `if` is executed, and the rest of
        the ladder i.e `else if` statement  is bypassed.
        *If none of the conditions is true, then the final `else` statement will be executed.
        * The final `else` acts as a default condition; that is, if all other conditional tests fail, then the last else statement is performed.
        *If there is no final `else` and all other conditions
        are false, then no action will take place.
        * */
        int month = 4;
        String season;
        if(month == 12 || month == 1 || month == 2) {
            season = "Winter";
        }
        else if(month == 3 || month == 4 || month == 5) {
            season = "Spring";
        }
        else if(month == 6 || month == 7 || month == 8) {
            season = "Summer";
        }
        else if(month == 9 || month == 10 || month == 11) {
            season = "Autumn";
        }
        else {
            season = "Bogus Month";
        }
        System.out.println("April is in the " + season + ".");


        /*
        * Switch statement
        * The `switch` statement is Java’s multiway branch statement. It provides an easy way to
        dispatch execution to different parts of your code based on the value of an expression. */
        /*The `switch` statement works like this: The value of the expression is compared with each of
        the values in the `case` statements. If a match is found, the code sequence following that `case`
        statement is executed. If none of the constants matches the value of the expression, then the
        `default` statement is executed. However, the `default` statement is optional. If no `case` matches
        and no `default` is present, then no further action is taken.
        The break statement is used inside the switch to terminate a statement sequence. When a
        `break` statement is encountered, execution branches to the first line of code that follows the
        entire `switch` statement. This has the effect of “jumping out” of the switch.
        Note :Value specified with case should be unique i.e no two case should have same value
        */
        /*for loop
         * for loop consist of initialization ,test-condition ,iteration
         * initialization is done at start of for-loop and it is done once. Generally, this is an expression that sets the value of the loop control variable,
which acts as a counter that controls the loop.
         * test-condition it has some boolean value true or false
         * if test-condition is true than group of statement is executed
         * iteration  this is usually an expression that increments or decrements the loop control variable
         */
         /* flow of for-loop
         * initialization
         * than check condition if its true than group of statement is executed else terminate loop
         * iterate loop variable ,than again check condition  than iteration and soon*/
        for(int i=0; i<6; i++) {
            switch (i) {
                case 0:
                    System.out.println("i is zero.");
                    break;
                case 1:
                    System.out.println("i is one.");
                    break;
                case 2:
                    System.out.println("i is two.");
                    break;
                case 3:
                    System.out.println("i is three.");
                    break;
                default:
                    System.out.println("i is greater than 3.");
            }
        }
    }
}
