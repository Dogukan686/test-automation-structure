@echo off
echo --------------------------------------------
echo Test Automation Project - Docker Build & Run
echo --------------------------------------------

:: Docker image build (buildx destekli ve local yükleme)
docker buildx build --load -t test-automation .

IF %ERRORLEVEL% NEQ 0 (
    echo [HATA] Docker image olusturulamadi.
    pause
    exit /b %ERRORLEVEL%
)

:: Docker container çalıştır
docker run --rm test-automation

IF %ERRORLEVEL% NEQ 0 (
    echo [HATA] Docker container icinde testler basarisiz.
    pause
    exit /b %ERRORLEVEL%
)

echo --------------------------------------------
echo Testler Docker container icinde basariyla calistirildi.
echo --------------------------------------------
pause