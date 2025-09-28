FROM oven/bun:1 as base
WORKDIR /app

FROM base as builder

COPY package.json bun.lock ./
RUN bun i
COPY . .

RUN bun run build
FROM joseluisq/static-web-server:2

COPY --from=builder /app/dist /dist
CMD ["--port","3000","--root","dist"]