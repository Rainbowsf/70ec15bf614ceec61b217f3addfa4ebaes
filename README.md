# Django function modeling dashboard

function modeling dashboard


About project
   
   
   1. This webapplication renders functions (for example  y = sin(t), or y = log10(t)/t^5) with a given interval (in days) and step (in hours)
   2. Matplotlib and numpy are used to simulate graphs. The process itself is performed through Celery asynchronous tasks.
   3. The number of functions that can be driven in is limited by the standard library + numpy (sin, log etc.)
   4. For faster loading of graph images, it was decided to put Redis as a caching system


