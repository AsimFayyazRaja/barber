echo "This will stop and remove barber-task container, then remove barber-task image, and run"

echo "Stoping docker for barber-task...."
sudo docker stop  barber-task

echo "Removing docker for barber-task...."
sudo docker rm  barber-task

echo "Removing docker image for barber-task...."
sudo docker image rm  barber-task:latest

echo "Building docker image for barber-task...."
sudo docker build -t barber-task:latest -f Dockerfile .

echo "Running docker image for barber-task...."
sudo docker run -d --name barber-task --restart=always -p 3000:3000 barber-task:latest --network=host