import java.util.concurrent.*; 

class Main {
  public static void main(String args[]) throws InterruptedException  
  { 
    Road road = new Road();
    Car[] cars = new Car[15];
    String[] ways = {"North to South", "East to West", "South to North", "West to East"};

    /**
     *          North
     *    West    x    East
     *          South
     * 
     * North to South
     * East to West
     * South to North
     * West to East
     */

    Semaphore sem = new Semaphore(1); 

    for (int i = 0; i < cars.length; i++) {
      cars[i] = new Car(sem, i, road, ways[i%4]);
    }

    for (int i = 0; i < cars.length; i++) {
      cars[i].start();
      Thread.sleep(10);
    }

    for (int i = 0; i < cars.length; i++) {
      cars[i].crossRoad();
      Thread.sleep(10);
    }

    for (int i = 0; i < cars.length; i++) {
      cars[i].join();
    }

  } 
}