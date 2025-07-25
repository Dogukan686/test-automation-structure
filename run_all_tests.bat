@echo off
echo [1] Virtual Environment varsa aktifleştiriliyor...
call venv\Scripts\activate.bat

echo [2] Gerekli pip paketleri yükleniyor...
pip install -r requirements.txt

echo [3] Testler çalıştırılıyor...
python behave_parallel\run_parallel.py

echo [4] Allure raporu oluşturuluyor...
allure generate reports/allure-results --clean -o reports/allure-report
allure open reports/allure-report

pause
