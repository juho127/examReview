# 🎓 시험 스캔 정보 검색 시스템

Gradio 기반의 시험 답안지 조회 애플리케이션입니다.

![시스템 스크린샷](screenShot/Screenshot%202025-10-31%20at%2011-27-01%20Gradio.png)

## 📋 주요 기능

- 학번으로 학생 본인의 정보 검색
- 학생의 이름, 학과, 점수 표시
- 답안지 스캔 이미지 조회
- 개인정보 보호 (본인 정보만 조회 가능)

## 🚀 설치 및 실행

### 1. 필요한 패키지 설치

```bash
pip install -r requirements.txt
```

### 2. 답안지 이미지 준비

`scanData` 폴더에 학번과 동일한 이름의 jpg 파일을 넣어주세요.

예시:
- `scanData/202200218.jpg`
- `scanData/202100288.jpg`

### 3. 애플리케이션 실행

```bash
python app.py
```

브라우저에서 `http://localhost:7860` 으로 접속하세요.

## 📁 파일 구조

```
examReview/
├── app.py                              # 메인 애플리케이션
├── test_result_excel_251031_1108.xls.csv  # 학생 데이터
├── scanData/                           # 답안지 이미지 폴더
│   ├── 202200218.jpg
│   ├── 202100288.jpg
│   └── ...
├── screenShot/                         # 스크린샷 폴더
│   └── Screenshot 2025-10-31 at 11-27-01 Gradio.png
├── requirements.txt                    # 패키지 의존성
├── README.md                          # 프로젝트 설명
└── LICENSE                            # MIT 라이센스
```

## 📄 CSV 파일 양식

학생 데이터 CSV 파일은 다음과 같은 형식을 따라야 합니다:

```csv
번호,ID,이름,학과,점수,평가의견
1,202200001,홍길동,컴퓨터공학과,85,
2,202200002,김철수,경영학과,90,
3,202200003,이영희,영어영문학과,78,
```

### CSV 필수 컬럼
- **번호**: 순번 (숫자)
- **ID**: 학번 (숫자, 이미지 파일명과 동일해야 함)
- **이름**: 학생 이름
- **학과**: 학과명
- **점수**: 시험 점수 (숫자)
- **평가의견**: 선택사항 (비워둘 수 있음)

### ⚠️ 중요 사항
- 첫 번째 행은 반드시 헤더여야 합니다
- CSV 파일은 UTF-8 인코딩으로 저장해야 합니다
- ID(학번)는 이미지 파일명과 정확히 일치해야 합니다

## 💡 사용 방법

1. 학번 입력란에 조회하고자 하는 학생의 학번을 입력합니다
2. "검색" 버튼을 클릭하거나 Enter 키를 누릅니다
3. 왼쪽에 학생 정보가 표시되고, 오른쪽에 답안지 이미지가 나타납니다

## 🎨 기능 상세

### 지원 이미지 형식
- .jpg, .JPG
- .jpeg, .JPEG
- .png, .PNG

### 개인정보 보호
- 학생들은 본인의 학번으로만 본인의 정보를 조회할 수 있습니다
- 전체 학생 목록은 표시되지 않습니다

## 🔧 파일명 변경시 고려사항

### CSV 파일명을 변경하려면

1. **CSV 파일명 변경**
   - 원하는 파일명으로 CSV 파일 이름을 변경합니다

2. **`app.py` 수정**
   - `app.py` 파일의 8번째 줄을 찾습니다
   ```python
   csv_file = "test_result_excel_251031_1108.xls.csv"
   ```
   - 새로운 파일명으로 변경합니다
   ```python
   csv_file = "새로운_파일명.csv"
   ```

### 이미지 폴더명을 변경하려면

1. **폴더명 변경**
   - `scanData` 폴더 이름을 원하는 이름으로 변경합니다

2. **`app.py` 수정**
   - `app.py` 파일의 11번째 줄을 찾습니다
   ```python
   scan_folder = Path("scanData")
   ```
   - 새로운 폴더명으로 변경합니다
   ```python
   scan_folder = Path("새로운_폴더명")
   ```

### 포트 번호를 변경하려면

- `app.py` 파일의 마지막 부분에서 포트 번호를 변경할 수 있습니다
```python
demo.launch(
    server_name="0.0.0.0",
    server_port=7860,  # 원하는 포트 번호로 변경
    share=True,
    show_error=True
)
```

## 📞 문의사항

이슈나 개선사항이 있으시면 알려주세요.
juho@hufs.ac.kr

## 📜 라이센스

MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

