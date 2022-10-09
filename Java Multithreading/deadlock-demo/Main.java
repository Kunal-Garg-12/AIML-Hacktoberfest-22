class Resource{
    String resource;
    Resource(String resource){
        this.resource=resource;
    }
}
class T1 extends Thread{
    Resource r1,r2;
    T1(Resource r1,Resource r2){
        this.r1=r1;
        this.r2=r2;
    }
    public void run(){  
        synchronized (r1){  
          System.out.println("Thread 1: locked resource 1");  
          try { Thread.sleep(100);} catch (Exception e) {}  
          synchronized (r2) {  
            System.out.println("Thread 1: locked resource 2");  
          }  
        }  
    }
}
class T2 extends Thread{
    Resource r1,r2;
    T2(Resource r1,Resource r2){
        this.r1=r1;
        this.r2=r2;
    }
    public void run(){  
        synchronized (r2){  
          System.out.println("Thread 2: locked resource 2");  
          try { Thread.sleep(100);} catch (Exception e) {}  
          synchronized (r1) {  
            System.out.println("Thread 2: locked resource 1");  
          }  
        }  
    }
}
public class Main{
  public static void main(String[] args){  
    Resource resource1 = new Resource("Printer"); 
    Resource resource2 = new Resource("Scanner"); 
    // t1 tries to lock resource1 then resource2  
    T1 t1 = new T1(resource1, resource2);  
    // t2 tries to lock resource2 then resource1  
    T2 t2 = new T2(resource1, resource2);
    t1.start();  
    t2.start();  
  }  
} 

