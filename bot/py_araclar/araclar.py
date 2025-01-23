import requests as rq
from requests_oauthlib import OAuth1
import py_araclar.api as api 
import cv2
import os

API_KEY = api.API_KEY
API_SECRET = api.API_SECRET_KEY
ACCESS_TOKEN = api.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = api.ACCESS_TOKEN_SECRET
BEARER_TOKEN = api.BEARER_TOKEN


auth = OAuth1(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
    "Content-type": "application/json"
}


def create_tweet(text, media_id=None):#tweetin oluşturulması 
    payload = {
        "text": text
        }
    if media_id:
        payload["media"] = {"media_ids": [media_id]}
        

    
    response = rq.post(
        "https://api.twitter.com/2/tweets",
        auth=auth,
        json=payload
    )
    if response.status_code == 201:
        print('Tweet başarıyla gönderildi!')
        print(response.json())
    else:
        print('Tweet gönderilirken hata oluştu:', response.status_code)
        print(response.text)


def upload_media(media_path):
    with open(media_path, 'rb') as image_file:
        files = {"media": ("media.jpg", image_file, "image/jpeg")}
        response = rq.post(
            "https://upload.twitter.com/1.1/media/upload.json",
            auth=auth,
            files=files
        )
        if response.status_code == 200:
            return response.json()['media_id_string']
        else:
            print(f"Medya yüklenirken hata oluştu Hata kodu: {response.status_code}")
            print(response.text)
            return None
        
def get_video_properties(video_path):
    cap = cv2.VideoCapture(video_path)

    video_süre_sn = cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS)

    print(f"Video süresi:"
          f"\n\t{video_süre_sn//3600:.1f} saat "
          f"\n\t{(video_süre_sn%3600)//60:.1f} dakika "
          f"\n\t{video_süre_sn%60:.1f} saniye")

    print(f"Videonun FPS değeri: {cap.get(cv2.CAP_PROP_FPS)}")
    print(f"Videodaki toplam kare sayısı: {cap.get(cv2.CAP_PROP_FRAME_COUNT)}")
    print(f"Videonun kare yüksekliği: {cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}")
    print(f"Videonun kare genişliği: {cap.get(cv2.CAP_PROP_FRAME_WIDTH)}")
    
       
    cap.release()

    
def get_frame(video_path,de):
    cap = cv2.VideoCapture(video_path)

    
    currentFrame=0

    while(True):
        ret,frame = cap.read()

        if ret:
            name='./frameler/frame'+str(currentFrame)+".jpg"
            print("Oluşturuluyor..." + name)

            if currentFrame % de==0 :
                cv2.imwrite(name,frame)

            currentFrame+=1
        else:
            break


    cap.release()
    cv2.destroyAllWindows()
        


