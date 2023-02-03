import cv2
import os


cap = cv2.VideoCapture('./videoforpng_in/sample.mp4') #動画ファイルのパスを設定
fps = int(cap.get(cv2.CAP_PROP_FPS)) #動画のFPSを取得
cap_all_f = cap.get(cv2.CAP_PROP_FRAME_COUNT) #動画の総フレームレートを取得

#もしvideoforpng_outのフォルダーがなかったら
outfile_path = "./videoforpng_out/"
if os.path.exists(outfile_path):
    print(outfile_path,"フォルダーが存在します。処理を実行します。")
else:
    print(outfile_path,"フォルダーが存在しないため新しくフォルダーを作成しました。")
    print("処理を実行します。")
    os.makedirs(outfile_path)



print('動画のフレームレート:{}'.format(fps))
print('出力時の画像枚数:{}'.format(int(cap_all_f)))
run = input('y/n:')

if(run == 'y'):
    i=1
    while (i <= cap_all_f):

        ret, img = ret, img = cap.read()       #画像の読み込み
        img_flip_ud = cv2.flip(img,-1)       #動画を上下左右反転（0_上下反転,1_左右反転,-1_上下左右反転）

        cv2.imwrite('./videoforpng_out/' + str(i) +'.png',img_flip_ud)  #出力する画像フォルダのパス+ファイル名+.png
        if(i % 10 == 0):
            print(i)
        elif(i == cap_all_f):
            print(i)
        i += 1
        

    print('finish')
