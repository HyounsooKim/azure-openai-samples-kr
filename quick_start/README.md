# 프롬프트 엔지니어링 Code를 이용한 실습

## 실습을 위한 개발환경 선택하기
해당 실습을 원활하게 제공하기 위해서 .devcontainer 환경을 제공하고 있습니다. 나의 PC에 Docker나 IDE 설치를 원하지 않는다면, `CodeSpace`를 권장합니다.  
- Local PC에 `Docker`가 설치되어 있다면, VS Code에서 Reopen DevContainer를 실행하여 Docker에 컨테이너 이미지를 생성하면 자동으로 실습 가능한 런타임과 패키지들이 설치되도록 구성되어 있습니다.  
- GitHub에서 제공하는 `CodeSpace`를 활용하면, CodeSpace가 제공하는 리모트 VM에 컨테이너가 올라가고, CodeSpace가 제공하는 웹브라우저 용 VS Code를 통해 즉시 개발을 진행할 수 있습니다.  
- Python 커널 3.11.4에 맞추어 테스트가 완료되었습니다.

참고: `CodeSpace`는 GitHub 개인 계정에게 월 15GB의 저장공간과 120 시간/core의 VM을 무료로 제공합니다.  
- [CodeSpace 비용](https://docs.github.com/en/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces)

#### 1️⃣ .env 파일 설정

.env.sample 파일을 .env 파일로 복사한 후 Azure OpenAI, AI Search 및 관련 리소스 API Key 값을 저장 후 진행합니다.  
코드 실습 도중, .env 파일 정보를 수정할 경우, 해당 파일의 커널을 `재시작` 하거나 파일을 닫았다가 다시 열어서 시작합니다.

#### 2️⃣ 실습 진행 순서

01_Create_resource 는 Infra 담당자 분이 미리 설정하는 부분입니다.

개발자일 경우, 02 ~ 15 번까지 하나씩 코드를 수행해 볼 수 있습니다.  
실습을 위해서 검증된 Python 커널 버전은 3.11.4 입니다. `Shift + Enter`를 누르면 실행됩니다.