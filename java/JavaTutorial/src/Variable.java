public class Variable {

    public static void main(String args[]){
        //declaring Variable a,b of integer type
        //integer size 4 bytes
        int a,b;
        b=20;

        //declaring Variable f1,f2 of floating point type
        //float size 4 bytes
        float f1,f2;
        f1 = 5;
        f2 = 2;

        //long size 8 bytes
        long ll;
        ll=150;

        //type cast long is converted into int
        a=(int)ll;
        float f3;
        f3=f1/f2;

        //in java '+' is used for concatenation
        System.out.println("a = "+a+" b = "+b);

        System.out.println("f1 = "+f1+" f2 = "+f2+" f3 = "+f3);

        //type cast
        System.out.println("f3 = "+f3+"\ntype cast f3 = "+(int)f3);

        //boolean variable can be assigned to true or false
        boolean c=true;
        System.out.println("c = "+c);
    }
}
