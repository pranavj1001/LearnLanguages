/*'class' is keyword, its used to declare that new class is being defined.
Here 'HelloWorld' is an identifier that is name of class
*/
class HelloWorld {
    //program begins with call to main()
    //public is access modifier,which allows the programmer to control the visibility of class member.
    //class member are all function and all variable declared and defined in class.
    /*
    When class member is preceded by   public  ,
    then that member may be access by code outside the class in which it is declared.
    */
    //static allows main() to be called without instantiate a particular instance of class i.e object of class.
    //void implies that main() does not return any value.
    //String args[] is used to store information that is available while executing program
    public static void main(String args[]){
        /*System is a class in the java.lang package.
        out is a static member of the System class, and is an instance of java.io.PrintStream .
        println is a method of java.io.PrintStream
        */
        System.out.println("Hello World");
    }
}
