# Grass-Trim-AI  

Grass-Trim-AI, uydu görüntülerini analiz ederek çim büyümesini tespit eden ve izleyen bir projedir. Watershed algoritmasını kullanarak yolları, binaları, ağaçları ve çimleri birbirinden ayırır ve bunları farklı renklerle gösterir. Şu an proje sadece segmentasyon işlemini gerçekleştirirken, ilerleyen aşamalarda çimlerin uzama durumunu analiz ederek budama alarmı verecek şekilde geliştirilecektir.  

## Özellikler  
- **Watershed Segmentasyonu:** Yolları, binaları, ağaçları ve çimleri birbirinden ayırır.  
- **Renk Haritalama:** Segmentasyon sonucu bölgeleri farklı renklerle gösterir.  
- **Gelecek Geliştirmeler:** Çim büyümesini zaman içinde analiz edip budama alarmı verecek bir sistem geliştirilecektir.  

## Mevcut Çıktı  
Aşağıda mevcut segmentasyon sonuçlarından bir örnek bulunmaktadır:  


## Anıtkabir
![image](https://github.com/user-attachments/assets/4dac0c36-8d34-46f7-b569-0136648a18ce)
![image](https://github.com/user-attachments/assets/9738ff22-ca0e-45b4-9bec-37fcc8a158c2)


## Dolmabahçe Sarayı

![image](https://github.com/user-attachments/assets/e1fcfd54-e876-4f1c-a308-3b1574ad2c3d)
![image](https://github.com/user-attachments/assets/324c3093-f753-4249-b1be-18748f3d7ab5)


## Kullanılan Kütüphaneler  
- OpenCV  
- NumPy  
- Matplotlib (görselleştirme için)  

## Gelecek Planlar  
- Çim büyümesini tespit eden ve izleyen bir sistem eklemek.  
- Aşırı uzayan çimler için otomatik bir uyarı mekanizması geliştirmek.  
- Segmentasyon doğruluğunu artırmak için makine öğrenmesi teknikleri entegre etmek.  

## Kurulum ve Kullanım  
1. Depoyu klonlayın:  
   ```bash
   git clone https://github.com/kullanici-adiniz/grass-trim-AI.git
   cd grass-trim-AI
2. Bağımlılıkları yükleyin:
   ```bash
   pip install opencv-python matplotlib numpy
   
3. Segmentasyon scriptini çalıştırın:
   ```bash
   python main.py
