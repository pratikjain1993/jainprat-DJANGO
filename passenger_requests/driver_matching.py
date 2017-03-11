from driver_request.models import Driver_Request
from testing.models import User
from passenger_requests.models import Trip_Request
from geopy.distance import vincenty
from driver import send_pushnotif

def driver_matching(passenger_id):
    req = Trip_Request.objects.get(request_id=passenger_id)
    passenger_source =  (float(req.source_lat),float(req.source_long))
    passenger_destination = (float(req.destination_lat),float(req.destination_long))


    try:
        for driver in Driver_Request.objects.all():
            driver_source = (float(driver.source_lat), float(driver.source_long))
            driver_destination = (float(driver.destination_lat), float(driver.destination_long))
            source_distance = (vincenty(driver_source, passenger_source).miles)/1.6094
            destination_distance = (vincenty(driver_destination, passenger_destination).miles)/1.6094
            if (source_distance <= 2 and destination_distance <= 2):
                s = send_pushnotif(driver.player_id, passenger_id)
                print s
        return ("Notifications Sent")
    except:
        return ("Error")



                #if(driver_source.distance(passenger_source)<= 2 and driver_destination.distance(passenger_destination)<=2):
        #s = driver(passenger_id)






