# 🎓 Exam Scan Information System
# 시험 스캔 정보 검색 시스템

A Gradio-based exam answer sheet viewing application.  
Gradio 기반의 시험 답안지 조회 애플리케이션입니다.

![System Screenshot](screenShot/Screenshot%202025-10-31%20at%2011-27-01%20Gradio.png)

## 📋 Key Features | 주요 기능

- **Individual Access**: Students can search their own exam information using their student ID  
  **개별 접근**: 학생들이 자신의 학번으로 본인의 시험 정보 검색
- **Information Display**: Shows student name, department, and score  
  **정보 표시**: 학생의 이름, 학과, 점수 표시
- **Answer Sheet Viewing**: Displays scanned exam answer sheet images  
  **답안지 조회**: 답안지 스캔 이미지 조회
- **Privacy Protection**: Students can only view their own information  
  **개인정보 보호**: 본인 정보만 조회 가능

## 🚀 Installation and Setup | 설치 및 실행

### 1. Install Required Packages | 필요한 패키지 설치

```bash
pip install -r requirements.txt
```

### 2. Prepare Answer Sheet Images | 답안지 이미지 준비

Create a `scanData` folder and place jpg files with names matching student IDs.  
`scanData` 폴더를 생성하고 학번과 동일한 이름의 jpg 파일을 넣어주세요.

Example | 예시:
- `scanData/202200001.jpg`
- `scanData/202200002.jpg`

### 3. Run the Application | 애플리케이션 실행

```bash
python app.py
```

Access via browser at `http://localhost:7860`  
브라우저에서 `http://localhost:7860` 으로 접속하세요.

## 📁 File Structure | 파일 구조

```
examReview/
├── app.py                              # Main application | 메인 애플리케이션
├── sample_data.csv                     # Sample student data | 샘플 학생 데이터
├── scanData/                           # Answer sheet images folder | 답안지 이미지 폴더
│   ├── 202200001.jpg
│   ├── 202200002.jpg
│   └── ...
├── screenShot/                         # Screenshot folder | 스크린샷 폴더
│   └── Screenshot 2025-10-31 at 11-27-01 Gradio.png
├── requirements.txt                    # Package dependencies | 패키지 의존성
├── README.md                           # Project documentation | 프로젝트 설명
└── LICENSE                             # MIT License | MIT 라이센스
```

## 📄 CSV File Format | CSV 파일 양식

The student data CSV file should follow this format:  
학생 데이터 CSV 파일은 다음과 같은 형식을 따라야 합니다:

```csv
번호,ID,이름,학과,점수,평가의견
1,202200001,홍길동,컴퓨터공학과,85,
2,202200002,김철수,경영학과,90,
3,202200003,이영희,영어영문학과,78,
```

### Required Columns | 필수 컬럼
- **번호 (Number)**: Sequence number | 순번
- **ID**: Student ID (must match image filename) | 학번 (이미지 파일명과 일치)
- **이름 (Name)**: Student name | 학생 이름
- **학과 (Department)**: Department name | 학과명
- **점수 (Score)**: Exam score | 시험 점수
- **평가의견 (Comment)**: Optional | 선택사항

### ⚠️ Important Notes | 중요 사항
- First row must be the header | 첫 번째 행은 반드시 헤더
- CSV file must be saved in UTF-8 encoding | UTF-8 인코딩으로 저장
- Student ID must exactly match the image filename | ID(학번)는 이미지 파일명과 정확히 일치

## 💡 How to Use | 사용 방법

1. Enter your student ID in the input field  
   학번 입력란에 본인의 학번을 입력합니다
2. Click the "Search" button or press Enter  
   "검색" 버튼을 클릭하거나 Enter 키를 누릅니다
3. Your information will be displayed on the left, and your answer sheet image on the right  
   왼쪽에 학생 정보가 표시되고, 오른쪽에 답안지 이미지가 나타납니다

## 🎨 Additional Features | 기능 상세

### Supported Image Formats | 지원 이미지 형식
- .jpg, .JPG
- .jpeg, .JPEG
- .png, .PNG

### Privacy Protection | 개인정보 보호
- Students can only view their own information using their student ID  
  학생들은 본인의 학번으로만 본인의 정보를 조회할 수 있습니다
- Complete student list is not displayed  
  전체 학생 목록은 표시되지 않습니다

## 🔧 Configuration | 파일명 변경시 고려사항

### To Change CSV Filename | CSV 파일명을 변경하려면

1. **Rename the CSV file**  
   **CSV 파일명 변경**
   - Rename your CSV file to the desired name  
     원하는 파일명으로 CSV 파일 이름을 변경합니다

2. **Modify `app.py`**  
   **`app.py` 수정**
   - Find line 8 in `app.py` | `app.py` 파일의 8번째 줄을 찾습니다
   ```python
   csv_file = "test_result_excel_251031_1108.xls.csv"
   ```
   - Change to your new filename | 새로운 파일명으로 변경합니다
   ```python
   csv_file = "your_new_filename.csv"
   ```

### To Change Image Folder Name | 이미지 폴더명을 변경하려면

1. **Rename the folder**  
   **폴더명 변경**
   - Rename `scanData` folder to your desired name  
     `scanData` 폴더 이름을 원하는 이름으로 변경합니다

2. **Modify `app.py`**  
   **`app.py` 수정**
   - Find line 11 in `app.py` | `app.py` 파일의 11번째 줄을 찾습니다
   ```python
   scan_folder = Path("scanData")
   ```
   - Change to your new folder name | 새로운 폴더명으로 변경합니다
   ```python
   scan_folder = Path("your_new_folder_name")
   ```

### To Change Port Number | 포트 번호를 변경하려면

- Modify the port number at the end of `app.py`  
  `app.py` 파일의 마지막 부분에서 포트 번호를 변경할 수 있습니다
```python
demo.launch(
    server_name="0.0.0.0",
    server_port=7860,  # Change to your desired port | 원하는 포트 번호로 변경
    share=True,
    show_error=True
)
```

## 📞 Contact | 문의사항

For issues or improvements, please contact:  
이슈나 개선사항이 있으시면 연락주세요:

juho@hufs.ac.kr

## 📜 License | 라이센스

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
