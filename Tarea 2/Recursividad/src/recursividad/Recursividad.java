package recursividad;

import java.util.Scanner;

/**
 *
 * @author seel_
 */

public class Recursividad {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        
        int numero1, numero2;
        
        System.out.print("Introduzca primer numero: ");
        
        numero1 = sc.nextInt();
        
        System.out.print("Introduzca segundo numero: ");
        
        numero2 = sc.nextInt();
        
        System.out.println("Suma: " + suma (numero1, numero2));

    }

    public static int suma(int a, int b) {
      
        if (b == 0) {
            
            return a;
            
        } 
        
        else if (a == 0) {
            
            return b;
            
        } 
        
        else {
            
            return 1 + suma(a, b - 1);
            
        }
        
    }
    
}
