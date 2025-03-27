import java.util.Scanner;

public class login {
    public boolean login(hesap hesap1){
        Scanner input = new Scanner(System.in);
        String kullanici;
        String sifre;
        System.out.println("kullanıcı adi = ");
        kullanici = input.nextLine();
        System.out.println("sifre= ");
        sifre = input.nextLine();
        if(hesap1.getIsim().equals(kullanici)&&hesap1.getSifre().equals(sifre)){
            return true;
        }
        else {
            System.out.println("yanlış giriş yaptınız");
            return false;
        }


    }
}
