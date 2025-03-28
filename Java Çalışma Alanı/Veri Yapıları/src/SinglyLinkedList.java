public class SinglyLinkedList<T> {
    class Node{
        int data;
        Node next;
        public Node(int data){
            this.data=data;
            this.next=null;
        }
        public void setNext(Node newNext){
            next=newNext;
        }
        public void setData(int data){
            this.data=data;
        }

    }
    public Node head=null;
    public Node tail=null;
    public void addNode(int data){
        Node newNode=new Node(data);
        if(head==null){
            head=newNode;
            tail=newNode;

        }
        else {
            tail.next=newNode;
            tail=newNode;
        }

    }

    public void display(){
        Node current=head;
        if (head==null){
            System.out.println("list is empty");
            return;
        }
        System.out.println("singly linked list: ");
        while(current!=null){
            System.out.println(current.data+" ");
            current=current.next;
        }
        System.out.println();
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

                }

                current=current.next;
            }
        }
        else{
            System.out.println("silinmek istenen sayı listede bulunmamakta");
        }
    }

    public static void main(String[] args) {
        SinglyLinkedList liste=new SinglyLinkedList();
        liste.addNode(4);
        liste.addNode(6);
        liste.addNode(9);
        liste.addNode(2);
        liste.addNode(12);
        liste.addNode(45);
        liste.addNode(1);

        liste.display();
        System.out.println(liste.inIt(9));
        liste.delete(9);
        liste.display();
    }
}

