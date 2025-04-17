FROM node:18

WORKDIR /app

# Crear package.json básico si no usaste Angular CLI
RUN if [ ! -f package.json ]; then echo '{"name":"gym-frontend","version":"1.0.0","scripts":{"start":"ng serve --host 0.0.0.0 --port 4200 --disable-host-check"},"dependencies":{"@angular/common":"^16.0.0","@angular/core":"^16.0.0"}}' > package.json; fi

# Instalar Angular CLI globalmente
RUN npm install -g @angular/cli

# Si existe package.json, instalar dependencias
RUN if [ -f package.json ]; then npm install; fi

# Si no existe src/, crear un proyecto básico
RUN if [ ! -d src ]; then ng new . --routing --style=scss --skip-git --skip-install; npm install; fi

EXPOSE 4200

CMD ["npm", "start"]