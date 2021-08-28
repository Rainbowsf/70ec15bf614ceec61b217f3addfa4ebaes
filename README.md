# Django function modeling dashboard

function modeling dashboard


About project
   
   
   1. This webapplication renders functions (for example  y = sin(t), or y = log10(t)/t^5) with a given interval (in days) and step (in hours)
   2. t - unix time, end point = present, start point = end point - interval
   3. Matplotlib and numpy are used to simulate graphs. The process itself is performed through Celery asynchronous tasks.
   4. The number of functions that can be driven in is limited by the standard library + numpy (sin, log etc.)
   5. There is refresh button for recalculation of function graphs
   6. For faster loading of graph images, it was decided to put Redis as a caching system


![image](https://user-images.githubusercontent.com/81432272/131210103-9c9fa97a-aae6-49c4-82af-12f200c895c6.png)
![image](https://user-images.githubusercontent.com/81432272/131210200-1f6f6861-cda1-4bb9-95f4-67d10c6c63b5.png)

