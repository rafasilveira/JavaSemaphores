from threading import Thread
from threading import Semaphore
from time import sleep


def traveler_thread(id, way, ways, bridge_sem, go_sems, done_sem, bridge):
  sleep(1)

  new_way = way - 1 if way >= 1 else way + 1
  print(f'Traveler {id} wants to go from {ways[way]} to {ways[new_way]}')

  go_sems[way].acquire()
  print(f'Traveler {id} got the green light and is waiting for the bridge')
  bridge_sem.acquire()
  print(f'Traveler {id} got the bridge and will start crossing')

  bridge.cross(way)

  bridge_sem.release()

  sleep(2)
  print(f'Traveler {id} crossed from {ways[way]} to {ways[new_way]} - counter: {bridge.counter}, hf_counter: {bridge.hf_counter}')
  done_sem.release()

  return


class Bridge:
  def __init__(self, bridge_sem, go_sems, done_sem):
    self.counter = 0
    self.hf_counter = 0
    self.bridge_sem = bridge_sem
    self.go_sems = go_sems
    self.done_sem = done_sem

  def cross(self, way):

    done_sem.acquire()

    if (way == 0):
      self.hf_counter += 1
      if (self.hf_counter <= 5):

        self.counter += 1
        sleep(1)

        if (self.hf_counter < 5):
          go_sems[0].release()
        else:
          self.hf_counter = 0
          go_sems[0].release()
          go_sems[1].release()

        return True
      
      else:
        self.hf_counter = 0
        return False

    if (way == 1):
      if (0 < self.hf_counter <= 5):
        return False
      self.counter += 1
      sleep(1)
      go_sems[0].release()
      go_sems[1].release()
      return True

    bridge_sem.release()
    return False


total_travelers = 9
travelers = []

ways = ["High Forest", "Great River"]

go_sems = [Semaphore(0) for way in ways]
bridge_sem = Semaphore(0)
done_sem = Semaphore(1)
bridge = Bridge(bridge_sem, go_sems, done_sem)


travelers.append(Thread(target=traveler_thread, args=[0, 1, ways, bridge_sem, go_sems, done_sem, bridge]))
travelers.append(Thread(target=traveler_thread, args=[1, 1, ways, bridge_sem, go_sems, done_sem, bridge]))
travelers.append(Thread(target=traveler_thread, args=[2, 1, ways, bridge_sem, go_sems, done_sem, bridge]))
travelers.append(Thread(target=traveler_thread, args=[3, 1, ways, bridge_sem, go_sems, done_sem, bridge]))
travelers.append(Thread(target=traveler_thread, args=[4, 0, ways, bridge_sem, go_sems, done_sem, bridge]))
travelers.append(Thread(target=traveler_thread, args=[5, 0, ways, bridge_sem, go_sems, done_sem, bridge]))
travelers.append(Thread(target=traveler_thread, args=[6, 0, ways, bridge_sem, go_sems, done_sem, bridge]))
travelers.append(Thread(target=traveler_thread, args=[7, 0, ways, bridge_sem, go_sems, done_sem, bridge]))
travelers.append(Thread(target=traveler_thread, args=[8, 0, ways, bridge_sem, go_sems, done_sem, bridge]))


for traveler in travelers:
  traveler.start()

bridge_sem.release()
go_sems[0].release()

for traveler in travelers:
  traveler.join()

print('Everyone finished crossing!')
