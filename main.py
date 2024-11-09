
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
old = DataManager()
new = FlightSearch(old)
comparison_list = FlightData(new, old)
comparison_list.compare()
notify = NotificationManager()
if comparison_list.aler >= 1:
  notify.send_message(comparison_list.message)
  print("a")
