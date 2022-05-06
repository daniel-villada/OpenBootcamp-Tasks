package com.ejerFunciones;



public class Main {
    public static void main(String[] args)
    {
        suma(2, 5, 3);
    }

    //Primera parte del ejercicio: Funcion que sume 3 numeros.
    public static void suma(int a, int b, int c){
        int resultado;
        resultado = a + b + c;
        System.out.println("El resultado de la suma es: " + resultado);
    }
}

class Coche{
    int numeroPuertas = 4;
    int puertasCoche(int numeroPuertas,int nPuertas){
        return numeroPuertas + nPuertas;
    }
}




