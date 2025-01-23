import schedule
import time
import random
import os
from py_araclar.araclar import create_tweet, upload_media ,get_video_properties, get_frame



def post_tweet():
    j = random.randint(30, 3852)*10 # 10 framede bir aldığım için random sayıyı 10un katında toplam frame sayısının 10 katı olarak seçmeliyim
    image_path = f"frameler\\frame{j}.jpg"
    
    try:
        media_id = upload_media(image_path)
        create_tweet(f"Recep İvedik - Frame {j} of 152520", media_id)
        print(f"Tweet posted with image {image_path}")
    except Exception as e:
        print(f"Error posting tweet with image {image_path}: {e}")
  

schedule.every(16).minutes.do(post_tweet) #16 dakikada bir post atmak üzere ayarlandı

if __name__ == "__main__":
    video_path = r"C:\Users\fıro\Desktop\bot\recep.mp4"

    
    while True:
        schedule.run_pending()
        time.sleep(1)  


