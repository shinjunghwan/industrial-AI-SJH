
import glob
import cv2
import numpy as np
images = glob.glob('dataset/*.jpg') ##이미지 리스트 총 17개 샘플
print(len(images))
for pivot_cnt in range(len(images)) :
    pcb_cnt = 0
    for comp_cnt in range(len(images)) :
        if pivot_cnt < comp_cnt :
            img_pivot = cv2.imread(images[pivot_cnt])
            img_comp = cv2.imread(images[comp_cnt])
            detector = cv2.ORB_create(200)
            kps0, fea0 = detector.detectAndCompute(img_pivot, None)
            kps1, fea1 = detector.detectAndCompute(img_comp, None)
            matcher = cv2.BFMatcher_create(cv2.NORM_HAMMING, False)
            matches = matcher.match(fea0, fea1)
            pts0 = np.float32([kps0[m.queryIdx].pt for m in matches]).reshape(-1, 2)
            pts1 = np.float32([kps1[m.trainIdx].pt for m in matches]).reshape(-1, 2)
            H, mask = cv2.findHomography(pts0, pts1, cv2.RANSAC, 10.0)
            match_cnt = 0
            for i, m in enumerate(matches):
                if mask[i]:
                    match_cnt = match_cnt + 1
            if match_cnt >= 50:
                pcb_cnt = pcb_cnt + 1
                cv2.imshow('img_pivot', img_pivot)
                cv2.imshow('img_comp', img_comp)
                cv2.waitKey(0)
                continue
    print(pivot_cnt)
    print("pcb_cnt")
    print(pcb_cnt)