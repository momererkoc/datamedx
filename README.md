# Ön İşlemler

**Proje kapsamında, bize teslim edilen veri seti aşağıdaki adımlara tabii tutulmuştur:**

 1. **Sütun İsimlerinin Yeniden Adlandırılması:** Veri setindeki orijinal sütun isimleri, daha anlaşılır ve açıklayıcı hale getirilmiştir. Bu sayede hem okunabilirlik artmış hem de analiz süreci kolaylaştırılmıştır.
    
 2. **Diyabet Sınıflandırması:** `e10` ve `e11` sütunları, diyabet hastalığının varlığını gösteren kodları içerdiğinden, bu sütunlar birleştirilmiş ve diyabetin varlığını temsil eden ikili (binary) bir sütun oluşturulmuştur. Bu dönüşüm, sınıflandırma modelleri için veri setini daha uygun hale getirmiştir.
    
 3. **Tarih Verisinin Standardizasyonu:** Saat bilgisi içermeyen eski tarih sütunu veri setinden çıkarılmış ve yerine zaman bilgisi de içeren, analizlerde zaman serisi işlemlerine uygun **`datetime`** formatında bir sütun eklenmiştir.
    
 4. **Veri Formatı ve Altyapı Uyarlaması:** Hazırlanan veri seti, kolay erişim ve analiz için **CSV formatına** dönüştürülmüş ve daha verimli veri yönetimi sağlamak amacıyla **MySQL veritabanına** aktarılmıştır.
    
 5. **Veri Temizliği ve Normalizasyon:** Bazı metin tabanlı sütunlar (örneğin ilaç bilgileri), büyük/küçük harf duyarlılığını ortadan kaldırmak, özel karakterleri temizlemek ve tutarlı karşılaştırmalar yapılabilmesini sağlamak için normalize edilmiştir.
    
 6. **İlaç Bilgileriyle Zenginleştirme:** `all_medications` sütunundaki hasta ilaç bilgileri, harici bir ilaç veri tabanı ile eşleştirilmiş; her hasta kaydı için ilgili **kategori bilgisi** (`Category_2`, örneğin: _Antitrombotikler_, _Ağrı Kesici / Ateş Düşürücüler_) ve **barkod bilgisi** (`Barcode`) ek sütunlar olarak veri setine dahil edilmiştir. Barkod bilgisi sayesinde, hastaların kullandığı ilaçlar ile tanıları arasındaki ilişkinin daha ayrıntılı incelenmesi mümkün hale gelmiş; ayrıca bu barkodlar üzerinden, Sağlık Bakanlığı'nın açık veri servisleri (API'leri) aracılığıyla ilacın endikasyonları, etken maddesi, kontrendikasyonları ve yan etkileri gibi tüm klinik detayların programatik olarak çekilmesi sağlanabilir hale gelmiştir.
