# Running the application from command prompt or terminal

Please install required packages before you begin

```
cd app

pip install -r requirements.txt
```

Use http://localhost:5000/ for local deployment.

```
cd app

python main.py
```

# Run Unit test from app folder

```
cd app

python -m unittest discover -s ./app/tests
```

# Run application using docker

Use http://0.0.0.0:5000/ for docker deployment.

```

cd app

docker build -f ../docker/Dockerfile-deploy -t exoplanet:latest .

docker run --rm -p 5000:5000 exoplanet

```

# Run unit tests using docker

```
cd app

docker build -f ../docker/Dockerfile-test -t exoplanet:latest .

docker run --rm -p 5000:5000 exoplanet
```

# Deploy using Kubernetes


First build the application container using docker.

```
cd app

docker build -f ../docker/Dockerfile-deploy -t exoplanet:latest .

```

Then run kubernetes deployment. 

```
cd app

kubectl apply -f ../kubernetes/deployment.yaml 

```

The kubernetes will deploy the image built by docker as per the specification in the deployment file and the created service will expose the deplyment with Load balancers.

The application can be accessed using the service end points and port number.




