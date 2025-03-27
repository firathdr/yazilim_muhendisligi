import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
    atm atm1 = new atm();
    hesap hesap1 = new hesap("firat","123",2000);

    atm1.calis(hesap1);
        System.out.println("programdan çıkılıyor");
    }
}