# 🧪 Test Otomasyon Case Çalışması

## 🎯 Proje Özeti

Bu proje, yazılım test mühendisi adayları için hazırlanmış uçtan uca bir otomasyon test case çalışmasıdır.  
Projede aşağıdaki yetenekler ve teknolojiler uygulanmıştır:

- ✅ Selenium ile UI test otomasyonu
- ✅ Behave (BDD) ile insan okunabilir test senaryoları
- ✅ Postman ile API mock testi
- ✅ API response’larını `.json` dosyasına yazma
- ✅ Dinamik tarayıcı seçimi (Chrome / Firefox)
- ✅ Test başarısız olursa otomatik ekran görüntüsü alma
- ✅ HTML ve Allure ile test raporlama
- ✅ Docker & Docker Compose desteği
- ✅ Python scripti ile paralel test koşumu (behave_parallel klasörü)

Kurulum, çalıştırma ve detaylar aşağıda adım adım açıklanmıştır. 👇


# E2E Test Automation Case Study

Bu proje, Yazılım Test Mühendisi teknik değerlendirme görevinde belirtilen 8 adımı içeren uçtan uca test otomasyonu çalışmasıdır.

## İçerik

- ✅ UI Test Otomasyonu (Selenium)
- ✅ API Testi (Mock Server)
- ✅ BDD Yapısı (Behave)
- ✅ Tarayıcı Parametrizasyonu (Chrome / Firefox)
- ✅ Test Raporlama
- ✅ Hata Anında Ekran Görüntüsü
- ✅ Docker & Docker Compose
- ✅ Paralel Test Koşumu

## Gereksinimler

- Python 3.10+
- Google Chrome / Firefox
- ChromeDriver / GeckoDriver
- pip

## Kurulum

```bash
pip install -r requirements.txt
```

## Test Çalıştırma

```bash
behave
```

## Docker Kullanımı

```bash
docker-compose up --build
```

## Paralel Koşum

```bash
behave-parallel -n 4
```

## İletişim

Herhangi bir sorunda iletişime geçebilirsiniz.


---

## Test Raporları

### Behave (HTML Formatı)
```bash
behave -f html -o reports/test_report.html
```

### Allure ile Raporlama
1. Aşağıdaki komutla allure sonuçlarını oluştur:
```bash
behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results
```

2. Ardından Allure raporunu başlat:
```bash
allure serve reports/allure-results
```

> Not: Allure CLI sistemine kurulu olmalıdır.


---

## Docker Kullanımı

### Build ve Test Çalıştırma

```bash
docker-compose up --build
```

Bu komut, otomasyon testlerini konteyner içinde başlatır.


---

## Paralel Test Koşumu

### Behave-Parallel ile

Testleri aynı anda birden fazla çekirdekte çalıştırmak için:

```bash
behave-parallel -n 4 -f pretty
```

- `-n 4` → 4 paralel thread kullanır
- Test dosyalarını otomatik olarak böler ve paralel yürütür

> Not: Her `.feature` dosyası ayrı thread'de yürütülür, step dosyaları ortak kullanılır.


---

## Paralel Test Koşumu (behave_parallel klasörü ile yerel çözüm)

`pip install behave-parallel` çalışmadığında, bu proje içinde yer alan `behave_parallel/run_parallel.py` dosyasını kullanarak paralel test çalıştırabilirsiniz.

### Kullanım:
```bash
python behave_parallel/run_parallel.py
```

- Bu script, `features/` klasöründeki tüm `.feature` dosyalarını aynı anda çalıştırır
- Varsayılan olarak 4 thread ile çalışır (isteğe göre arttırılabilir)

---
