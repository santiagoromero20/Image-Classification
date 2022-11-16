# **Image Classification**

The main goal of this project was te get familiar with other steps of  ML project. Here I focused mostly on the Deploymeny and Testing. I used an already trained model, Resnet, to classifiy images. And also developed the Api with Flask.

![Alt ](img/armadillo.jpeg "Title")
## **Motivations**

It is well known that once you have trained your model it is time to put it in "action". You have to integrated into a system, mantain and re-train it (between other thinigs...).
This lead me to the idea of building this ML project which focus more on the tasks previously menioned.
## **Technologies and Teachings**

This project was full of new Teachings and Technologies. As I mentioned before, the focus was put in the Deployment. To code the Api I used the MicroService **Flask** and for the Front-end **HTML**. 

Then, **Redis** was used as an in-memory data structure store, and a communicator between the Api and Model services. It was very useful to mantain the clarity and tidynees of the project.

Once the project was finished, a Stress Testing (when you test how much users the Api can handle well) was done with **Locust**. You can read the Report.md file (inside the stress_test folder) to see the results I got.

Finally, a very powerful tool was used among the whole project. If you go through it you can see that each service is containerized, with its own on requeriments and dependencies on the Dockerfile.
By now you know that I am talking about **Docker**.

## **Install and run**

To run the services using compose:

```bash
$ docker-compose up --build -d
```

To stop the services:

```bash
$ docker-compose down
```

# **Tests**

### **Integration end-to-end**

You must have the full pipeline running and [requests](https://docs.python-requests.org/en/latest/) library installed. Then, from this project root folder run:

```
$ python tests/test_integration.py
```

### **Modules**

We make use of [multi-stage docker builds](https://docs.docker.com/develop/develop-images/multistage-build/) so we can have into the same Dockerfile environments for testing and also for deploying our service.

#### **Api**

Run:

```bash
$ cd api/
$ docker build -t flask_api_test --progress=plain --target test .
```

You will only need to pay attention to the logs corresponding to the testing code which will look like this:

```bash
#10 [test 1/1] RUN ["pytest", "-v", "/src/tests"]
#10 sha256:707efc0d59d04744766193fe6873d212afc0f8e4b28d035a2d2e94b40826604f
#10 0.537 ============================= test session starts ==============================
#10 0.537 platform linux -- Python 3.8.13, pytest-7.1.1, pluggy-1.0.0 -- /usr/local/bin/python
#10 0.537 cachedir: .pytest_cache
#10 0.537 rootdir: /src
#10 0.537 collecting ... collected 4 items
#10 0.748
#10 0.748 tests/test_api.py::TestIntegration::test_bad_parameters PASSED           [ 25%]
#10 0.757 tests/test_api.py::TestEnpointsAvailability::test_feedback PASSED        [ 50%]
#10 0.769 tests/test_api.py::TestEnpointsAvailability::test_index PASSED           [ 75%]
#10 0.772 tests/test_api.py::TestEnpointsAvailability::test_predict PASSED         [100%]
#10 0.776
#10 0.776 ============================== 4 passed in 0.24s ===============================
#10 DONE 0.8s
```

You are good if all tests are passing.

#### Model

Same as api, run:

```bash
$ cd model/
$ docker build -t model_test --progress=plain --target test .
```

## **Final Comment**

I invite you to read the TableOfContents.md file to gain a wider and clearer idea of the project. Hope you enjoy and learn from it as I have done!
```
