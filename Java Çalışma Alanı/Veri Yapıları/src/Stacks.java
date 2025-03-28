public class Stacks<T> {
    private T[] dizi;
    private int es;
    public Stacks(){
        dizi=(T[]) new Object[10];
        es=0;
    }
    public Stacks(int es){
        dizi=(T[]) new Object[es];
        es=0;
    }
    public void push(T eleman){
        if (es==dizi.length)
            throw new RuntimeException("Stack overflow");
        dizi[es++]=eleman;
    }
    public T pop(){
        if (es==0)
            throw new RuntimeException("Stack overflow");
        return dizi[--es];
    }
    public T peek(){
        if(es==0)
            throw new RuntimeException("Stack overflow");
        return dizi[es-1];
    }
    public boolean isEmpyt(){
        return es==0;
    }
    public void print(){
        int current =0;
        while(current<dizi.length){
            System.out.println(dizi[current]);
            current++;
        }
    }

    public static void main(String[] args) {
        Stacks<Integer> st=new Stacks<>(7);
        st.push(4);
        st.push(6);
        st.push(9);
        st.push(2);
        st.push(12);
        st.push(45);
        st.push(1);


        st.print();
        System.out.println("***************");
        System.out.println(st.pop());//pop son ekleneni çıkartır aynı zamanda return degeri vardır

        System.out.println(" peek kodu = "+ st.peek());
        st.print();
    }

}
