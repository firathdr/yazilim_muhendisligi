import java.util.EmptyStackException;
import java.util.*;

public class ArrayStack <E> extends Stack<E> {
    protected int capacity;
    public static final int CAPACITY=1000;
    protected E S[];
    protected int top=-1;
    public ArrayStack(){
        this(CAPACITY);
    }
    public ArrayStack(int cap){
        capacity=cap;
        S=(E[]) new Object[capacity];
    }

    public int size(){
        return (top+1);
    }
    public boolean isEmpty(){
        return (top<0);
    }
    public E push(E element){
        S[++top]=element;

        return element;
    }
    public E top() throws EmptyStackException{
        if (isEmpty())
            throw new EmptyStackException();
        return S[top];
    }
    public E pop() throws EmptyStackException{
        E element;
        if (isEmpty())
            throw new EmptyStackException();
        element=S[top];
        S[top--]=null;
        return element;
    }
    public String toString(){
        String s;
        s="[";
        if(size()>0)s+=S[0];
        if (size()>1)
            for (int i=1;i<=size()-1;i++){
                s+=", "+S[i];
            }
        return s+"]";

    }
    public void status(String op,Object element){
        System.out.print("--------->"+op);
        System.out.println(", returns "+size());
        System.out.print("result: size= "+size());
        System.out.println(", stack: "+this);

    }

    public static void main(String[] args) {
        Object o;
        ArrayStack<Integer> arrayStack=new ArrayStack<Integer>();
        arrayStack.status("new arraystack",null);
        arrayStack.push(7);
        arrayStack.status("A.push(7)",null);

        o=arrayStack.pop();
        arrayStack.push(12);
        arrayStack.push(87);
        arrayStack.push(12);
        arrayStack.push(87);
        arrayStack.push(12);

        arrayStack.status("poppeddd",o);
        String result=arrayStack.toString();
        System.out.println(result);
    }







}
