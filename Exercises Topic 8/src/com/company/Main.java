package com.company;

public class Main {

    public static void main(String[] args) {
	    Persona persona = new Persona();
	    persona.setNombre("Miranda");
	    persona.setEdad(20);
	    persona.setTelefono(5551212);

	    System.out.println(persona.getNombre());
	    System.out.println(persona.getEdad());
	    System.out.println(persona.getTelefono());
    }
}

class Persona{
    private String nombre;
    private int edad;
    private int telefono;

    public void setNombre(String nombre){
        this.nombre = nombre;
    }

    public String getNombre() {
        return nombre;
    }

    public void setEdad(int edad){
        this.edad = edad;
    }

    public int getEdad() {
        return edad;
    }

    public void setTelefono(int telefono){
        this.telefono = telefono;
    }

    public int getTelefono() {
        return telefono;
    }
}