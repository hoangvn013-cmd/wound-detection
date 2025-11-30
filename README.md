# 🏥 AI Wound Diagnosis & First Aid Support
> Hệ thống chẩn đoán vết thương và tư vấn sơ cứu sử dụng Deep Learning (ResNet-50).

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)

## 📖 Giới thiệu (Introduction)
Dự án xây dựng một hệ thống thị giác máy tính hỗ trợ phân loại các vết thương ngoài da phổ biến (Bỏng, Vết cắt, Trầy xước...) và đưa ra hướng dẫn sơ cứu ngay lập tức. Hệ thống sử dụng mô hình **ResNet-50** với kỹ thuật **Transfer Learning**, đạt độ chính xác cao trên tập kiểm thử.

## 🗂️ Dữ liệu (Dataset)
- **Nguồn:** Tổng hợp ~1.500 ảnh thực tế.
- **Phân loại:**
    - `Burn` (Bỏng)
    - `Cut/Laceration` (Vết cắt/rách)
    - `Abrasion` (Trầy xước)
    - ...
- **Quy trình:** Dữ liệu được chuẩn hóa, gán nhãn và chia tập Train/Val/Test (70/20/10).

## 🧠 Mô hình & Kỹ thuật (Methodology)
1. **Model:** ResNet-50 (Pre-trained on ImageNet).
2. **Kỹ thuật Training:**
   - **Fine-tuning:** Tinh chỉnh toàn bộ mô hình để thích nghi với ảnh y tế.
   - **Data Augmentation:** RandomResizedCrop, Rotation, ColorJitter.
   - **Dropout (0.5):** Giảm thiểu Overfitting.
3. **Kết quả:**
   - Accuracy: >90%
   - F1-Score trung bình: >0.85
