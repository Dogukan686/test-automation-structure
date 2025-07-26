@echo off
echo ---------------------------------------------
echo Test Automation Project - Docker Build
echo ---------------------------------------------

docker buildx build --load -t test-automation .

echo ---------------------------------------------
echo Starting Test Container...
echo ---------------------------------------------

docker run --rm test-automation

echo ---------------------------------------------
echo Test Completed.
echo ---------------------------------------------
pause
