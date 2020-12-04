public class Road {
  int current;
  int counter;

  public Road() {
    this.current = 0;
    this.counter = 0;
  }

  void cross (int carId, String way) {

    // if (this.current == 0) {
      // System.out.println("Road is available!");
      System.out.println("Car " + carId + " started crossing the road: " + way);
      this.current = carId;
      try {
        Thread.sleep(1000);
      } catch (InterruptedException e) {
        e.printStackTrace();
      }
      // this.current = 0;
      this.counter++;
      // System.out.println("Car " + carId + " finished crossing the road");
      // System.out.println(this.counter + " cars have crossed.\n");
    // }

    // System.out.println("Road is busy! Car " + carId + " must wait for car " + this.current);
  }
}
