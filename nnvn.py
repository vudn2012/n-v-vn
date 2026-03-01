import streamlit as st

# 1. CẤU HÌNH TRANG
st.set_page_config(page_title="Từ điển Ngôn ngữ mạng", page_icon="📖", layout="wide")

# 2. KHO DỮ LIỆU 
slangs = [
    {"cat": "Gen Z", "word": "Chằm Zn", "meaning": "Trạng thái trầm cảm, mệt mỏi (Kẽm ký hiệu là Zn)."},
    {"cat": "Gen Z", "word": "Flex", "meaning": "Khoe khoang thành tích cá nhân một cách khéo léo."},
    {"cat": "Gen Z", "word": "Ét ô ét", "meaning": "SOS - Dùng khi gặp tình huống khẩn cấp hoặc khó đỡ."},
    {"cat": "Gen Z", "word": "Xịt keo", "meaning": "Trạng thái đứng hình, câm nín vì quá bất ngờ."},
    {"cat": "Gen Z", "word": "Vô tri", "meaning": "Những hành động không ý nghĩa nhưng gây cười."},
    {"cat": "Gen Alpha", "word": "Skibidi", "meaning": "Dùng để chỉ sự kỳ quặc hoặc quá đỉnh."},
    {"cat": "Gen Alpha", "word": "Sigma", "meaning": "Chỉ người ngầu, độc lập, bản lĩnh."},
    {"cat": "Xu hướng", "word": "Check var", "meaning": "Kiểm tra, xác minh tính đúng đắn của thông tin."},
    {"cat": "Xu hướng", "word": "Cứu dữ chưa", "meaning": "Câu cảm thán khi gặp tình huống oái oăm."},
    {"cat": "Xu hướng", "word": "Ngoan xinh yêu", "meaning": "Cách gọi cưng nựng dành cho người yêu."},
    {"cat": "Đời đầu", "word": "Gà mờ", "meaning": "Người mới, chưa có kinh nghiệm."},
    {"cat": "Đời đầu", "word": "Cùi bắp", "meaning": "Kém cỏi, lỗi thời."},
    {"cat": "Văn hóa mạng", "word": "Hết nước chấm", "meaning": "Tuyệt vời, không còn gì để chê."},
    {"cat": "Văn hóa mạng", "word": "À lôi", "meaning": "Từ cảm thán 'Trời ơi' của người Tày."}
]

# 3. GIAO DIỆN CHÍNH (HOÀN TOÀN BẰNG PYTHON)
st.title("📖 TỪ ĐIỂN NGÔN NGỮ MẠNG VIỆT NAM")
st.write("Dự án liệt kê các thuật ngữ mạng xã hội phổ biến nhất.")

# Thanh tìm kiếm
search_query = st.text_input("🔍 Nhập từ lóng cần tìm...", "").lower()

# Bộ lọc danh mục
categories = ["Tất cả"] + sorted(list(set(item["cat"] for item in slangs)))
selected_cat = st.selectbox("📂 Lọc theo thế hệ/danh mục:", categories)

# Xử lý logic lọc dữ liệu
filtered_slangs = slangs
if search_query:
    filtered_slangs = [i for i in filtered_slangs if search_query in i["word"].lower()]
if selected_cat != "Tất cả":
    filtered_slangs = [i for i in filtered_slangs if i["cat"] == selected_cat]

# Hiển thị kết quả dưới dạng thẻ (Cards)
st.divider()
if filtered_slangs:
    cols = st.columns(3) # Chia làm 3 cột
    for idx, item in enumerate(filtered_slangs):
        with cols[idx % 3]:
            with st.container(border=True):
                st.subheader(f":red[{item['word']}]")
                st.caption(f"Phân loại: {item['cat']}")
                st.write(item['meaning'])
else:
    st.info("Không tìm thấy từ này. Hãy thử từ khác nhé! 😅")

# 4. CHÂN TRANG
st.divider()
st.caption("Dự án học tập từ ICANTECH - Phát triển bởi Python")
