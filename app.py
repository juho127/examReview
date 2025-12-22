import gradio as gr
import pandas as pd
import os
from pathlib import Path

# CSV 파일 읽기 (상위 폴더의 list_data.csv 사용)
try:
    csv_file = Path(__file__).parent.parent / "list_data.csv"
    df = pd.read_csv(csv_file, encoding='utf-8')
except FileNotFoundError:
    try:
        csv_file = Path(__file__).parent.parent / "list_data.csv"
        df = pd.read_csv(csv_file, encoding='cp949')
    except Exception as e:
        print(f"❌ CSV 파일을 읽을 수 없습니다: {e}")
        df = pd.DataFrame(columns=['구분', '학번', '이름', '학과', '점수'])
except Exception as e:
    print(f"❌ CSV 파일을 읽을 수 없습니다: {e}")
    df = pd.DataFrame(columns=['구분', '학번', '이름', '학과', '점수'])

# scanData 폴더 경로
scan_folder = Path(__file__).parent.parent / "scanData"

# 구분과 scanData 폴더 매핑
CATEGORY_FOLDER_MAP = {
    "비즈니스딥러닝_설캠": "비딥설",
    "비즈니스딥러닝_글캠": "비딥글",
    "인공지능": "인공지능"
}

def get_categories():
    """구분 목록 반환"""
    try:
        categories = list(df['구분'].unique())
        return categories if categories else ["데이터 없음"]
    except Exception:
        return ["데이터 없음"]

def search_student(category, student_id):
    """구분과 학생 ID로 정보 검색"""
    try:
        # 입력 검증
        if not category or category == "데이터 없음":
            gr.Warning("⚠️ 구분을 선택해주세요.")
            return "### ⚠️ 구분을 선택해주세요.", "", "", "", None
        
        if not student_id:
            gr.Warning("⚠️ 학번을 입력해주세요.")
            return "### ⚠️ 학번을 입력해주세요.", "", "", "", None
        
        # ID를 문자열로 변환하여 검색
        student_id = str(student_id).strip()
        
        # 학번이 숫자인지 확인
        if not student_id.isdigit():
            gr.Warning("⚠️ 학번은 숫자만 입력 가능합니다.")
            return "### ⚠️ 학번은 숫자만 입력 가능합니다.", "", "", "", None
        
        # 데이터프레임에서 해당 구분과 학생 찾기
        student = df[(df['구분'] == category) & (df['학번'].astype(str) == student_id)]
        
        if student.empty:
            gr.Warning(f"⚠️ 해당 구분에서 학번 '{student_id}'을(를) 찾을 수 없습니다.")
            return f"### ❌ 해당 구분에서 학번을 찾을 수 없습니다.\n\n입력한 정보를 다시 확인해주세요.\n\n- **선택한 구분:** {category}\n- **입력한 학번:** {student_id}", "", "", "", None
        
        # 학생 정보 추출
        student_info = student.iloc[0]
        name = str(student_info['이름'])
        department = str(student_info['학과'])
        score = student_info['점수']
        
        # 이미지 파일 찾기 (구분에 맞는 폴더에서)
        folder_name = CATEGORY_FOLDER_MAP.get(category, category)
        image_folder = scan_folder / folder_name
        image_path = image_folder / f"{student_id}.jpg"
        
        image = None
        if image_path.exists():
            image = str(image_path)
        else:
            # 다른 확장자도 확인
            for ext in ['.JPG', '.jpeg', '.JPEG', '.png', '.PNG']:
                alt_path = image_folder / f"{student_id}{ext}"
                if alt_path.exists():
                    image = str(alt_path)
                    break
        
        if image is None:
            gr.Info(f"ℹ️ 답안지 이미지가 없습니다. (폴더: {folder_name})")
        
        # 결과 포맷팅
        info_text = f"""
### 📋 학생 정보

**구분:** {category}  
**학번:** {student_id}  
**이름:** {name}  
**학과:** {department}  
**점수:** {score}점
        """
        
        gr.Info(f"✅ '{name}' 학생 정보를 찾았습니다!")
        return info_text, name, department, f"{score}점", image
        
    except Exception as e:
        gr.Error(f"❌ 오류가 발생했습니다: {str(e)}")
        return f"### ❌ 오류 발생\n\n{str(e)}", "", "", "", None

