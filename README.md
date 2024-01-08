## Tech stack
- [ ] Node JS v20.10
- [ ] FastAPI
- [ ] Docker
- [ ] Web part (Yarn 1.22.17 + Vite v5.0.11 + VueJS 3.3.11)

## Init project
```commandline
docker compose build
docker compose up
```

## Available URL
```
# API endpoint
http://localhost:8008/calculate/

# GUI
http://localhost:8080/
```

## If something happens with the GUI you can check the solution using a direct API request
```commandline
http://localhost:8008/calculate/?value_a=2&value_b=5&target=200&method=newton
http://localhost:8008/calculate/?value_a=2&value_b=5&target=200&method=fsolve
```

## Notice
Keep in mind to get expected in requirements value "3.258144456" need to provide a target value equal to the "200.0003598"