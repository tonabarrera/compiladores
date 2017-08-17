/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package generator;

import java.util.ArrayList;

/**
 *
 * @author tona
 */
public class Automaton {
    private ArrayList<Character> alphabet;
    private ArrayList<Integer> states;
    private ArrayList<Integer> finalStates;
    private int initialState;
    private ArrayList<Transition> transitions;
    private int currentState;

    public Automaton() {
        transitions = new ArrayList<>();
    }

    public void setAlphabet(ArrayList<Character> alphabet) {
        this.alphabet = alphabet;
    }

    public void setStates(ArrayList<Integer> states) {
        this.states = states;
    }

    public void setFinalStates(ArrayList<Integer> finalStates) {
        this.finalStates = finalStates;
    }

    public void setInitialState(int initialState) {
        this.initialState = initialState;
    }

    public void addTransition(int currentState, int nextState, char symbol) {
        transitions.add(new Transition(currentState, nextState, symbol));
    }

    public boolean evaluateString(String word) {
        currentState = initialState;
        for (char symbol: word.toCharArray()) {
            if (!alphabet.contains(symbol)) return false;
            System.out.println("symbol: " + symbol);
            for (Transition transition: transitions) {
                if (transition.getCurrentState() == currentState) {
                    if (transition.getSymbol() == symbol){
                        currentState = transition.getNextState();
                        break;
                    }
                }
            }
        }
        return finalStates.contains(currentState);
    }
}
