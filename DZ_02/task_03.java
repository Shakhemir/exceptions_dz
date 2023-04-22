public static void main(String[] args) throws Exception {
    try {
        int a = 90;
        int b = 3;
        System.out.println(a / b);
        printSum(23, 234);
        int[] abc = {1, 2};
        abc[3] = 9;
    } catch (ArithmeticException ex) {
        System.out.println("Возможно было деление на 0");
    } catch (IndexOutOfBoundsException ex) {
        System.out.println("Массив выходит за пределы своего размера!");
    } catch (Throwable ex) {
        System.out.println("Что-то пошло не так. Проверь код");
    }
}

public static void printSum(Integer a, Integer b) {
    System.out.println(a + b);
}