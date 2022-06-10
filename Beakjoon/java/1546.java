import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int count = scanner.nextInt();
        double array[] = new double[count];
        double tmp = 0;
        double sum = 0;
        for(int i = 0; i < count; i++){
            array[i] = scanner.nextInt();
        }
        for(int i = 0; i < count; i++){
            for (int j = 0; j < i ; j++){
                if(array[i] < array[j]){
                    tmp = array[i];
                    array[i] = array[j];
                    array[j] = tmp;
                }
            }
        }
        double highiest = array[count-1];
        for(int i = 0; i < count; i++){
            array[i] = (array[i]/ highiest) * 100;
            sum += array[i];
        }
        System.out.println(sum/(double) count);
    }
}
