# Proje Arayüz Sözleşmesi (Contract)

Bu proje "Contract-First" prensibiyle geliştirilmektedir. `main` branch üzerinde bulunan fonksiyon imzaları (isimler, parametreler ve dönüş tipleri) ve veri yapıları tüm modüllerin entegrasyonu için sabittir.

## Kurallar

1. **Hard-code Yasaktır:** Hiçbir düğüm adı, süre veya kapasite değeri koda doğrudan yazılamaz. Her şey `data/test_scenario.json` formatına uygun dış veri dosyalarından okunmalıdır.
2. **Imzalar Değiştirilemez:** `src/models.py` ve `src/core.py` içindeki tip belirlemeleri (`Type Hinting`) kesindir.
3. **Branch Mantığı:** Kimse `main` branch'e doğrudan kod yazamaz. Herkes kendi görevini `feature/gorev-adi` şeklinde yeni bir branch açarak yapacak ve bitince Pull Request (PR) gönderecektir.
4. **Mocking:** Bir modül henüz bitmemişse, hata fırlatmak yerine sahte (mock) değerler döndürülmelidir (Örn: Dijksta'nın geçici olarak boş liste döndürmesi gibi) ki testler engellenmesin.
