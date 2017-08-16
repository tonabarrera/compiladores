/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package implementation;

import generator.Automaton;

import java.util.ArrayList;

/**
 *
 * @author tona
 */
public class Run {
    public static void main(String args[]) {
        System.out.println("Hi");
        boolean is_valid;
        Automaton automaton = new Automaton();
        automaton.setInitialState(0);
        ArrayList<Character> alphabet = new ArrayList<Character>();
        alphabet.add('a');
        alphabet.add('b');
        alphabet.add('c');
        alphabet.add('d');
        alphabet.add('e');
        automaton.setAlphabet(alphabet);
        ArrayList<Integer> states = new ArrayList<>();
        states.add(0);
        states.add(1);
        states.add(2);
        automaton.setStates(states);
        automaton.addTransition(0, 1, 'a');
        is_valid = automaton.evaluateString("madre mia willy");
        if (is_valid) System.out.println("Valido"); else System.out.println("No valido");
    }
}
