public class Main {
    public static void main(String[] args) {
        resolution resolution=new resolution(1920,1080);
        monitor monitor = new monitor("e300","samsung","16",resolution);
        anakart anakart = new anakart("b250","asus",4,"windows");
        kasa kasa=new kasa("shadowblade","shadoww","metal",anakart,monitor);

        System.out.println(kasa.getAnakart().getIsletim_sistemi());

        kasa.getAnakart().yukle("linux");
        System.out.println(kasa.getAnakart().getIsletim_sistemi());
        System.out.println(kasa.getMonitor().getResolution().getBoy());

    }
}