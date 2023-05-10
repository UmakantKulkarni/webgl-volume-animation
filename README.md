# WebGL Volume Animation

Play back 3D volumetric time series data.
[Try it out online!](https://www.willusher.io/webgl-volume-animation/#url=https://cdn.willusher.io/webgl-volume-animation-data/urllist.txt)

## Data Format

Timesteps should be stored as an image stack in a zip files. Supported image types
are webp (in the future maybe png, jpg, etc). The zip structure should be:

```
data.zip:
- <prefix>0000.webp
- ...
- <prefix>####.webp
```

Where `<prefix>` is any string prefix.

Multiple timesteps can be loaded by uploading a set of zip files or providing a text file
which has the URL of each timestep. The text file should have one URL per line:

```
https://.../timestep000.zip
...
https://.../timestep###.zip
```

## Running

After cloning the repo run

```
npm install
```

To install webpack, then you can run the serve task and point your browser to `localhost:8080`:

```
npm run serve
```

Where you should see the page shown below.

To deploy your application, run:

```
npm run deploy
```

Then you can copy the content of the `dist/` directory to your webserver. You can build a development
distribution by running `npm run build`.


Install python library pillow to convert png to webp:

```
pip3 install -U pillow
```

Create Zip files from folders:

```
zip -r <output_file> <folder_1> <folder_2> ... <folder_n>
zip -r temp.zip Documents
```

NGINX configuration: https://docs.unity3d.com/Manual/webgl-networking.html

```
server {
    listen        192.168.0.141:80;

    add_header 'Access-Control-Allow-Origin' 'http://192.168.0.141:9000';
    add_header 'Access-Control-Allow-Credentials' 'true';
    add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS';
    add_header 'Access-Control-Allow-Headers' 'DNT,X-CustomHeader,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Authorization';

    location / {
    autoindex on;
    root  /tmp/ply2las/longdress/webgl-volume-animation-data;
    }

}
```
where 'http://192.168.0.141:9000' is the npm/webpack server URL.


Restart NGINX:

```
sudo systemctl restart nginx
```
