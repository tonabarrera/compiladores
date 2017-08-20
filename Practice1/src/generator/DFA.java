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
public class DFA extends NFA{

    public void setAlphabet(ArrayList<Character> alphabet) {
        this.alphabet.addAll(alphabet);
    }

    public boolean evaluateString(String word) {
        currentStates.add(initialState);
        for (char symbol: word.toCharArray()) {
            if (!alphabet.contains(symbol)) return false;
            for (Transition transition: transitions) {
                if (transition.getCurrentState() == currentStates.get(0)) {
                    if (transition.getSymbol() == symbol){
                        currentStates.set(0, transition.getNextState());
                        break;
                    }
                }
            }
        }
        return finalStates.contains(currentStates.get(0));
    }
}
