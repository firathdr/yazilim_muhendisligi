public class DoublyLinkedList {
    class Node{
        int data;
        Node previous;
        Node next;
        public Node(int data){
            this.data=data;
        }
        public int getData(){return data;}
        public Node getNext(){return next;}
        public Node getPrevious(){return previous;}

        public void setNext(Node newNext){
            next=newNext;
        }
        public void setPrevious(Node newPrevious){
            previous=newPrevious;
        }

    }
    Node head,tail=null;
    public void addNode(int data){
        Node newNode =new Node(data);
        if (head==null){
            head=tail=newNode;
            head.previous=null;
            tail.next=null;
        }
        else{
            tail.next=newNode;
            newNode.previous=tail;
            tail=newNode;
            tail.next=null;
        }
    }
    public void display(){
        Node current =head;
        System.out.println("DLLde bulunan degerler= ");

        while(current!=null){
            System.out.println(current.data);
            current=current.next;
        }
    }
    public boolean inIt(int data){
        Node current=head;
        while(current!=null){
            if (current.data==data){
                return true;
            }

            current=current.next;
        }
        return false;
    }
    public void delete(int data){
        Node current=head;
        if (inIt(data)){
            while(current.next!=null){
                if (current.next.data==data){

                    current.setNext(current.next.next);
                    current.next.next.previous=current;


                }

                current=current.next;
            }
        }
        else{
            System.out.println("silinmek istenen sayı listede bulunmamakta");
        }
    }
    public void addFirst(int data){
        Node w=head;
        Node x=tail;
        Node v=new Node(data);
        head=v;
        v.setNext(w);
        v.setPrevious(null);
        w.setPrevious(v);



    }
    public void removeLast(){
        tail=tail.previous;
        tail.next=null;
    }
    public void addAfter(int select,int insert){
        //select dedigimiz sectimiz sayıdan sonra next niyetine insert eklicez
        Node current=head;
        while(current!=null){
            if (current.data==select&current.next!=null){
                Node x =new Node(insert);
                x.setNext(current.next);
                current.next=x;
                x.setPrevious(current);


            }
            current=current.next;
        }



    }

    public static void main(String[] args) {
        DoublyLinkedList dlist=new DoublyLinkedList();
        dlist.addNode(4);
        dlist.addNode(6);
        dlist.addNode(9);
        dlist.addNode(2);
        dlist.addNode(12);
        dlist.addNode(45);
        dlist.addNode(1);
        dlist.display();
        dlist.addAfter(2,100);
        dlist.display();
        dlist.delete(100);
        dlist.display();



    }
}
