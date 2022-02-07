import java.util.Scanner;

public class Demo {

    private static Scanner sc;

    public static void main(String[] args) {
        int num, sum = 0;
        sc = new Scanner(System.in);

        System.out.println("Please enter any integer: ");
        num = sc.nextInt();

        while (num <= 10000) {
            sum = sum + num;
            num++;
        }
        System.out.println("Sum of the numbers from while loop: " + sum);
    }
}
