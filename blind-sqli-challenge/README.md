# 🎯 Poeency's CTF Challenge - "Blind Shop"

Chào mừng các bạn đến với thử thách CTF của mình! Đây là một web application challenge về Blind SQL Injection với twist thú vị.

## 🌐 Thông tin thử thách

**🔗 Challenge URL:** http://100.93.221.59:53191

**🚩 Flag format:** `poeency{...}`

**⏰ Thời gian:** 05/12/2025 18h - 05/12/2025 22h

**🎮 Mục tiêu:** Tìm flag ẩn trong hệ thống!

## 📋 Hướng dẫn tham gia

### Bước 1: Truy cập website

Mở trình duyệt và truy cập: **http://100.93.221.59:53191**

### Bước 2: Đăng ký tài khoản

1. Click vào nút **Register** hoặc **Sign Up**
2. Tạo tài khoản với username và password của bạn
3. Đăng nhập vào hệ thống

### Bước 3: Khám phá và tìm lỗ hổng

Website này là một cửa hàng online đơn giản. Nhiệm vụ của bạn là:

- 🔍 Khám phá các chức năng của website
- 🐛 Tìm các lỗ hổng bảo mật (SQL Injection, XSS, IDOR, etc.)
- 🎯 Khai thác để lấy được flag với format `poeency{...}`

### Bước 4: Submit flag

Khi tìm được flag, hãy gửi cho mình để xác nhận! 🎉

## 💡 Gợi ý

<details>
<summary>Click để xem gợi ý (spoiler warning!)</summary>

**📖 Chương 1: Khám phá cửa hàng**
> _"Mình vừa đăng ký tài khoản và bắt đầu mua sắm. Có vẻ như có một số sản phẩm mình không thể xem được... Chắc là dành cho VIP hay gì đó?"_

- Hãy thử mua một vài sản phẩm và xem lịch sử đơn hàng
- Chú ý xem có gì đặc biệt không?
- Nếu bạn là admin, bạn sẽ muốn xem thông tin gì?

**📖 Chương 2: Danh tính là gì?**
> _"Hmm, username của mình chỉ là một chuỗi text thôi mà... Vậy nếu mình đặt tên là một câu lệnh thì sao?"_

- Khi bạn đăng ký, username có bị validate không?
- Nếu username được dùng trong database query...
- Thử nghĩ xem: mua hàng → lưu vào database → ai đó xem lịch sử...

**📖 Chương 3: Dấu vết vô hình**
> _"Mình không thấy kết quả trực tiếp, nhưng có cách nào để biết query có chạy không? Ví dụ như... xem có đơn hàng nào xuất hiện không?"_

- Boolean Blind SQLi: True = có kết quả, False = không có
- Time-based Blind SQLi: Delay để biết True/False
- Nhưng còn một cách khác: **Side-channel** - quan sát tác động gián tiếp!
- Nếu query đúng → username được insert → ai đó có thể TÌM THẤY nó

**📖 Chương 4: Leo thang đặc quyền**
> _"Được rồi, giờ mình cần trở thành admin. Nhưng password là gì nhỉ? Không sao, mình có thể đoán từng ký tự một..."_

- Dùng `LIKE 'a%'` để check ký tự đầu
- Mỗi lần đúng → tạo username mới → mua hàng → kiểm tra
- Lặp lại cho đến khi có full password
- Login với admin credentials!

**📖 Chương 5: Tìm kho báu**
> _"Giờ mình đã là admin rồi! Nhưng flag ở đâu? Tên bảng bị randomize... Phải tìm cách leak tên bảng trước đã."_

- Admin có thể xem order history của tất cả users
- Dùng kỹ thuật tương tự để leak:
  - Tên bảng (từ `sqlite_master`)
  - Tên cột (từ `pragma_table_info`)
  - Cuối cùng là flag!

**🎯 Tóm lại:**
1. SQLi qua username khi mua hàng
2. Bruteforce admin password qua side-channel (order history)
3. Login as admin
4. Leak flag table name và flag content

</details>

## 🛠️ Tools hữu ích

Các công cụ có thể giúp bạn:

- **Burp Suite / OWASP ZAP** - Proxy để phân tích HTTP requests
- **SQLMap** - Tự động khai thác SQL Injection
- **Browser DevTools** - Kiểm tra JavaScript, cookies, local storage
- **Python requests** - Viết script tự động hóa

## ⚠️ Lưu ý quan trọng

- ✅ **Được phép:** Tấn công vào website này
- ❌ **Không được:** DDoS hoặc làm crash server
- 🤝 **Khuyến khích:** Chia sẻ kiến thức sau khi hoàn thành
- 📝 **Writeup:** Hãy viết writeup về cách bạn giải quyết challenge!

