FROM node:18

WORKDIR /app/frontend

COPY ./frontend/package*.json ./
RUN npm install

COPY ./frontend/ ./
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "50000"]

EXPOSE 50000