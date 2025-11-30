import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
from sklearn.model_selection import train_test_split

# --- CẤU HÌNH ---
# Lấy đường dẫn thư mục hiện tại
ROOT_DIR = os.getcwd()
IMG_DIR = os.path.join(ROOT_DIR, 'imgs')
ANN_DIR = os.path.join(ROOT_DIR, 'annotations')

# Các đuôi file ảnh chấp nhận
IMG_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.bmp', '.JPG', '.PNG']

def extract_label_from_xml(xml_path):
    """Đọc file XML để lấy tên nhãn (label)"""
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        # Tìm object đầu tiên
        obj = root.find('object')
        if obj is not None:
            return obj.find('name').text
        return 'background'
    except:
        return 'Unknown'

def main():
    data = []
    
    # 1. Lấy danh sách tất cả ảnh
    all_images = []
    for ext in IMG_EXTENSIONS:
        # Tìm cả file thường và file trong folder con nếu có
        all_images.extend(glob.glob(os.path.join(IMG_DIR, f"*{ext}")))
    
    print(f"--> Tìm thấy {len(all_images)} ảnh trong thư mục 'imgs'.")

    if len(all_images) == 0:
        print("LỖI: Không tìm thấy ảnh nào! Hãy kiểm tra lại đường dẫn folder imgs.")
        return

    # 2. Duyệt qua từng ảnh để ghép cặp với XML
    for img_path in all_images:
        filename = os.path.basename(img_path)
        file_id = os.path.splitext(filename)[0]
        
        # Đường dẫn file XML dự kiến
        xml_path = os.path.join(ANN_DIR, file_id + '.xml')
        
        label = 'Unknown'
        
        # Nếu tìm thấy file XML thì đọc nhãn
        if os.path.exists(xml_path):
            label = extract_label_from_xml(xml_path)
        
        # Tự động đoán Severity qua tên file (nếu có)
        severity = 'Unknown'
        lower_name = filename.lower()
        if 'severe' in lower_name: severity = 'Severe'
        elif 'mild' in lower_name: severity = 'Mild'
        elif 'moderate' in lower_name: severity = 'Moderate'

        # Lưu đường dẫn tương đối để dễ di chuyển code
        rel_img_path = os.path.join('imgs', filename)
        
        data.append({
            'image_name': filename,
            'label': label,
            'severity': severity,
            'image_path': rel_img_path
        })

    df = pd.DataFrame(data)
    print(f"--> Đã ghép metadata cho {len(df)} ảnh.")

    # 3. Chia tập dữ liệu (70% Train - 20% Val - 10% Test)
    # Nếu dữ liệu quá ít hoặc mất cân bằng, code sẽ fallback về 'train' hết
    try:
        # Chỉ chia split nếu có đủ dữ liệu (>10 dòng)
        if len(df) > 10:
            # Tách 10% cho Test
            train_val, test = train_test_split(df, test_size=0.1, random_state=42, stratify=df['label'])
            # Tách tiếp 22.2% của phần còn lại (tương đương 20% tổng) cho Val
            train, val = train_test_split(train_val, test_size=0.2222, random_state=42, stratify=train_val['label'])
            
            df.loc[train.index, 'split'] = 'train'
            df.loc[val.index, 'split'] = 'val'
            df.loc[test.index, 'split'] = 'test'
        else:
            print("(!) Dữ liệu quá ít để chia tập, gán tất cả là 'train'.")
            df['split'] = 'train'
            
    except Exception as e:
        print(f"(!) Không thể chia đều theo Label (do số lượng label quá ít). Chuyển sang chia ngẫu nhiên.")
        # Chia ngẫu nhiên không cần stratify
        train_val, test = train_test_split(df, test_size=0.1, random_state=42)
        train, val = train_test_split(train_val, test_size=0.2222, random_state=42)
        df.loc[train.index, 'split'] = 'train'
        df.loc[val.index, 'split'] = 'val'
        df.loc[test.index, 'split'] = 'test'

    # 4. Xuất file CSV
    output_file = 'metadata_wound.csv'
    df.to_csv(output_file, index=False)
    
    print("-" * 30)
    print(f"✅ HOÀN THÀNH! File đã lưu tại: {output_file}")
    print("Thống kê dữ liệu:")
    print(df['split'].value_counts())
    print("-" * 30)

if __name__ == "__main__":
    main()