import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class b2750 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int count = Integer.parseInt(br.readLine());
        int array[] = new int[count];
        int tmp = 0;
        for(int i = 0; i < count; i++){
            array[i] = Integer.parseInt(br.readLine());
        }


        for(int i = 0; i < count; i++){
            for(int j =0; j < count; j++){
                if(array[i] < array[j]&&array[i]!= array[j]){
                    tmp = array[i];
                    array[i] = array[j];
                    array[j] = tmp;
                }
            }
        }


        for(int i = 0; i < count; i++){
            if(i + 1 != count){
                if(array[i] == array[i+1]) {
                    i++;
                }
            }
            System.out.println(array[i]);
        }

    }
}
