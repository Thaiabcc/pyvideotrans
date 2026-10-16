# pyVideoTrans — bản Windows tự build

Mã nguồn tùy chỉnh từ project pyVideoTrans, build hoàn toàn bằng GitHub Actions. Không cần build hay cài Python trên máy sử dụng.

## Tải và sử dụng

1. Mở [Releases](https://github.com/Thaiabcc/pyvideotrans/releases).
2. Chọn bản build mới nhất và tải **pyVideoTrans-Windows.zip** trong Assets.
3. Giải nén toàn bộ ZIP vào một thư mục.
4. Mở **sp.exe**; giữ nguyên các thư mục đi kèm.

Nếu chưa có Release, xem [trạng thái build](https://github.com/Thaiabcc/pyvideotrans/actions). Chỉ bản vượt qua bước build và kiểm tra import mới được phát hành. Model AI được tải khi sử dụng; tính năng GPU cần driver NVIDIA phù hợp.

## Build lại trên GitHub

Vào **Actions → Build Windows EXE → Run workflow**. Máy chủ Windows của GitHub cài thư viện theo uv.lock, đóng gói EXE, kèm FFmpeg, kiểm tra import và tạo Release.

## Mã nguồn

- source.zip: mã nguồn project, gồm pyproject.toml, uv.lock, LICENSE và thư mục videotrans.
- build_windows.py: chương trình đóng gói chạy trên GitHub.
- .github/workflows/windows-build.yml: cấu hình GitHub Actions.

Bản upload loại bỏ môi trường .venv, log, video đầu ra, model đã tải và các cấu hình cá nhân.

Dự án gốc: https://github.com/jianchang512/pyvideotrans — giấy phép GPL-3.0, xem LICENSE trong source.zip và bản phát hành.
