/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package implementation;

import generator.DFA;
import generator.NFA;

import java.util.ArrayList;
import java.util.Scanner;

/**
 * @author tona
 */
public class Run {
    private static NFA automaton = new NFA();
    //private static DFA automaton = new DFA();
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);

        initializeAutomaton();
        for (int i = 0; i < 10; i++) {
            System.out.println("Introduce una cadena: ");
            String myString = scanner.nextLine();

            if (automaton.evaluateString(myString))
                System.out.println("Cadena valida");
            else
                System.out.println("Cadena no valida");

        }
    }

    private static void initializeAutomaton() {
        ArrayList<Character> alphabet = new ArrayList<>();
        ArrayList<Integer> states = new ArrayList<>();
        int initialState;
        String statesString;

        alphabet.add('0');
        alphabet.add('1');
        alphabet.add('5');

        states.add(0);
        states.add(1);
        states.add(2);
        states.add(3);
        states.add(4);
        states.add(5);

        automaton.setAlphabet(alphabet);
        automaton.setStates(states);
        automaton.setInitialState(0);
        automaton.addFinalState(6);
        automaton.addFinalState(4);

        automaton.addTransition(0, 0, '0');
        automaton.addTransition(0, 1, '0');
        automaton.addTransition(1, 2, 'e');
        automaton.addTransition(1, 3, 'e');
        automaton.addTransition(2, 4, '1');
        automaton.addTransition(3, 5, '0');
        automaton.addTransition(5, 6, '5');

    }
}
