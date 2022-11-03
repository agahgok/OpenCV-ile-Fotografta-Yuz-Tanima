import cv2 #kütüphane ekleme işlemi
 
yuzprogramı = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #kullanacağmız hazır yüz bulma programı
 
resim = cv2.imread("ornek1.jpg") #resmimizi belirtme
 
griresim = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)#resmimizi griye donuştürme
 
program = yuzprogramı.detectMultiScale(griresim,1.3,3)#programı çalıştırma (taranacak resim,büyütme oranı,kontrol sayısı)
 
 
for (a,b,c,d) in program :
    cv2.rectangle(resim,(a,b),(a+c,b+d),(255,0,0),2) #burada bulduğumuz insan yüzlerini kare içide alma işlemini yapıyoruz
    #(yüzlerin gösterileceği resim,(köşe ayarlama)(köşe ayarlama),(karenin rengi),karenin kalınlığı)
 
cv2.imshow("kapatmak icin herhangi bir tusa basiniz",resim) #resmin son halini gösterme
 
cv2.waitKey(0)
cv2.destroyAllWindows() #herhangi bir tuşa basınca kapatmak için

#"haarcascade_frontalface_default.xml" ve incelenecek resim ayni dosya içerisinde olmali