package test;
import java.util.*;

public class hw3_16102284 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String num1 , num2;
		System.out.println("Input two natural number");
		while(true) {
			num1 = scan.next();
			num2 = scan.next();
			try {
				int hei=Integer.parseInt(num1);
				int wid=Integer.parseInt(num2);
				if(hei>0 && hei<101 && wid>0 && wid<101) {
					rectangle(hei, wid);
					System.exit(0);
				}
				else {
					System.out.println("INPUT ERROR!");
				}
			}
			catch(NumberFormatException e) {
				System.out.println("INPUT ERROR!");
			}
			
		}
    }
	public static void rectangle(int hei, int wid) {
		for(int i = 1; i < (hei * wid)+1; i++) {
			if(i%wid==0) {
				System.out.println(i + " ");
			}
			else {
				System.out.print(i + "  ");
			}
		}
	}

}
