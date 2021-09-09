
package seriedefibonacciconrecursividad;

import java.util.Scanner;

/**
 *
 * @author seel_
 */
public class SerieDeFibonacciConRecursividad {

    
    public static void main(String[] args) {
        
        int x = 0;
        
        System.out.println("Ingrese un numero...");
        
        Scanner consola = new Scanner(System.in);

        x = consola.nextInt();
  
        SerieDeFibonacciConRecursividad ObjetoFibonacci = new SerieDeFibonacciConRecursividad();
        
        System.out.println("La Sucesion Fibonacci de "+ x + " mediante Recursividad es " + ObjetoFibonacci.fibonacciRecursivo(x));
        
    }
    
    //Metodo recursivo para la sucesion Fibonacci
    
    public int fibonacciRecursivo(int n){
    
        if(n==1 || n==2){
        
            //El caso base, la respuesta 
            
            return 1;
        }
        else{
        
            //Dominio (Problema -1)
            
            return fibonacciRecursivo(n-1) + fibonacciRecursivo(n-2);
            
        }
        
        
    }
    
}
