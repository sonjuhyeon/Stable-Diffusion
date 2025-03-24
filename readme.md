# Stable Diffusion 이미지 생성 API (FastAPI 기반)

이 프로젝트는 Stable Diffusion 모델을 활용해 프롬프트 기반 이미지를 생성하는 간단한 FastAPI 서버입니다.  
프롬프트를 입력하면 캐릭터 이미지를 생성하고, 이미지 파일로 저장합니다.

---

## 프로젝트 실행 방법

### 1. 가상환경 생성
```bash
python3 -m venv stable_diffusion
```

### 2. 가상환경 활성화
```bash
source stable_diffusion/bin/activate
```

### 3. 필수 라이브러리 설치
```bash
pip install -r requirements.txt
```

### 4. app 디렉토리로 이동
```bash
cd app
```

### 5. FastAPI 실행(uvicorn 이용)
```bash
uvicorn main:app --reload
```
---

## API 사용 방법

### 이미지 생성 요청
```
GET /generate?prompt={your text prompt here}
```

- 예시
```
http://localhost:8000/generate?prompt=a cute anime girl with white hair
```

---

## 디렉토리 구조 예시
```bash
.
├── app
│   ├── main.py              # FastAPI 엔드포인트
│   └── generator.py         # 이미지 생성 로직
├── img/                     # 생성된 이미지 저장 폴더
├── requirements.txt         # 필요한 패키지 목록
└── README.md
```