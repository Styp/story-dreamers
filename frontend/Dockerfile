FROM node:18-alpine as builder

WORKDIR /app/
COPY package*.json /app/

RUN npm ci

COPY . /app/
RUN npm run build

FROM nginx:alpine

COPY --from=builder /app/dist/ /usr/share/nginx/html