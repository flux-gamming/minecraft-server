# Running the minecraft server
java -Xms2g -Xmx2g -jar minecraft_server.1.15.2.jar nogui &

# Running ngrok for TCP tunneling
unzip ngrok-stable-linux-amd64.zip
sudo ./ngrok authtoken ${{ secrets.AUTHTOKEN }}
sudo ./ngrok tcp 25565
