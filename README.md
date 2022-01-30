# Litter_Detection
It is a frequent sight to see people throwing banana peels, tin cans, plastic covers and bottles. Many people while using  roads spit there and throw wrappers and other wastes on the roadsides. It is disappointing to see the laziness and indifference of people ruining our environment.

Birds and Animals consume these waste products, confusing them for food. They don't survive.

As responsible citizens, we propose the creation of a system that automatically detects cases of littering, allowing the authorities in charge to take necessary action. 

Our system uses the wonders of modern computer vision technology to detect cases of littering from camera video streams. It uses object detection to detect objects that are likely to be trash.  It then logs these instances of littering and creates a report in a human readable format. 

This report can then be forwarded to the appropriate government authorities. These authorities can then take appropriate action against the perpetrators according to the law of the land. Much like car speeding limits, this may cause lawbreakers to think twice before littering. Our environment benefits.

We use the OpenCV library for object detection. Python is used for the core of the project. We have a database of images of items that are likely to be litter. Tin cans, plastic bottles, plastic bags, etc. More objects can be added as the system gains adoption.

We use OpenCV's object detection feature to compare objects in the input stream with objects from the database. When a positive appears, it is logged along with the time and place.

These logs can eventually be turned into human readable reports to be forwarded to the appropriate authorities.

We hope that with careful use of this system, we can reduce the effects of the menace to environment that is the problem of littering. Already, speeding detection systems installed on busy roads reduce death tolls and accidents. This is a successful example of the use of computer vision on a large scale to save lives. Our solution aspires to emulate this success to the problem of littering.

![People_Littering](https://user-images.githubusercontent.com/90915273/151687852-d2639baa-c4ea-46c6-a0e5-b4576b9cf25d.png)
