package com.company;

public class Main {

    public static void main(String[] args) {
	Cliente cliente = new Cliente();
	Trabajador trabajador = new Trabajador();

	cliente.nombre = "Neithan";
	cliente.edad = 20;
	cliente.telefono = 555;
	cliente.credito = 50;
	trabajador.salario = 100;


	System.out.println(cliente.nombre);
    System.out.println(cliente.edad);
    System.out.println(cliente.telefono);
    System.out.println(cliente.credito);
    System.out.println(trabajador.salario);


    }
}

class Persona{
    String nombre;
    int edad;
    int telefono;
}

class Cliente extends Persona{
    int credito;
}

class Trabajador extends Persona{
    int salario;
}