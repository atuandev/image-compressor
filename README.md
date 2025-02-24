# Images Compressor Python

Đây là code Python tối ưu hình ảnh hàng loạt một cách miễn phí, nhanh chóng. Có thể xử lý bao nhiêu cũng được, tốc độ nhanh.

## Giới thiệu
Đoạn code này xử lý tất cả các tệp hình ảnh trong thư mục được cung cấp, khớp với các loại được chỉ định, tối ưu hóa chúng và lưu chúng trong một thư mục đầu ra được chỉ định. Định dạng đầu ra cũng có thể được thiết lập. Nếu không có thư mục đầu ra nào được chỉ định, thư mục gốc sẽ được sử dụng làm vị trí đầu ra.

## Hướng dẫn setup
Hướng setup Python Project để chạy được source này tại [đây](https://www.notion.so/Setup-project-19c0e5ada1dd809096d2dfacc458115a)

## Chạy dự án sau khi setup xong
Mở terminal và chạy: `python main.py`

**Các tham số:**

- `folder_path` (str): Đường dẫn đến thư mục chứa hình ảnh cần tối ưu hóa.
- `input_image_types` (str): Danh sách các loại hình ảnh đầu vào được phân tách bằng dấu phẩy để xử lý (ví dụ: "jpg,png"). Mặc định là "jpg,png".
- `output_image_type` (str): Loại hình ảnh đầu ra mong muốn. Nếu là `None`, hình ảnh sẽ giữ nguyên loại ban đầu.
- `output_folder` (str): Thư mục để lưu hình ảnh đã tối ưu hóa. Nếu là `None`, `folder_path` sẽ được sử dụng làm thư mục đầu ra.

**Ví dụ sử dụng:**

Để tối ưu hóa tất cả các tệp jpg và png trong thư mục "images" và lưu chúng dưới dạng webp trong thư mục "optimized_images", bạn có thể sử dụng đoạn code sau:

```python
optimize_images(folder_path="images", input_image_types="jpg,png", output_image_type="webp", output_folder="optimized_images")
```

Nếu bạn muốn tối ưu hóa hình ảnh mà không thay đổi định dạng và lưu chúng trong cùng thư mục, bạn có thể sử dụng:


```python
optimize_images(folder_path="images")
```
