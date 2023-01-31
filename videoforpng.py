"""
ーー個人ごとの変更点ーー
入力動画ファイルのパス（動画ファイルのパスを指定（拡張子まで入れる））(10行目)
出力画像ファイルのパス(画像を入れたいフォルダを指定)(11行目)
動画の向き反転(プログラム作者の環境では、上下左右反対で出力されたため)(15行目)
"""
import cv2
import sys

in_path = './videoforpng_in/IMG_5146.MOV'
out_path = './videoforpng_out/'

def img_fl(image):
    #反転を行う場合は、コメントアウトを外し、引数２を変更
    #image = cv2.flip(image,-1)#動画を上下左右反転（0_上下反転,1_左右反転,-1_上下左右反転,通常にするにはこの行をコメントアウト）
    return image


#処理の準備
cap = cv2.VideoCapture(in_path) #動画ファイルのパスを設定
if cap.isOpened():
    fps = int(cap.get(cv2.CAP_PROP_FPS)) #動画のFPSを取得
    cap_all_f = cap.get(cv2.CAP_PROP_FRAME_COUNT) #動画の総フレームレートを取得

    print('フレームレート:{}'.format(fps))
    print('総フレームレート:{}'.format(int(cap_all_f)))
    print('最大出力枚数:{}'.format(int(cap_all_f / 10)))

    ret, img = cap.read()
    cv2.imwrite(out_path + 'sample.png',img_fl(img))
    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)#動画再生位置を0フレーム目にset
    print('\nsample画像を出力しました')   
else:
    print('画像が読み込めません')
    sys.exit


#処理開始
run = input('続けて出力しますか？ y/n:')
if(run == 'y'):
    j = 1
    num = 1
    for i in range(1,int(cap_all_f)):

        ret, img = ret, img = cap.read()       #画像の読み込み
        img_flip = img_fl(img)
        blur = cv2.Laplacian(img_flip, cv2.CV_64F).var()   #ブレ検知(値が小さいほどブレ画像)
        print(i,blur)

        if(blur > 150):
            if(j % 10 == 0):
                cv2.imwrite(out_path + str(num) +'.png',img_flip)  #出力する画像フォルダのパス+ファイル名+.png
                num += 1 
            j+=1 

print('finish')
