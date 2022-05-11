import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int count = scanner.nextInt();

        BigInteger add = scanner.nextBigInteger();
        BigInteger array[] = new BigInteger[count];

        BigInteger calc = BigInteger.valueOf(1);
        BigInteger sum = BigInteger.valueOf(0);
        for(int i = 1; i < count; i++){
            calc = calc.multiply(BigInteger.valueOf(10));
        }
        for(int i = 0; i < count; i++){
            array[i] = add.divide(calc);
            if(calc.intValue() != 1)
                calc = calc.divide(BigInteger.valueOf(10));
            sum = sum.add(array[i].remainder(BigInteger.valueOf(10)));
        }

        System.out.print(sum);
    }
}
