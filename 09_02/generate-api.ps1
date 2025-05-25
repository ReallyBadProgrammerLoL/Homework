# Удалить старые файлы (если есть)
Remove-Item -Recurse -Force .\endpoints\apis, .\endpoints\models, .\endpoints\router_init.py -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Force -Path .\endpoints

Remove-Item -Recurse -Force .\openapi-generator-output -ErrorAction SilentlyContinue

# Генерация из spec.yaml
docker run --rm -v ${PWD}:/app openapitools/openapi-generator-cli:latest-release generate `
    -i /app/spec.yaml -g python-fastapi -o /app/openapi-generator-output `
    --additional-properties=packageName=endpoints --additional-properties=fastapiImplementationPackage=endpoints

# Перемещение нужных файлов
Move-Item -Force .\openapi-generator-output\src\endpoints\apis .\endpoints\
Move-Item -Force .\openapi-generator-output\src\endpoints\models .\endpoints\
Move-Item -Force .\openapi-generator-output\src\endpoints\main.py .\endpoints\router_init.py

# Удаление временной папки
Remove-Item -Recurse -Force .\openapi-generator-output
