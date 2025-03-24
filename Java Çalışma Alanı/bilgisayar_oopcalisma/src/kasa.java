public class kasa {
    private String model;
    private String uretici;
    private String malzeme;
    private anakart anakart;
    private monitor monitor;

    public kasa(String model, String uretici, String malzeme,anakart anakart,monitor monitor) {
        this.model = model;
        this.uretici = uretici;
        this.malzeme = malzeme;
        this.anakart=anakart;
        this.monitor=monitor;
    }

    public anakart getAnakart() {
        return anakart;
    }

    public monitor getMonitor() {
        return monitor;
    }

    public void setMonitor(monitor monitor) {
        this.monitor = monitor;
    }

    public void setAnakart(anakart anakart) {
        this.anakart = anakart;
    }

    public void ac(){
        System.out.println("bilgisayar açılıyor");
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public String getUretici() {
        return uretici;
    }

    public void setUretici(String uretici) {
        this.uretici = uretici;
    }

    public String getMalzeme() {
        return malzeme;
    }

    public void setMalzeme(String malzeme) {
        this.malzeme = malzeme;
    }
}

