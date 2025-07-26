# 🧪 Test Otomasyon Case Çalışması

## 🎯 Proje Özeti

Bu proje, uçtan uca test otomasyonu yetkinliklerini göstermek amacıyla hazırlanmıştır.  
Postman, Selenium, Behave, Docker gibi araçlar kullanılarak test süreçleri tek bir yapıda birleştirilmiştir.

## 🚀 Proje Kapsamı

- Selenium ile kullanıcı arayüzü (UI) testleri
- Behave (BDD) ile senaryo tanımlama
- Postman mock server ile API testi
- API response verilerinin `.json` dosyalarına yazılması
- Hata durumunda otomatik ekran görüntüsü alma
- Allure ve HTML ile test raporlama
- Docker + Docker Compose ile testlerin izole çalıştırılması
- Paralel test koşumu (behave_parallel scripti ile)

---

## 🧱 Gereksinimler

- Python 3.10+
- pip
- Google Chrome / Firefox
- ChromeDriver / GeckoDriver
- Docker Desktop (varsayılan olarak Compose destekli)

---

## 🔧 Kurulum

```bash
pip install -r requirements.txt
```

---

## 🧪 Test Çalıştırma

### 1. Temel Test:
```bash
behave
```

### 2. HTML Raporlu Test:
```bash
behave -f html -o reports/test_report.html
```

---

## ⚙️ Allure ile Raporlama

### 1. Allure Sonuçlarını Üret:
```bash
behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results
```

### 2. Raporu Görüntüle:
```bash
allure serve reports/allure-results
```

> Not: Sisteminizde Allure CLI ve Java kurulu olmalıdır.

---

## 🐳 Docker Üzerinden Çalıştırma

```bash
docker-compose up --build
```

Bu komut, gerekli imajı oluşturur ve testleri konteyner içinde çalıştırır.

---

## 🔄 Paralel Test Koşumu

### 1. behave-parallel ile:
```bash
behave-parallel -n 4 -f pretty
```

### 2. Alternatif (run_parallel.py dosyası ile):
```bash
python behave_parallel/run_parallel.py
```

---

## 📂 Klasör Yapısı

```
.
├── features/               # .feature dosyaları
├── steps/                  # step tanımlamaları
├── behave_parallel/        # run_parallel.py dosyası
├── reports/                # HTML & Allure raporları
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── run_all_tests.bat
├── run_docker_tests.bat
```

---

Bu yapı, hem teknik değerlendirmelerde hem de gerçek projelerde yeniden kullanılabilir bir test otomasyon iskeleti sunar.
