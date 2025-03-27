FROM node:14.8.0-alpine3.12

WORKDIR .

COPY package.json ./
COPY package-lock.json ./

RUN npm install
RUN npm install react-scripts@3.4.3 -g


RUN npm install grpc-web
RUN npm install grpc

#RUN npm install grpc
#RUN npm install @grpc/proto-loader

#RUN npm install @grpc/proto-loader
#RUN npm install @grpc/grpc-js
##RUN npm install http2

COPY . .

EXPOSE 3000

CMD ["npm", "start", "--debug"]

