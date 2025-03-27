import java.util.Scanner;

public class atm {
    public void calis(hesap hesap1){
        login login1 = new login();
        Scanner scan = new Scanner(System.in);
        System.out.println("Bankamıza hoşgeldiniz");
        int giris_hakki=3;
        while(true){
            if(login1.login(hesap1)){
                System.out.println("giriş başarılı ");
                break;

            }
            else {
                System.out.println("giriş başarısız");
                giris_hakki--;
                System.out.println("kalan giriş hakkı ="+giris_hakki);
            }
            if (giris_hakki==0){
                System.out.println("Giriş hakkınız bitti");
                return;
            }
        }
        System.out.println("********************");
        String islemler = "1. bakiye görüntümele\n2.Para Yatırma\n3.Para çekme\n4.çıkış";
        System.out.println(islemler);
        System.out.println("********************");
        while(true){
            System.out.println("işlem seçiniz");
            Scanner input = new Scanner(System.in);
            String islem = input.nextLine();

            if(islem.equals("q")) break;
            else if (islem.equals("1")){
                System.out.println("bakiyeniz = "+ hesap1.getBakiye());
            }
            else if(islem.equals("2")){
                System.out.println("yatırmak istedigini bakiye giriniz");
                int tutar = scan.nextInt();
                hesap1.yatir(tutar);
            }
            else if(islem.equals("3")){
                System.out.println("çekmek istedigini bakiye giriniz");
                int tutar = scan.nextInt();
                hesap1.cek(tutar);
            }

            if((islem.equals(" ")||islem.equals("")||islem.equals("1")||islem.equals("2")||islem.equals("3")||islem.equals("q"))!=true) System.out.println("geçersiz işlem girdiniz");
        }
    }
}
