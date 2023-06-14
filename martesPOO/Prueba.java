public class Prueba {
    public static void main(String[] args) {
    int limite = 10;
    int numero1 = 1, numero2 = 0, numero3 = 0;
    String cadena = "";
    
    for(int contador = 0; contador < limite; contador++){
        
        cadena += numero3 + " ";
        numero3 = 0;
        numero3 += numero2 + numero1;
        numero1 = numero2;
        numero2 = numero3;
    
    }
    System.out.println(cadena);
}
}
