# TTS Lite — gTTS + Edge TTS

Bản thu gọn chỉ dành cho TTS online: nhập văn bản hoặc import SRT/TXT, xuất MP3/WAV. Không cần Python, GPU, CUDA hay model AI trên máy.

## Tải và chạy

1. Mở [bản phát hành mới nhất](https://github.com/Thaiabcc/pyvideotrans/releases/latest).
2. Tải **TTS-Lite-Windows.zip** trong Assets, giải nén và mở **TTS-Lite.exe**.
3. Chọn gTTS hoặc Edge TTS, nhập văn bản / import SRT, rồi bấm **Xuất âm thanh…**.

Cần Internet. Nội dung được gửi tới Google hoặc Microsoft theo dịch vụ đã chọn. gTTS dùng ngôn ngữ `vi` cho tiếng Việt. Edge có giọng HoaiMy và NamMinh; có thể tải thêm danh sách giọng.

SRT giữ mốc thời gian và tự tăng tốc tối đa 2x. Đoạn không vừa mốc được báo riêng, lưu âm thanh gốc và báo cáo `.timeline.json`, không cắt lời.

## Build trên GitHub

Vào **Actions → Build TTS Lite → Run workflow**. GitHub kiểm tra SRT và xử lý âm thanh, build EXE, chạy thử giao diện, kiểm tra dịch vụ online rồi tạo Release. `build-sizes.json` ghi dung lượng chính xác; `online-check.json` ghi kết quả kiểm tra từng dịch vụ.

Mã nguồn bản gọn nằm trong `tts-lite-source.zip` và đính kèm mỗi Release. Bản pyVideoTrans đầy đủ trước đó vẫn nằm trong `source.zip` và workflow Build Windows EXE.

Giấy phép GPL-3.0. Mã căn SRT kế thừa từ bản pyVideoTrans tùy chỉnh, dự án gốc: https://github.com/jianchang512/pyvideotrans.
