try {
    int d = 0;
    double catchedRes1 = intArray[8] / d;
    System.out.println("catchedRes1 = " + catchedRes1);
} catch (IndexOutOfBoundsException) {
    System.out.println("Index out of range");
} catch (ArithmeticException) {
    System.out.println("Division by zero");
}