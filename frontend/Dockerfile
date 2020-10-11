FROM node:14.13.1 AS builder

#############
# Arg & Env #
#############

ENV PROJECT_NAME frontend
ENV PROJECT_PATH /app

#########################
# Build APP             #
#########################

WORKDIR ${PROJECT_PATH}


RUN npm set registry https://registry.npmjs.org/

COPY ./ ./
RUN npm install

RUN npm run-script build

#########################
# Serve APP             #
#########################

FROM nginx

ENV PROJECT_NAME frontend
ENV PROJECT_PATH /app

COPY --from=builder ${PROJECT_PATH}/dist /usr/share/nginx/html
COPY ./nginx.vue.conf /etc/nginx/conf.d/default.conf


