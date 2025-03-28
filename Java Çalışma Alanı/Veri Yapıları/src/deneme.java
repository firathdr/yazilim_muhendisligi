import java.util.List;
import java.util.Stack;


public class deneme {
    public static void main(String[] args) {

        int [] a=new int[10];
        for (int i=0; i<a.length;i++){
            a[i]=i+1;

        }

        int [] b=a.clone();
        b[5]=12;
        for (double e:a) {
            System.out.println(e);
        }


        Stack st=new Stack();
        st.push(12);
        st.push(4);
        st.push(6);
        st.push(9);
        st.push(2);
        st.push(12);
        st.pop();
        st.push(45);
        st.push(1);
        st.push(4);
        st.push(6);
        st.push(9);
        st.push(2);
        st.push(12);
        st.pop();
        st.push(45);
        st.push(1);
        for (int i=0;i<st.size();i++){
            System.out.println(st.get(i));
        }


    }
}
