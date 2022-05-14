package com.privacidadAbstracionEncapsulamiento;

public class Main {
    public static void main(String[] args){
        Persona persona = new Persona();

        //estableciendo valores para cada propiedad con los setters
        persona.setNombre("Daniel");
        persona.setEdad(24);
        persona.setTelefono("3174242424");

        //mostrando valores en pantalla con los getters

        System.out.println(persona.getNombre());
        System.out.println(persona.getEdad());
        System.out.println(persona.getTelefono());
    }
}

class Persona{
    private String nombre;
    private int edad;
    private String telefono;

    //definiendo el setters de cada propiedad
    public void setNombre(String nombre)
    {
        this.nombre = nombre;
    }

    public void setEdad(int edad)
    {
        this.edad = edad;
    }

    public void setTelefono(String telefono)
    {
        this.telefono = telefono;
    }

    //definiendo los getters de cada propiedad

    public String getNombre()
    {
        return this.nombre;
    }

    public int getEdad()
    {
        return this.edad;
    }

    public String getTelefono()
    {
        return this.telefono;
    }
}
