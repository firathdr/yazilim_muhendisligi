public class monitor {
    private String model;
    private String uretici;
    private String boyut;
    private resolution resolution;

    public monitor(String model, String uretici, String boyut, resolution resolution) {
        this.model = model;
        this.uretici = uretici;
        this.boyut = boyut;
        this.resolution = resolution;
    }
    public void monitorukapat(){
        System.out.println("monitör kapatılıyor");
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

    public String getBoyut() {
        return boyut;
    }

    public void setBoyut(String boyut) {
        this.boyut = boyut;
    }

    public resolution getResolution() {
        return resolution;
    }

    public void setResolution(resolution resolution) {
        this.resolution = resolution;
    }
}
