import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int arraySize = scanner.nextInt();
        int calcCount = scanner.nextInt();
        int array[] = new int[arraySize];
        int sumArray[] = new int[arraySize+1];
        int calcArray[] = new int[calcCount];
        for (int i = 0; i < arraySize; i++)
            array[i] = scanner.nextInt();
        for(int i = 0; i <= arraySize; i++){
            if(i == 0)
                sumArray[i] = 0;
            else if(i == 1)
                sumArray[i] = array[i-1];
            else
                sumArray[i] = sumArray[i-1] + array[i-1];
        }
        for(int i = 0; i < calcCount; i++){
            int startSum = scanner.nextInt();
            int endSum = scanner.nextInt();
            if(startSum >= 1 && endSum >= 1)
                calcArray[i] = sumArray[endSum] - sumArray[startSum-1];
        }
        for(int i = 0; i < calcCount; i++){
            System.out.println(calcArray[i]);
        }


    }

}
