package com.company;

import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
       // Parte 1
       int a=1, b=2, c=3;
       System.out.println(suma(a,b,c));

       //Parte 2
        coche auto = new coche();
        auto.sumarPuerta();
        System.out.println(auto.p);
    }

    //Parte 1
    public static int suma(int a, int b, int c) {
        return a+b+c;
    }

    //Parte 2
    static class coche{
        public int p = 4;

        public void sumarPuerta(){
            this.p++;
        }
    }
}
