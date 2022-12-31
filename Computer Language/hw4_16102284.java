package test;
import java.util.*;

public class hw4_16102284 {

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
		if(hei % 2 == 0) {
			for(int i = 0; i<hei/2; i++) {
				for(int j = 1; j<(wid+1); j++) {
					if(j%wid != 0) {
						System.out.print((j + (2 * wid*i)) + "   ");
					}
					else {
						System.out.println((j + (2 * wid*i)) + "   ");
					}
				}
			for(int k = wid; k > 0; k--) {
					if(k % wid != 1) {
						System.out.print((wid*(2*i+1) + k) + "   ");
					}
					else {
						System.out.println((wid*(2*i+1) + k) + "   ");
					}
				}
				
				
			}
		}
		else {
			for(int i = 0; i<hei/2; i++) {
				for(int j = 1; j<(wid+1); j++) {
					if(j%wid != 0) {
						System.out.print((j + (2 * wid*i)) + "   ");
					}
					else {
						System.out.println((j + (2 * wid*i)) + "   ");
					}
				}
			for(int k = wid; k > 0; k--) {
					if(k % wid != 1) {
						System.out.print((wid*(2*i+1) + k) + "   ");
					}
					else {
						System.out.println((wid*(2*i+1) + k) + "   ");
					}
				}
			
			}
		for(int l = wid * (hei-1) + 1; l< (wid * hei) +1; l++) {	
			if(l%wid==0) {
				System.out.println(l + "  ");
				}
			else {
				System.out.print(l + "   ");
				}
			}
			
			
				
			
			
			
			
			
			
		}
		
		
		
		
	}

}
