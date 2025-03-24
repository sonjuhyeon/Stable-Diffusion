## FastAPI 시작하는 방법

- 1. venv 가상환경 생성
python3 -m venv stable_diffusion

- 2. 가상환경 활성화
source stable_diffusion/bin/activate

- 3. 필수 라이브러리 설치  
pip install -r requirements.txt

- 4. app 디렉토리로 이동  
cd app

- 5. FastAPI 실행(uvicorn 이용)
uvicorn main:app --reload