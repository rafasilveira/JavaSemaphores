import java.util.concurrent.*; 

public class Car extends Thread {
  Semaphore sem;
  int id;
  Road road;
  String way;

  public Car(Semaphore sem, int id, Road road, String way) {
    super("Car"+id); 
    this.sem = sem;
    this.id = id;
    this.road = road;
    this.way = way;
  }

  @Override
  public void run() { 

    System.out.println("Starting car " + id);
  }

  public void crossRoad() {
    try {
      System.out.println("Car " + this.id + " is waiting to cross");
      sem.acquire();
      System.out.println("Car " + this.id + " gets a permit");
      road.cross(this.id, this.way);
      Thread.sleep(1000);
      System.out.println("Car " + this.id + " releases the permit");
      System.out.println(road.counter + " cars have crossed\n");
      sem.release();

    } catch (InterruptedException e) {
      e.printStackTrace();
    }
  }
  
}
