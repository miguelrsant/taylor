kill-ports:
	-lsof -t -i:3030 | xargs -r kill -9 2>/dev/null || true
	-lsof -t -i:3000 | xargs -r kill -9 2>/dev/null || true
	-lsof -t -i:8000 | xargs -r kill -9 2>/dev/null || true
	-lsof -t -i:5432 | xargs -r kill -9 2>/dev/null || true

	-docker stop $$(docker ps -q --filter "publish=3030") 2>/dev/null || true
	-docker stop $$(docker ps -q --filter "publish=3000") 2>/dev/null || true
	-docker stop $$(docker ps -q --filter "publish=8000") 2>/dev/null || true
	-docker stop $$(docker ps -q --filter "publish=5432") 2>/dev/null || true
dev: kill-ports
	cp .env.dev .env
	cp .env.dev ./frontend/.env
	docker compose -f docker-compose.yml up -d --build db
	cd backend && pdm run flask --app main.py db upgrade -d database/migrations
	cd backend && pdm run gunicorn main:app -b 0.0.0.0:8000 &
	cd frontend && npm run dev
	
build: kill-ports
	cp .env.build .env
	docker compose up -d --build


restart: kill-ports
	docker compose down -v &
	docker system prune -a --force &
	docker volume prune -a --force