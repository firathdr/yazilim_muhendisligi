import java.util.Random;
import java.util.ArrayList;


public class kartlar {
    private String havuz[]={"A","B","C","D","E","F","G","H","A","B","C","D","E","F","G","H"};
     String harf[][]=new String[4][4];
    Random rand = new Random();

    public String getHarf(int a,int b) {
        return harf[a][b];
    }

    public String getHavuz(int a) {

        return havuz[a];
    }
    int count=16;
    public void karistir(){
        for(int i=0;i<4;i++){
            for (int j=0;j<4;j++){
                int hafiza =rand.nextInt(count);
                count-=1;
                harf[i][j]=havuz[hafiza];
                havuz=remove(havuz,hafiza);

            }
        }
    }



    public  String[] remove(String[] dizi, int index){
        if (index < 0 || index >= dizi.length) {
            return dizi;  // İndeks geçersiz ise diziyi değiştirmeden geri döndür
        }
        String [] yenidizi = new String[dizi.length-1];
        int yenindeks=0;
        for (int i = 0; i < dizi.length; i++) {
            if (i != index) {
                yenidizi[yenindeks] = dizi[i];
                yenindeks++;
            }
        }
        return yenidizi;
    }



}
