FROM node:20.10-alpine

WORKDIR /usr/src/app

RUN rm -rf /usr/src/app/node_modules
RUN mkdir -p /usr/src/app/node_modules
RUN chown -R root:root /usr/src/app

RUN yarn global add @vue/cli

USER root

COPY ./vuejs/package*.json ./vuejs/yarn.lock ./
RUN yarn install --frozen-lockfile --check-files

COPY --chown=root:root ./vuejs/ /usr/src/app/