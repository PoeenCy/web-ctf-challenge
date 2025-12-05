# 🎯 Poeency's CTF Challenge - "Sanity Check"

Chào mừng các bạn đến với thử thách khởi động! Đây là một web application challenge về PHP Type Juggling - hoàn hảo để làm quen với môi trường CTF.

## 🌐 Thông tin thử thách

**🔗 Challenge URL:** http://100.93.221.59:37821

**🚩 Flag format:** `poeency{...}`

**⏰ Thời gian:** Tạm thời (có thể đóng bất cứ lúc nào)

**🎮 Mục tiêu:** Bypass validation và lấy flag!

## 📋 Hướng dẫn tham gia

### Bước 1: Truy cập website

Mở trình duyệt và truy cập: **http://100.93.221.59:37821**

⚠️ **Lưu ý:** Challenge chỉ accessible qua Tailscale VPN. Xem [hướng dẫn setup Tailscale](../TAILSCALE_SETUP.md).

### Bước 2: Đăng nhập

1. Nhập bất kỳ username nào
2. Click **Login**
3. Bạn sẽ thấy một grid các checkboxes

### Bước 3: Khám phá và tìm lỗ hổng

Website này là một trang "vibe coding" đơn giản. Nhiệm vụ của bạn là:

- 🔍 Khám phá cách website xử lý input
- 🐛 Tìm lỗ hổng PHP Type Juggling
- 🎯 Bypass validation để lấy flag

### Bước 4: Submit flag

Khi tìm được flag, hãy gửi cho mình để xác nhận! 🎉

## 💡 Gợi ý

<details>
<summary>Click để xem gợi ý (spoiler warning!)</summary>

**📖 Chương 1: Quan sát**
> _"Mình vừa login và thấy một grid checkboxes. Có vẻ như mình cần chọn đúng các ô để lấy flag..."_

- Thử check/uncheck các boxes và submit
- Xem response trả về như thế nào
- Có validation nào không?

**📖 Chương 2: PHP Type Juggling**
> _"Hmm, PHP xử lý dữ liệu như thế nào nhỉ? Loose comparison (`==`) vs Strict comparison (`===`)..."_

- PHP có thể so sánh kiểu dữ liệu khác nhau
- `"string" == 0` → `true` trong PHP!
- Array, dictionary, list... đều có cách so sánh riêng
- Nếu server expect một kiểu dữ liệu nhưng nhận được kiểu khác?

**📖 Chương 3: Bypass Validation**
> _"Server đang check gì? Làm sao để bypass nó?"_

- Checkboxes gửi data dưới dạng gì?
- Thử thay đổi request với Burp Suite
- Nếu server expect `list` nhưng nhận được `dict` thì sao?
- Type juggling có thể giúp bypass validation!

**🎯 Tóm lại:**
1. Hiểu cách PHP xử lý type juggling
2. Phân tích request/response
3. Thay đổi data type để bypass validation
4. Lấy flag!

</details>

## 🛠️ Tools hữu ích

Các công cụ có thể giúp bạn:

- **Burp Suite / OWASP ZAP** - Proxy để phân tích và modify HTTP requests
- **Browser DevTools** - Kiểm tra Network tab, xem request/response
- **Python requests** - Viết script để test các payload khác nhau
- **curl** - Test nhanh các request

## ⚠️ Lưu ý quan trọng

- ✅ **Được phép:** Tấn công vào website này
- ❌ **Không được:** DDoS hoặc làm crash server
- 🤝 **Khuyến khích:** Chia sẻ kiến thức sau khi hoàn thành
- 📝 **Writeup:** Hãy viết writeup về cách bạn giải quyết challenge!
- 🌐 **VPN Required:** Phải join Tailscale network để truy cập

## 🎓 Kiến thức cần biết

Challenge này giúp bạn học về:

- **PHP Type Juggling** - Cách PHP so sánh các kiểu dữ liệu khác nhau
- **Loose vs Strict Comparison** - Sự khác biệt giữa `==` và `===`
- **HTTP Request Manipulation** - Thay đổi request để bypass validation
- **Web Security Basics** - Hiểu cách validate input đúng cách

## 🏃 Chạy local (Optional)

Nếu muốn chạy local để test:

```bash
cd sanity_check
docker-compose up -d

# Truy cập: http://localhost:37821
```

---

**Good luck và have fun! 🚀**

_Challenge created by poeency_
