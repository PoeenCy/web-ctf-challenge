# Admin Guide - Poeency CTF Challenge

## 🎯 Challenge Information

- **Public URL:** http://100.93.221.59:53191
- **Port:** 53191
- **Flag format:** `poeency{...}`

## 🔧 Management Commands

### Start/Stop Challenge

```bash
# Start challenge
docker-compose up -d --build

# Stop challenge
docker-compose down

# Restart challenge
docker-compose restart

# View logs
docker-compose logs -f web

# Rebuild from scratch
docker-compose down -v
docker-compose up -d --build
```

### Change Port

```bash
# Stop current instance
docker-compose down

# Start with new port
PORT=8888 docker-compose up -d

# Or edit .env file
echo "PORT=8888" > .env
docker-compose up -d
```

## 📊 Current Challenge Info

### Admin Credentials (from last startup)
- Username: `admin`
- Password: Check logs with `docker-compose logs web`
- Secret Key: Check logs
- Flag Table: Check logs

### Flag
```
poeency{tenshi_appear_supprise!!!!}
```

## 🎮 For Participants

Share `README.md` with participants - it contains all necessary information for them to participate.

## 🛠️ Troubleshooting

### Check if container is running
```bash
docker ps | grep poeency_blind_sqli
```

### Check container logs
```bash
docker-compose logs -f
```

### Access container shell
```bash
docker exec -it poeency_blind_sqli sh
```

### Check database
```bash
docker exec -it poeency_blind_sqli sh -c "sqlite3 /app/store.db '.tables'"
```

### Reset everything
```bash
docker-compose down -v
rm -rf build/uploads/*
docker-compose up -d --build
```

## 📝 Solution

The solution is in `solution/exploit.py`. To run:

```bash
cd solution
# Update URL if needed
python3 exploit.py
```

## 🏆 Tracking Participants

Keep track of who solved the challenge:

1. _______________
2. _______________
3. _______________

## 🔒 Security Notes

- Admin password is randomly generated on each startup
- Flag table name is randomized
- Secret key is randomly generated
- Database is reset on container restart
