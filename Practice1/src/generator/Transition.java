package generator;

/**
 * Created by tona on 16/08/2017 for Practice1.
 */
class Transition {
    private int currentState;
    private int nextState;
    private char symbol;

    Transition(int currentState, int nextState, char symbol) {
        this.currentState = currentState;
        this.nextState = nextState;
        this.symbol = symbol;
    }

    int getCurrentState() {
        return currentState;
    }

    int getNextState() {
        return nextState;
    }

    char getSymbol() {
        return symbol;
    }
}
