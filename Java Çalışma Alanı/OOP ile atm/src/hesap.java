public class hesap {
    private String isim;
    private String sifre;
    private int bakiye;

    public hesap(String isim, String sifre, int bakiye) {
        this.isim=isim;
        this.sifre=sifre;
        this.bakiye=bakiye;
    }

    public void yatir(int tutar){
        bakiye=bakiye+tutar;
        System.out.println("yeni bakiye ="+bakiye);
    }
    public void cek(int tutar){
        if(tutar>bakiye) System.out.println("yetersiz bakiye , bakiyeniz= "+ bakiye);
        else {
            bakiye -= tutar;
            System.out.println("çekilen tutar ="+tutar +"  yeni bakiyeniz = " + bakiye);
        }
    }
    public String getIsim() {
        return isim;
    }

    public void setIsim(String isim) {
        this.isim = isim;
    }

    public String getSifre() {
        return sifre;
    }

    public void setSifre(String sifre) {
        this.sifre = sifre;
    }

    public int getBakiye() {
        return bakiye;
    }

    public void setBakiye(int bakiye) {
        this.bakiye = bakiye;
    }
}
