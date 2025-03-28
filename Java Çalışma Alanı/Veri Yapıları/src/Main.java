import java.lang.reflect.GenericArrayType;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.SortedSet;


public class Main  {
    public static void main(String[] args) {
        /**
        System.out.println("Hello world!");
        Counter c;
        Counter deneme=new Counter();
        c =new Counter();
        deneme=c;

        System.out.println(deneme.count);
        for (int i=0;i<100;i++){
            deneme.incrementCount();
        }
        System.out.println(c.count);
        c.decrementCount();
        System.out.println(deneme.count);
         **/
        Gnome cupra=new Gnome(23,"balik");
        Gnome hamsi=new Gnome(5,"balik2");

        System.out.println(cupra.weight);
        System.out.println(cupra.name);
        cupra.fish();
        hamsi.fish();
        LinkedList<String> denemee=new LinkedList<>();






    }
}