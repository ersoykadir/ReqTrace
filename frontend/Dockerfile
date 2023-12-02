FROM node:latest
WORKDIR /app
# Layer for dependencies
COPY package*.json ./
RUN npm install
# Layer for source code
COPY src ./src
# Layer for packaging
# RUN npm run build
# RUN cd dist
# ENTRYPOINT ["npx", "serve"]
# there seems to be a bug in the build process, scripts are missing
# Will debug later, for now just run the server

EXPOSE 1234

ENTRYPOINT ["npm", "start"]
