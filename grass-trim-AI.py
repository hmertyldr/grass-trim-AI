import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def segment_image(img):
    # Görüntüyü RGB'den HSV renk uzayına çevir
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # Binalar, yollar ve gri alanlar için maske
    lower_gray = np.array([0, 0, 50])
    upper_gray = np.array([180, 30, 255])
    mask_gray = cv.inRange(imgHSV, lower_gray, upper_gray)

    # Yeşil alanlar (ağaçlar, çalılıklar, çimenler) için maske
    lower_green = np.array([15, 1, 20])
    upper_green = np.array([180, 255, 110])
    mask_green = cv.inRange(imgHSV, lower_green, upper_green)

    # Evler için maske (213, 147, 134 RGB civarı)
    lower_house = np.array([0, 70, 120])
    upper_house = np.array([12, 255, 255])
    mask_houses = cv.inRange(imgHSV, lower_house, upper_house)

    # Segmentasyon görüntüsünü oluştur
    segmented_img = np.zeros_like(img)
    segmented_img[mask_gray != 0] = [200, 200, 200]  # Binalar ve yollar
    segmented_img[mask_green != 0] = [0, 255, 0]  # Yeşil alanlar
    segmented_img[mask_houses != 0] = [0, 0, 255]  # Evler

    return segmented_img, mask_gray, mask_green, mask_houses


def apply_watershed(img, mask_green):
    # Yeşil alanlar üzerinde daha iyi sonuç için ön işleme
    kernel = np.ones((3, 3), np.uint8)

    # Morfolojik işlemler (dilate ve erode) ile sure foreground ve background iyileştirildi
    sure_fg = cv.erode(mask_green, kernel, iterations=3)  # Öndeki nesneler
    sure_bg = cv.dilate(mask_green, kernel, iterations=3)  # Arkadaki nesneler
    unknown = cv.subtract(sure_bg, sure_fg)

    # Bağlı bileşenleri bul (markers)
    _, markers = cv.connectedComponents(sure_fg)

    # Bilinmeyen alanları 0 ile işaretle
    markers = markers + 1
    markers[unknown == 255] = 0

    # Watershed algoritmasını uygula
    markers = cv.watershed(img, markers)

    # Sonuçları renklendir (farklı yeşil tonları)
    img_watershed = np.zeros_like(img)
    img_watershed[markers == 1] = [0, 255, 0]  # Çimenler (açık yeşil)
    img_watershed[markers == 2] = [34, 139, 34]  # Çalılıklar (orta yeşil)
    img_watershed[markers > 2] = [0, 100, 0]  # Ağaçlar (koyu yeşil)

    return img_watershed, markers


if __name__ == "__main__":
    # Görüntüyü yükle
    imgPath = "Anitkabir.png"  # Resim dosya yolunu buraya ekle
    img = cv.imread(imgPath)

    # Segmentasyon işlemi
    segmented_img, mask_gray, mask_green, mask_houses = segment_image(img)

    # Watershed sadece yeşil alanlar üzerinde uygulanacak
    watershed_img, markers = apply_watershed(img, mask_green)

    # Son görüntüyü oluştur: evler, yollar ve yeşil alanlar birleşik
    combined_img = cv.addWeighted(segmented_img, 0.7, watershed_img, 0.3, 0)

    # Yarı saydam görüntüyü orijinal görüntü ile birleştir
    final_img = cv.addWeighted(combined_img, 0.8, img, 0.2, 0)

    # Sonuçları göster
    plt.figure(figsize=(12, 12))

    plt.subplot(221)
    plt.title("Segmentasyon (Binalar, Yollar, Yeşil Alanlar, Evler)")
    plt.imshow(cv.cvtColor(segmented_img, cv.COLOR_BGR2RGB))

    plt.subplot(222)
    plt.title("Binalar ve Yollar Maskesi")
    plt.imshow(mask_gray)

    plt.subplot(223)
    plt.title("Yeşil Alanlar Maskesi")
    plt.imshow(mask_green)

    plt.subplot(224)
    plt.title("Evler Maskesi")
    plt.imshow(mask_houses)

    plt.figure(figsize=(12, 8))
    plt.subplot(121)
    plt.title("Orijinal Görüntü")
    img_org = cv.imread(imgPath)
    plt.imshow(cv.cvtColor(img_org, cv.COLOR_BGR2RGB))

    plt.subplot(122)
    plt.title("Watershed Sonucu")
    plt.imshow(cv.cvtColor(final_img, cv.COLOR_BGR2RGB))

    plt.tight_layout()
    plt.show()
