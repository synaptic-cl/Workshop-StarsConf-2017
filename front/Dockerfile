FROM node:6.11-alpine

WORKDIR /data
ADD package.json package.json
RUN npm install --dev

WORKDIR /src
ENV NODE_PATH=/data/node_modules
ENV PATH=/data/node_modules/.bin:$PATH
CMD ["npm", "run", "dev"]
