# AI Wound Detection & Classification

Hệ thống nhận diện và phân loại vết thương sử dụng Deep Learning với mô hình ResNet-50 và kỹ thuật Transfer Learning/Fine-tuning.

## Giới thiệu

Dự án xây dựng mô hình AI có khả năng:

* Nhận diện các loại vết thương từ ảnh.
* Phân loại mức độ tổn thương.
* Đánh giá hiệu suất bằng Accuracy, Classification Report và Confusion Matrix.
* Trực quan hóa kết quả dự đoán trên tập kiểm thử.

Mô hình được huấn luyện bằng PyTorch và triển khai trên Google Colab.

---

## Quy trình thực hiện

### Giai đoạn 1: Chuẩn bị Dataset

* Đọc dữ liệu ảnh từ thư mục dataset.
* Đọc file XML annotation.
* Trích xuất nhãn (label) của từng ảnh.
* Phân loại mức độ nghiêm trọng:

  * Mild
  * Moderate
  * Severe
* Tạo file metadata CSV.
* Chia dữ liệu:

  * Train: 70%
  * Validation: 20%
  * Test: 10%

---

### Giai đoạn 2: Tiền xử lý ảnh

* Resize ảnh về kích thước chuẩn.
* Chuẩn hóa dữ liệu (Normalization).
* Data Augmentation:

  * Random Flip
  * Random Rotation
  * Random Crop

Mục tiêu:

* Giảm hiện tượng Overfitting.
* Tăng khả năng tổng quát hóa của mô hình.

---

### Giai đoạn 3: Xây dựng mô hình

Sử dụng:

* PyTorch
* Torchvision
* ResNet-50 Pretrained trên ImageNet

Transfer Learning:

* Tải trọng số pretrained.
* Thay thế lớp Fully Connected cuối cùng.
* Fine-tuning toàn bộ mạng để phù hợp với bài toán phân loại vết thương.

---

### Giai đoạn 4: Huấn luyện

Thông số huấn luyện:

| Tham số       | Giá trị             |
| ------------- | ------------------- |
| Optimizer     | Adam                |
| Learning Rate | 0.0001              |
| Loss Function | CrossEntropyLoss    |
| Batch Size    | 32                  |
| Epochs        | 20                  |
| GPU           | CUDA (Google Colab) |

---

### Giai đoạn 5: Đánh giá mô hình

Các chỉ số đánh giá:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

Thư viện sử dụng:

```python
sklearn.metrics
```

---

### Giai đoạn 6: Trực quan hóa

Hiển thị:

* Accuracy theo Epoch
* Loss theo Epoch
* Confusion Matrix
* Ảnh dự đoán đúng/sai

---

## Cấu trúc thư mục

```text
Wound_Project/
│
├── imgs/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
│
├── annotations/
│   ├── image1.xml
│   ├── image2.xml
│   └── ...
│
├── metadata_wound.csv
│
├── Ai_nhận_diện_vết_thương_và_phân_loại.ipynb
│
└── README.md
```

---

## Công nghệ sử dụng

* Python
* PyTorch
* Torchvision
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Google Colab

---

## Cài đặt

Clone repository:

```bash
git clone https://github.com/your-username/wound-detection.git
cd wound-detection
```

Cài đặt thư viện:

```bash
pip install torch torchvision pandas numpy matplotlib seaborn scikit-learn tqdm
```

---

## Chạy dự án

Mở notebook:

```bash
Ai_nhận_diện_vết_thương_và_phân_loại.ipynb
```

Thực hiện tuần tự các cell:

1. Chuẩn bị dữ liệu
2. Tiền xử lý ảnh
3. Tạo Dataset/DataLoader
4. Khởi tạo ResNet-50
5. Train Model
6. Đánh giá kết quả

---

##  Kết quả

Mô hình sử dụng Transfer Learning từ ResNet-50 giúp:

* Giảm thời gian huấn luyện.
* Tận dụng tri thức từ ImageNet.
* Cải thiện độ chính xác trên tập dữ liệu vết thương.

Kết quả cuối cùng được đánh giá bằng Accuracy, Classification Report và Confusion Matrix.

---

##  Tác giả

**Hoàng Ngô Việt**

Sinh viên Trường Đại học Khoa học Tự nhiên - ĐHQGHN

---

## License

Dự án phục vụ mục đích học tập và nghiên cứu.
