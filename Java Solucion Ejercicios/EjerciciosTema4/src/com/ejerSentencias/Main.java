package com.ejerSentencias;



public class Main {
    public static void main(String[] args){

        //ejercicio con if
        int numeroIf = 0;
        System.out.println("*****Usando if*****");
        if (numeroIf > 0 ){
            System.out.println("El " + numeroIf  + " es Positivo.");
        }
        else if (numeroIf < 0) {
            System.out.println("El " + numeroIf  + " es Negativo.");
        }
        else{
            System.out.println("Numero es igual a 0");
        }

        //Ejercicio con Ciclo While
        int numeroWhile = 0;
        System.out.println("*****Usando while*****");

        while (numeroWhile < 3){
            numeroWhile++;
            System.out.println(numeroWhile);
        }

        //Ejercicio con Ciclo Do While
        int numeroDoWhile = 3;
        System.out.println("Usando DoWhile");

        do {
            numeroDoWhile++;
            System.out.println(numeroDoWhile);
        }while (numeroDoWhile < 3);

        //Ejercicio con Ciclo For
        System.out.println("*****Usando For*****");

        for (int numeroFor = 0; numeroFor <=3 ; numeroFor++){
            System.out.println(numeroFor);
        }

        //Ejercicio con Switch-Case

        String estacion = "Super Mario";
        System.out.println("*****Usando Switch*****");

        switch (estacion){
            case("Invierno"):
                System.out.println("estamos en Invierno");
                break;
            case("Otoño"):
                System.out.println("estamos en Otoño");
                break;
            case("Primavera"):
                System.out.println("estamos en Primavera");
                break;
            case("Verano"):
                System.out.println("estamos en Verano");
                break;
            default:
                System.out.println("No es una estacion del año");
        }
    }
}
