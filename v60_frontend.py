import streamlit as st
import requests
from datetime import datetime

# Cấu hình tiêu đề trang web
st.set_page_config(page_title="V60 MagnaRise AI", page_icon="🚀", layout="centered")

st.title("🚀 V60 - Cổng Cập Nhật Tiến Độ")
st.markdown("---")

# Danh sách lựa chọn (Anh có thể bổ sung đủ 12 tên RM sau)
danh_sach_rm = ["Nguyễn Văn A", "Trần Thị Quynh Mai", "Lê Văn C"] 
danh_sach_trang_thai = ["S01 - Tiếp nhận", "S02 - Thẩm định", "S03 - Phê duyệt", "S04 - Giải ngân", "S05 - Hoàn tất"]

# Tạo Form nhập liệu
with st.form("nhap_lieu_form", clear_on_submit=True):
    st.subheader("Thông tin Hồ sơ")
    
    rm_name = st.selectbox("👤 Tên Chuyên Viên (RM):", danh_sach_rm)
    ma_hs_v60 = st.text_input("📁 Mã Hồ Sơ (Ví dụ: HS-002):")
    trang_thai = st.selectbox("📊 Trạng thái hiện tại:", danh_sach_trang_thai)
    
    st.markdown("---")
    # Nút bấm Submit
    submitted = st.form_submit_button("🚀 GỬI BÁO CÁO LÊN HỆ THỐNG", use_container_width=True)

    if submitted:
        if ma_hs_v60.strip() == "":
            st.error("⚠️ Vui lòng nhập Mã Hồ Sơ!")
        else:
            # 1. Đóng gói dữ liệu giống hệt định dạng API anh đã làm
            payload = {
                "rm_name": rm_name,
                "ma_hs_v60": ma_hs_v60.strip().upper(),
                "trang_thai": trang_thai[:3], # Cắt lấy chữ S01, S02 gửi đi
                "thoi_gian": datetime.now().strftime("%H:%M %d/%m/%Y")
            }
            
            # 2. Bắn dữ liệu thẳng vào API (Máy chủ đang chạy)
            try:
                # Đảm bảo máy chủ FastAPI ở màn hình đen 1 vẫn đang chạy
                res = requests.post("http://127.0.0.1:8000/api/v1/cap-nhat-ho-so", json=payload)
                if res.status_code == 200:
                    st.success(f"✅ Đã cập nhật thành công hồ sơ {ma_hs_v60.strip().upper()} lên máy chủ V60!")
            except Exception as e:
                st.error("❌ Không thể kết nối tới máy chủ V60. Vui lòng kiểm tra lại API.")