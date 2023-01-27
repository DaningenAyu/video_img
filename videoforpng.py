"""
ーー個人ごとの変更点ーー
入力動画ファイルのパス(9行目)
出力画像ファイルのパス(27行目)
動画の向き反転(プログラム作者の環境では、上下左右反対で出力されたため)(24行目)
"""
import cv2

cap = cv2.VideoCapture('./videoforpng_in/IMG_5142.mp4') #動画ファイルのパスを設定
fps = int(cap.get(cv2.CAP_PROP_FPS)) #動画のFPSを取得
cap_all_f = cap.get(cv2.CAP_PROP_FRAME_COUNT) #動画の総フレームレートを取得

print('フレームレート:{}'.format(fps))
print('総フレームレート:{}'.format(int(cap_all_f)))
print('出力枚数:{}'.format(int(cap_all_f / 10)))

run = input('y/n:')

if(run == 'y'):
    i=1
    while (i <= cap_all_f):

        ret, img = ret, img = cap.read()       #画像の読み込み
        img_flip_udlr = cv2.flip(img,-1)       #動画を上下左右反転（0_上下反転,1_左右反転,-1_上下左右反転,通常にするにはこの行をコメントアウト）

        if(i % 10 == 0):
            cv2.imwrite('./videoforpng_out/' + str(i) +'.png',img_flip_udlr)  #出力する画像フォルダのパス+ファイル名+.png
            print(i)
        elif(i == cap_all_f):
            print(i)
        i += 1
        

    print('finish')