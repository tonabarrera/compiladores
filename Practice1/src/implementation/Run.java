/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package implementation;

import generator.Automaton;

import java.util.ArrayList;
import java.util.Scanner;

/**
 * @author tona
 */
public class Run {
    private static Scanner scanner;
    private static Automaton automaton = new Automaton();

    public static void main(String args[]) {
        scanner = new Scanner(System.in);

        boolean is_valid;
        initializeAutomaton();
        for (int i = 0; i < 10; i++) {
            System.out.println("Introduce a string: ");
            String myString = scanner.nextLine();

            is_valid = automaton.evaluateString(myString);

            if (is_valid) System.out.println("Valido");
            else System.out.println("No valido");
        }
    }

    private static void initializeAutomaton() {
        ArrayList<Character> alphabet = new ArrayList<>();
        ArrayList<Integer> finales = new ArrayList<>();
        ArrayList<Integer> states = new ArrayList<>();
        int initialState;
        String alphabetString;
        String statesString;

        System.out.println("1.-Introduce your alphabet symbols separate for a space:");
        alphabetString = scanner.nextLine();
        for (Character symbol : alphabetString.toCharArray())
            if (symbol != ' ') alphabet.add(symbol);

        System.out.println("2.-Introduce your states:");
        statesString = scanner.nextLine();
        for (String state : statesString.split(" "))
            states.add(Integer.valueOf(state));

        System.out.println("3.-Introduce your initial state:");
        initialState = scanner.nextInt();
        scanner.nextLine();

        System.out.println("4.-Introduce your final states separate for a space:");
        statesString = scanner.nextLine();
        for (String state : statesString.split(" "))
            finales.add(Integer.valueOf(state));

        System.out.println("5.-Introduce your transitions (currentState, nextState, symbol)");

        automaton.setAlphabet(alphabet);
        automaton.setStates(states);
        automaton.setInitialState(initialState);
        automaton.setFinalStates(finales);

        automaton.addTransition(0, 0, 'b');
        automaton.addTransition(0, 1, 'a');

        automaton.addTransition(1, 2, 'b');
        automaton.addTransition(1, 1, 'a');

        automaton.addTransition(2, 3, 'b');
        automaton.addTransition(2, 1, 'a');

        automaton.addTransition(3, 0, 'b');
        automaton.addTransition(3, 1, 'a');

        //        automaton.addTransition(0, 1, '1');
//        automaton.addTransition(1, 0, '1');
//        automaton.addTransition(0, 2, '0');
//        automaton.addTransition(2, 0, '0');
//        automaton.addTransition(3, 1, '0');
//        automaton.addTransition(1, 3, '0');
//        automaton.addTransition(3, 2, '1');
//        automaton.addTransition(2, 3, '1');
    }
}
