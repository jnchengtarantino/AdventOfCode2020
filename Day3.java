import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Day3 {
   public static void main(String[] args) {
    File file = new File("day3input.txt");
    BufferedReader reader = null;

    try {
        reader = new BufferedReader(new FileReader(file));
        String text = null;

        int x1 = 0, x2 = 0, x3 = 0 , x4 = 0, x5 = 0;
        int y5= 0;
        int count1 = 0, count2 = 0, count3 = 0, count4 = 0, count5 = 0;
        //part 1
        while ((text = reader.readLine()) != null) {

            if (text.charAt(x1% text.length()) == '#') count1++;
            x1+=1;

            if (text.charAt(x2% text.length()) == '#') count2++;
            x2+=3;

            if (text.charAt(x3% text.length()) == '#') count3++;
            x3+=5;

            if (text.charAt(x4% text.length()) == '#') count4++;
            x4+=7;

            if (y5%2 == 0 && text.charAt(x5% text.length()) == '#') count5++;
            if(y5%2 == 0) x5+=1;
            y5++;
        }

        System.out.println(count1);
        System.out.println(count2);
        System.out.println(count3);
        System.out.println(count4);
        System.out.println(count5);

        System.out.println(count1*count2*count3*count4*count5);
        //part 2

        System.out.println("Reached end of file");
    } catch (FileNotFoundException e) {
        e.printStackTrace();
    } catch (IOException e) {
        e.printStackTrace();
    } finally {
        try {
            if (reader != null) {
                reader.close();
            }
        } catch (IOException e) {
        }
    }
   } 
}
