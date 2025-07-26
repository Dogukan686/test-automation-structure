@echo off
echo [1/3] Docker imajı oluşturuluyor...
docker-compose build

echo [2/3] Docker container başlatılıyor ve testler çalıştırılıyor...
docker-compose up

echo [3/3] Testler tamamlandı. Allure raporu oluşturmak istiyorsan aşağıdaki komutu çalıştır:
echo.
echo allure serve reports/allure-results
pause
