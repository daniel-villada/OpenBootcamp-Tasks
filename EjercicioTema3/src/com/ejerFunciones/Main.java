package com.ejerFunciones;



public class Main {
    public static void main(String[] args) {
        //llamo mi funcion suma
        suma(2, 5, 3);

        //Creo Objecto miCoche
        Coche miCoche = new Coche();
        miCoche.numeroPuertas = 4;
        System.out.println("Numero de puertas: " + miCoche.incrementoPuertas(1));
    }

    //Primera parte del ejercicio: Funcion que suma 3 numeros.
    public static void suma(int a, int b, int c){
        int resultado;
        resultado = a + b + c;
        System.out.println("El resultado de la suma es: " + resultado);
    }

    //Segunda parte del ejercicio: Creo Clase Coche
    public static class Coche{
        int numeroPuertas;

        int incrementoPuertas(int puerta){
            int cantidadPuertas = numeroPuertas + puerta;
            return cantidadPuertas;
        }
    }
}





