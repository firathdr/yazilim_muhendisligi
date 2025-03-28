public class BinaryTree {
    public class BTNode<T>{
        public BTNode<T> left;
        public BTNode<T> right;
        public T value;
        public  BTNode(T value,BTNode<T> left,BTNode<T> right){
            this.left=left;
            this.right=right;
            this.value=value;
        }
    }
    public abstract class BinarySearchTree<T extends Comparable<T>>{
        private BTNode<T> root;
        public BinarySearchTree(){}

        public BinarySearchTree(BTNode<T> root){
            this.root=root;
        }

        public BTNode<T> getRoot(){
            return root;
        }
        public BTNode<T> find(BTNode<T> node,T value){
            if (node==null||node.value==value)
                return node;
            else if (value.compareTo(node.value)<0)
                return find(node.left,value);
            else
                return find(node.right,value);
        }
        public boolean contains(T value){
            return find(root,value)!=null;
        }
        public void add(T value){
            add(root,value);
        }
        private void add(BTNode<T> node,T value){
            if (root==null){
                root=new BTNode<>(value,null,null);
                return;
            }
            if (value.compareTo(node.value)<0){
                if (node.left==null)
                    node.left=new BTNode<>(value,null,null);
                else
                    add(node.left,value);

            } else if (value.compareTo(node.value)>0) {
                if (node.right==null)
                    node.right=new BTNode<>(value,null,null);
                else
                    add(node.right,value);


            }
            else throw new RuntimeException("eleman agacta mevcut");


        }

        protected abstract Object clone() throws CloneNotSupportedException;
        public  BTNode<T> successor(T value){
            BTNode<T> node= find(getRoot(), value);

            if(node == null || node.right == null){
                return null;
            }

            node = node.right;

            while (node.left != null){
                node = node.left;
            }
            return node;
        }
        public  BTNode<T> predecessor(T value){
            BTNode<T> node= find(getRoot(), value);

            if(node == null || node.left == null){
                return null;
            }

            node = node.left;

            while (node.right != null){
                node = node.right;
            }
            return node;
        }
        public  BTNode<T> findParent(BTNode<T> node){
            BTNode<T> parent = getRoot();

            if(node==parent)
                return null;

            while(parent.right.value.compareTo(node.value)!=0 && parent.left.value.compareTo(node.value)!=0){
                if((parent.value.compareTo(node.value)>0)){
                    parent=parent.left;
                }
                else if(parent.value.compareTo(node.value)<0){
                    parent=parent.right;
                }
            }
            return parent;
        }
    }

}

