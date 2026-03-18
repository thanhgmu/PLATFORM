# PLATFORM — Deploy to VPS

## 1) Prepare env

```bash
cp .env.example .env
nano .env
```

Update at minimum:
- `SECRET_KEY`
- `SUPERADMIN_EMAIL`
- `SUPERADMIN_PASSWORD`
- storage credentials if you are not using the default MinIO setup

## 2) Build and start

```bash
docker compose up -d --build
```

## 3) Check health

```bash
curl http://127.0.0.1/health
curl http://127.0.0.1/ready
curl http://127.0.0.1:8000/api/v1/agents
curl http://127.0.0.1:8000/api/v1/cases
```

## 4) Check logs

```bash
docker compose logs -f backend
docker compose logs -f gateway
docker compose logs -f postgres
```

## 5) Rebuild after repo update

```bash
git pull origin main
docker compose down
docker compose up -d --build
```

## 6) Roll back fast

```bash
git log --oneline -n 5
git checkout <old_commit>
docker compose down
docker compose up -d --build
```
