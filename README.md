# Bài 3: Cấu hình xác thực SSH và Đẩy dự án lên GitHub

## Giới thiệu
Bài tập này hướng dẫn cách cấu hình khóa SSH (Ed25519) để xác thực an toàn với GitHub và đẩy mã nguồn từ thư mục cục bộ lên kho lưu trữ từ xa mà không cần sử dụng mật khẩu.

## Các bước thực hiện
1. Tạo khóa SSH Ed25519:
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```
2. Khởi động SSH agent và thêm khóa:
   ```bash
   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/id_ed25519
   ```
3. Sao chép nội dung khóa công khai (`~/.ssh/id_ed25519.pub`) và thêm vào cài đặt SSH keys trên GitHub.
4. Kiểm tra kết nối:
   ```bash
   ssh -T git@github.com
   ```
5. Liên kết repository cục bộ với GitHub bằng giao thức SSH và đẩy mã nguồn:
   ```bash
   git remote add origin git@github.com:username/repository.git
   git push -u origin main
   ```

## Hướng dẫn chạy chương trình
Chạy file `main.py` để kiểm tra trạng thái môi trường Git cục bộ:
```bash
python main.py
```