# EDA-web-app-built-with-streamlit-deployed-using-docker

## Not sharing the code on GitHub. Check the Video Demo. Link provided at the bottom of this page

* Build docker image from containing our streamlit app

````console
  sudo docker build . -t iris_web_app
````

![Docker Build](https://github.com/deepankarkotnala/EDA-web-app-built-with-streamlit-deployed-using-docker/blob/master/images/docker_build.png)

* Docker Build Completed Successfully

![Docker Build_Complete](https://github.com/deepankarkotnala/EDA-web-app-built-with-streamlit-deployed-using-docker/blob/master/images/build_complete.png)


* Checking the Docker Images

![Docker Images](https://github.com/deepankarkotnala/EDA-web-app-built-with-streamlit-deployed-using-docker/blob/master/images/docker_images.png)

* Create a writable Container layer by running the Docker Image. This will start our streamlit app.

![Docker Container](https://github.com/deepankarkotnala/EDA-web-app-built-with-streamlit-deployed-using-docker/blob/master/images/docker_run.png)


* Check our app on localhost:8080

![Streamlit App](https://github.com/deepankarkotnala/EDA-web-app-built-with-streamlit-deployed-using-docker/blob/master/images/running_app.png)

Here's a [link](https://github.com/deepankarkotnala/EDA-web-app-built-with-streamlit-deployed-using-docker/blob/master/images/Demo.mkv?raw=true) to download a video explaining the working of this app.

