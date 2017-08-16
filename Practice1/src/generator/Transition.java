package generator;

import java.util.ArrayList;

/**
 * Created by tona on 16/08/2017 for Practice1.
 */
public class Transition {
    private int currentState;
    private int nextState;
    private char symbol;

    public Transition(int currentState, int nextState, char symbol) {
        this.currentState = currentState;
        this.nextState = nextState;
        this.symbol = symbol;
    }
}
