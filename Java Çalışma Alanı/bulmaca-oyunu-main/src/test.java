import java.util.Random;

public class test {
    public static void main(String[] args) {
        kartlar kart = new kartlar();
        Random random = new Random();

        System.out.println("|*****|*****|*****|*****|");
        System.out.printf("|**%s**|**%s**|**%s**|**%s**|\n", '?', '?', '?', '?');
        System.out.printf("|**%s**|**%s**|**%s**|**%s**|\n", '?', '?', '?', '?');
        System.out.printf("|**%s**|**%s**|**%s**|**%s**|\n", '?', '?', '?', '?');
        System.out.printf("|**%s**|**%s**|**%s**|**%s**|\n", '?', '?', '?', '?');


        System.out.println("|*****|*****|*****|*****|\n");
        kart.karistir();
        String kota[][] = new String[8][2];
        int sayac1 = 0;
        int sayac2 = 0;
        int son = 0;

        boolean tek = true;
        while (true) {

            try {
                int a1 = random.nextInt(4);
                int a2 = random.nextInt(4);
                int b1 = random.nextInt(4);
                int b2 = random.nextInt(4);
                if (!(a1 == b1 && a2 == b2)) {
                    if (kart.getHarf(a1, a2) == kart.getHarf(b1, b2)) {
                        if (tek == true) {
                            System.out.printf("tahmin doğru: %s==%s\n", kart.getHarf(a1, a2), kart.getHarf(b1, b2));
                            System.out.printf("indis değeri (%d,%d) ve (%d %d)\n",a1+1,a2+1,b1+1,b2+1);

                            kota[sayac1][sayac2] = kart.getHarf(a1, a2);
                            sayac2++;
                            kota[sayac1][sayac2] = kart.getHarf(b1, b2);
                            sayac2 = 0;
                            sayac1++;
                            tek = false;

                        }

                        if(tek==false){
                            for(int z=0;z<8;z++){
                                if (kart.getHarf(a1,a2)==kota[z][0]&&kart.getHarf(b1,b2)==kota[z][1]){
                                    son=1;
                                    break;

                                }

                            }
                            if (son==0){
                                System.out.printf("tahmin doğru: %s==%s\n", kart.getHarf(a1, a2), kart.getHarf(b1, b2));
                                System.out.printf("indis değeri (%d,%d) ve (%d %d)\n",a1+1,a2+1,b1+1,b2+1);
                                kota[sayac1][sayac2] = kart.getHarf(a1, a2);
                                sayac2++;
                                kota[sayac1][sayac2] = kart.getHarf(b1, b2);
                                sayac2 = 0;
                                sayac1++;
                            }

                            son=0;


                        }
                        if (kota[7][1]!=null){

                            System.out.printf("|**%s**|**%s**|**%s**|**%s**|\n", kart.getHarf(0,0),kart.getHarf(0,1),kart.getHarf(0,2),kart.getHarf(0,3));
                            System.out.printf("|**%s**|**%s**|**%s**|**%s**|\n", kart.getHarf(1,0),kart.getHarf(1,1),kart.getHarf(1,2),kart.getHarf(1,3));
                            System.out.printf("|**%s**|**%s**|**%s**|**%s**|\n", kart.getHarf(2,0),kart.getHarf(2,1),kart.getHarf(2,2),kart.getHarf(2,3));
                            System.out.printf("|**%s**|**%s**|**%s**|**%s**|\n", kart.getHarf(3,0),kart.getHarf(3,1),kart.getHarf(3,2),kart.getHarf(3,3));

                            System.out.println("Tüm tahminler yapıldı program sonlandırılıyor");
                            break;
                        }

                        }
                    }
                } catch(Exception e){

                    System.out.println(e);
                    break;}
        }
    }
}











