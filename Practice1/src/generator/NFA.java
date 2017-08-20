/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package generator;

import java.util.ArrayList;
import java.util.Stack;

/**
 * @author Alumno
 */
public class NFA {
    ArrayList<Character> alphabet;
    ArrayList<Integer> finalStates;
    int initialState;
    ArrayList<Integer> currentStates;
    ArrayList<Transition> transitions;
    private ArrayList<Integer> states;

    public NFA() {
        states = new ArrayList<>();
        transitions = new ArrayList<>();
        finalStates = new ArrayList<>();
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

    public void addFinalState(int state) {
        finalStates.add(state);
    }

    public boolean evaluateString(String word) {
        currentStates = getEpsilonStates(initialState);
        for (char c : word.toCharArray()){
            currentStates = getEpsilonStates(move(currentStates, c));
        }
        for (int s : currentStates) {
            System.out.println(s);
            if (finalStates.contains(s))
                return true;
        }

        return false;
    }

    private ArrayList<Integer> getEpsilonStates(int state) {
        ArrayList<Integer> aux = new ArrayList<>();
        Stack<Integer> stack = new Stack<>();
        stack.push(state);
        aux.add(state);
        while (!stack.empty()) {
            int s = stack.pop();
            for (Transition t: transitions) {
                if (t.getSymbol() == 'e' && t.getCurrentState() == s && !aux.contains(t
                        .getNextState())) {
                    aux.add(t.getNextState());
                    stack.push(t.getNextState());
                }
            }
        }
        return aux;
    }

    private ArrayList<Integer> getEpsilonStates(ArrayList<Integer> states) {
        ArrayList<Integer> aux = new ArrayList<>();
        for (int s : states) {
            aux.addAll(getEpsilonStates(s));
        }
        return aux;
    }

    private ArrayList<Integer> move(ArrayList<Integer> states, Character c) {
        ArrayList<Integer> nextStates = new ArrayList<>();
        for (int s: states)
            for (Transition transition : transitions)
                if (s == transition.getCurrentState() && transition.getSymbol() == c)
                    nextStates.add(transition.getNextState());

        return nextStates;
    }
}
