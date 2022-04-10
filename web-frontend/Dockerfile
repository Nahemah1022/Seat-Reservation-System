FROM node:lts-alpine as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM bitnami/nginx:latest

COPY --from=build-stage /app/dist /app
COPY ./nginx.conf /opt/bitnami/nginx/conf/server_blocks/frontend.conf