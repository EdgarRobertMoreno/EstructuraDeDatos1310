package contadorregresivo;

/**
 *
 * @author seel_
 */

public class ContadorRegresivo {

    public static void main(String[] args) {
        
        ContadorRegresivo Bomba = new ContadorRegresivo();
        
        Bomba.CuentaAtras(30);
        
    }
    
    public void CuentaAtras(int segundos) {
    
        if(segundos == 0 ){
        
            //Caso Base
            
            System.out.println("BOOMMMMM !!!");
        
        }
        else {
        
            //Dominio
            
            System.out.println(segundos);
            
            //La recursividad
            
            CuentaAtras(segundos -1);
            
        }
        
    }
    
}
