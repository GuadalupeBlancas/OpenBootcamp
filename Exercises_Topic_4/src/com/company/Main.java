package com.company;

public class Main {

    public static void main(String[] args) {
	    double numeroIf = 0;
	    double numeroWhile = 0;
	    int numeroFor = 0;
	    String estacion = "año";

	    if(numeroIf < 0){
	        System.out.println("El valor de la variable numeroIf es negativo");
        } else if(numeroIf > 0){
	        System.out.println("El valor de la variable numeroIf es positivo");
        }else if(numeroIf == 0){
	        System.out.println("El valor de la varible numeroIf es 0");
        }


	    while(numeroWhile <3){
	        System.out.println(numeroWhile);
	        numeroWhile++;
        }

	    do {
            System.out.println(numeroWhile);
	    } while (numeroWhile < 3);

	    for(; numeroFor <= 3; numeroFor++){
            System.out.println(numeroFor);
        }

	    switch (estacion){
            case "Primavera":
	        System.out.println("Estamos en: " + estacion);
	        break;
            case "Verano":
            System.out.println("Estamos en: " + estacion);
            break;
            case "Invierno":
            System.out.println("Estamos en: " + estacion);
            break;
            case "Otoño":
            System.out.println("Estamos en: " + estacion);
            break;
            default:
                System.out.println("EL valor de la varible estación no es ninguna estación del año");
        }
    }
}
