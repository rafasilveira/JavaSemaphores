public class Road {
  int current;
  int counter;

  public Road() {
    this.current = 0;
    this.counter = 0;
  }

  void cross (int carId, String way) {
    System.out.println("Car " + carId + " started crossing the road: " + way);
    this.current = carId;
    try {
      Thread.sleep(1000);
    } catch (InterruptedException e) {
      e.printStackTrace();
    }
    this.counter++;
  }
}