def create_ui():
    """Gradio UI 생성"""
    
    # 커스텀 CSS
    custom_css = """
    #main-container {
        max-width: 1400px;
        margin: auto;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 15px;
    }
    .gradio-container {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    #search-box {
        font-size: 18px;
        padding: 12px;
        border-radius: 10px;
        border: 2px solid #667eea;
    }
    #category-box {
        font-size: 16px;
        padding: 10px;
        border-radius: 10px;
        border: 2px solid #667eea;
    }
    #search-btn {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border: none;
        padding: 12px 30px;
        font-size: 16px;
        font-weight: bold;
        border-radius: 10px;
        cursor: pointer;
        transition: all 0.3s;
    }
    #search-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    .info-box {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 10px 0;
    }
    #image-display {
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    """
    
    with gr.Blocks(css=custom_css, theme=gr.themes.Soft()) as demo:
        gr.Markdown(
            """
            # 🎓 Hankuk University of Foreign Studies 시험 스캔 정보 검색 시스템
            ### 과목을 선택하고 학번을 입력하여 시험 정보와 답안지를 확인하세요
            ---
            """
        )
        
        with gr.Row():
            with gr.Column(scale=1):
                category_input = gr.Dropdown(
                    label="📚 구분 선택",
                    choices=get_categories(),
                    value=None,
                    elem_id="category-box"
                )
                student_id_input = gr.Textbox(
                    label="🔍 학번 입력",
                    placeholder="학번을 입력하세요 (예: 202200218)",
                    elem_id="search-box"
                )
                search_btn = gr.Button(
                    "검색",
                    variant="primary",
                    size="lg",
                    elem_id="search-btn"
                )
        
        gr.Markdown("---")
        
        with gr.Row():
            with gr.Column(scale=1):
                info_display = gr.Markdown(
                    "### 과목을 선택하고 학번을 입력 후 검색 버튼을 클릭하세요",
                    elem_classes="info-box"
                )
                
                with gr.Row():
                    with gr.Column():
                        name_display = gr.Textbox(
                            label="👤 이름",
                            interactive=False
                        )
                    with gr.Column():
                        dept_display = gr.Textbox(
                            label="🏫 학과",
                            interactive=False
                        )
                    with gr.Column():
                        score_display = gr.Textbox(
                            label="📊 점수",
                            interactive=False
                        )
            
            with gr.Column(scale=1):
                image_display = gr.Image(
                    label="📄 답안지 스캔",
                    type="filepath",
                    elem_id="image-display",
                    height=500
                )
        
        gr.Markdown(
            """
            ---
            💡 **안내사항:**
            - 과목(구분)을 선택한 후 본인의 학번을 정확히 입력해주세요
            - 답안지 이미지와 시험 결과를 확인할 수 있습니다
            - 개인정보 보호를 위해 본인의 정보만 조회 가능합니다
            - 제작 : juho@hufs.ac.kr
            """
        )
        
        # 이벤트 핸들러
        search_btn.click(
            fn=search_student,
            inputs=[category_input, student_id_input],
            outputs=[info_display, name_display, dept_display, score_display, image_display]
        )
        
        # Enter 키로도 검색 가능
        student_id_input.submit(
            fn=search_student,
            inputs=[category_input, student_id_input],
            outputs=[info_display, name_display, dept_display, score_display, image_display]
        )
    
    return demo

if __name__ == "__main__":
    # scanData 폴더가 없으면 생성
    if not scan_folder.exists():
        scan_folder.mkdir(exist_ok=True)
        print(f"⚠️  '{scan_folder}' 폴더가 생성되었습니다. 이미지 파일을 이 폴더에 넣어주세요.")
    
    print(f"📁 CSV 파일: {csv_file}")
    print(f"📁 스캔 폴더: {scan_folder}")
    print(f"📊 로드된 데이터: {len(df)}개 레코드")
    
    # Gradio 앱 실행
    demo = create_ui()
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=True,
        show_error=True,
        allowed_paths=[str(scan_folder)]
    )
