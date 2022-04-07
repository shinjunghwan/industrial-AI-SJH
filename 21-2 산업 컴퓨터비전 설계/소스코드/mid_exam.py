###중간 프로젝트
###주제 : 여러개의 PCB사진을 비교하여 같은 종류의 PCB로 분류
##INPUT : 여러개의 샘플 PCB사진
##OUTPUT : PCB종류 수와 번호 배열 리스트
import glob
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

images = glob.glob('dataset/*.jpg') ##이미지 리스트 총 17개 샘플
sharpening_mask = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]) ##샤프닝 마스크
kernel3 = np.ones((5, 5), np.uint8)  ##커널 생성 3,5,7중 적정값 선택
kernel5 = np.ones((9, 9), np.uint8)  ##커널 생성 3,5,7,9 중 적정값 선택

num_g = 0 # PCB 종류 카운트

for img_pivot in range(images) :
    num_g = num_g + 1
    piv_img = cv2.resize(cv2.imread(images[img_pivot], 0), (512, 512)) ##이미지 비교를 위해 512 * 512 사이즈 통일
    s_piv_img = cv2.filter2D(piv_img, -1, sharpening_mask) ##샤프닝
    _, s_piv_img = cv2.threshold(s_piv_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) ##이진화
    stm_piv_img = cv2.dilate(s_piv_img, kernel3, iterations=1) ##모폴로지 연산 팽창
    stm_piv_img = cv2.morphologyEx(stm_piv_img, cv2.MORPH_OPEN, kernel5, iterations=3) ##모폴로지 연산 오프닝
    num_c = 0
    for img_comp in range(images) :
        if img_comp > img_pivot:
            cmp_img = cv2.resize(cv2.imread(images[img_comp], 0), (512, 512)) ##비교 이미지 동일하게 연산(이하 동일)
            s_cmp_img = cv2.filter2D(cmp_img, -1, sharpening_mask)
            _, s_cmp_img = cv2.threshold(s_cmp_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            stm_cmp_img = cv2.dilate(s_cmp_img, kernel3, iterations=1)
            stm_cmp_img = cv2.morphologyEx(stm_cmp_img, cv2.MORPH_OPEN, kernel5, iterations=3)
            score, diff = ssim(stm_piv_img, stm_cmp_img, full=True) ##기준 이미지와 비교 이미지 동일성 비교

            print(images[img_pivot])
            print(images[img_comp])
            print(f"Similarity : {score:.5f}")
            if score >= 0.65: ##65%이상은 같은 PCB로 인식
                cv2.imshow('stm_piv_img', stm_piv_img)
                cv2.imshow('stm_cmp_img', stm_cmp_img)
                #images.remove(images[img_comp]) ##인식한 PCB는 리스트에서 삭제
                images.pop(img_comp)  ##인식한 PCB는 리스트에서 삭제
                cv2.waitKey(0)
                continue

print(num_g)