# poeency's CTF Challenge - Sanity Check

## 🎯 Challenge Overview

Welcome to **poeency's Checkbox Challenge**! This is a type juggling challenge where you need to bypass input validation to retrieve the flag.

## 🚀 Quick Start

### Prerequisites
- Docker
- Docker Compose

### Running the Challenge

1. **Build and start the container:**
   ```bash
   docker-compose up -d --build
   ```

2. **Access the challenge:**
   Open your browser and navigate to:
   ```
   http://localhost:37821
   ```

3. **Stop the challenge:**
   ```bash
   docker-compose down
   ```

## 📝 Challenge Description

Chào mừng bạn ghé thăm website "vibe coding" của mình! Thực ra mình dựng nó chỉ để test xem server cần oxi không thôi, nhưng ở đâu đó vẫn có vài lỗi nho nhỏ đang ẩn mình. Liệu bạn có tìm ra chúng không?

## 🎮 How to Play

1. Enter any username to login
2. You'll see a grid of checkboxes
3. Find a way to bypass the validation and get the flag!

## 🔧 Configuration

- **Port:** The challenge runs on port 37821 (mapped from internal port 5000)
- **Flag Format:** `poeency{...}`
- **Container Name:** `poeency_sanity_check`

## 📁 Files Structure

```
sanity_check/
├── build/              # Application source code
│   ├── app.py         # Main Flask application
│   ├── Dockerfile     # Container configuration
│   ├── flag.txt       # Flag file
│   ├── init.sh        # Initialization script
│   ├── static/        # CSS and static assets
│   └── templates/     # HTML templates
├── solution/          # Solution and writeup
│   ├── exploit.py     # Exploit script
│   └── solution.md    # Detailed writeup
└── docker-compose.yml # Docker compose configuration
```

## 🛠️ Development

To modify the challenge:

1. Edit files in the `build/` directory
2. Rebuild the container:
   ```bash
   docker-compose up -d --build
   ```

## 🎨 Customization

This challenge has been personalized with:
- Custom branding (poeency)
- Modern gradient UI design
- Vietnamese language support
- Improved user experience with animations

## 📞 Support

If you encounter any issues, please check:
- Docker is running
- Port 37821 is not in use by another application
- You have proper permissions to run Docker

## 🏆 Have Fun!

Good luck solving the challenge! May the flags be with you! 🚀

---
Created with ❤️ by poeency
