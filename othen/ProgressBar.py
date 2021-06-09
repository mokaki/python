from rich.progress import track
import  time
 
for step in track(range(30)):
    print('早起Python')
    time.sleep(0.5)
