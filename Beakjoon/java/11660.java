import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int doubleArraySize = scanner.nextInt();
        int calcCount = scanner.nextInt();
        int array[][] = new int[doubleArraySize+1][doubleArraySize+1];
        int sumArray[][] = new int [doubleArraySize+1][doubleArraySize+1];
        int result[] = new int[calcCount];

        for(int i = 1; i <= doubleArraySize; i++){
            for(int j = 1; j <= doubleArraySize; j++){
                array[i][j] = scanner.nextInt();
            }
        }


        for(int i = 1; i <= doubleArraySize; i++){
            for(int j = 1; j <= doubleArraySize; j++){
                sumArray[i][j] = sumArray[i][j - 1] + sumArray[i -1][j] - sumArray[i-1][j-1] + array[i][j];
            }
        }

        for(int i = 0; i < calcCount; i++){
            int startX = scanner.nextInt();
            int startY = scanner.nextInt();
            int endX = scanner.nextInt();
            int endY = scanner.nextInt();
            result[i] = sumArray[endX][endY] - sumArray[startX-1][endY] - sumArray[endX][startY-1] + sumArray[startX-1][startY-1];
        }
        for(int i = 0; i < calcCount; i++){
            System.out.println(result[i]);
        }
    }
}
