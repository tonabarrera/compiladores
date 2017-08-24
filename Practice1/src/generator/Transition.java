package generator;

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
