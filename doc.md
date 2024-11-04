# 파이썬 준비

pyenv install --list
pyenv install 3.12.7
pyenv shell 3.12.7
pyenv versions

# 파이썬 가상환경

python -m venv venv
source venv/bin/activate

# Django

pip install django
django-admin startproject conf .

# MariaDB

sudo mysql
CREATE DATABASE road2gm DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE USER 'road2gm'@'%' IDENTIFIED BY 'w9BLfbbAxaygP2ZyX6EoaxBFsVSFCe5n';
FLUSH PRIVILEGES;
exit

# 패키지 설치

pip install mysqlclient
pip install django-model-utils
pip freeze > requirements.txt

# `conf/secret.json` 파일

```json
{
  "secretKey": "비밀키50자",
  "debug": true,
  "allowedHosts": [
    ".example.com",
    "192.168.56.1",
    ".localhost",
    "127.0.0.1",
    "[::1]"
  ],
  "database": {
    "default": {
      "ENGINE": "django.db.backends.mysql",
      "NAME": "road2gm",
      "USER": "road2gm",
      "PASSWORD": "비밀번호",
      "HOST": "127.0.0.1",
      "PORT": "3306",
      "OPTIONS": {
        "charset": "utf8mb4"
      }
    }
  }
}
```
# Git 저장소 준비

## 이미 원격 저장소가 있는 경우

```bash
git clone git@github.com-mairoo:mairoo/road2gm-django.git
```

## 로컬 저장소 만들고 원격 저장소에 연결

```bash
mkdir road2gm-react
cd road2gm-react
git init
```

다중 계정을 위해서 Host alias 지정 (github.com-mairoo)

```bash
git remote add origin git@github.com-mairoo:mairoo/road2gm-django.git
git remote -v
git branch --set-upstream-to=origin/main main
```

# fixtures 로드
```
python manage.py loaddata data.json
```