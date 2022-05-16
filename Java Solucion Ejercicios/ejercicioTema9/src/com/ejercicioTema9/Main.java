package com.ejercicioTema9;

public class Main {
    public static void main(String[] args){
        Cliente cliente = new Cliente();
        Trabajador trabajador = new Trabajador();

        System.out.println("*Cliente*");
        cliente.nombre = "Daniel";
        cliente.edad = 24;
        cliente.telefono = "+573636366363";
        cliente.credito = 2500.54;

        System.out.println("nombre: " + cliente.nombre+"\n" + "edad: " + cliente.edad+"\n" + "telefono: " + cliente.telefono+"\n"+ "credito: " + "$"+cliente.credito + "\n");

        System.out.println("*Trabajador*");
        trabajador.nombre = "Alberto";
        trabajador.edad = 27;
        trabajador.telefono = "+15252525252";
        trabajador.salario = 1500.25;

        System.out.println("nombre: " + trabajador.nombre+"\n" + "edad: " + trabajador.edad+"\n" + "telefono: " + trabajador.telefono+"\n" + "Salario: " + "$"+trabajador.salario);
    }
}

class Persona{
    String nombre;
    int edad;
    String telefono;
}

class Cliente extends Persona{
    double credito;
}

class Trabajador extends Persona{
    double salario;
}
