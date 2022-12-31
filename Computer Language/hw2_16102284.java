package test;
import java.util.*;


public class hw2_16102284 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String num1 , num2;
		System.out.println("Input two natural number");
		while(true) {
			num1 = scan.next();
			num2 = scan.next();
			try {
				int a1=Integer.parseInt(num1);
				int b1=Integer.parseInt(num2);
				if(a1>1 && a1<10 && b1>1 && b1<10) {
					gugudan(a1,b1);
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
	
	public static void gugudan(int num1,int num2){		
		if(num1 < num2) {
			for(int i = 1; i<10; i++) {
				for(int a=num1; a<=num2; a++) {
					if(a*i < 10) {
						System.out.print(a + " * " + i + " =  " + a*i +  "   ");
					}
					else {
						System.out.print(a + " * " + i + " = " + a*i +  "   ");
					}
					
				}
				System.out.println();
			}
		}
			else {
				for(int j = 1; j<10; j++) {
					for(int b = num1; b>=num2; b--) {
						if(b*j < 10) {
							System.out.print(b + " * " + j + " =  " + b*j  + "   ");
						}
						else {
							System.out.print(b + " * " + j + " = " + b*j + "   ");
						}
					}
					System.out.println();
				
			}
			
			
		}

	}			
}
