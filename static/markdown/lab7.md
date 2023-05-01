# Lab 7: Automated Web Interactions with Selenium

## Introduction

In this lab, we will be using the application [Postman](https://www.postman.com/downloads/) to better understand the HTTP requests being made to the server. Postman is a tool that allows you to make HTTP requests to a server and see the response. It is a great tool for debugging and testing APIs. We will also set up the basic tools you need to start web scraping and automated interactions with web pages using the [Selenium](https://www.selenium.dev/) library.

## Task 1: Installations

- Use `pip` to install all dependencies from `requirements.txt` as we did in previous labs.
- Download and install Postman from [here](https://www.postman.com/downloads/).
- Download the [ChromeDriver](https://chromedriver.chromium.org/downloads) for your operating system and the current version of Chrome (you can check your Chrome version by going to `chrome://settings/help` in your browser).
  - **HINT**: You might need to unzip the file after downloading it.
- Complete `TODO 1` by placing your ChromeDriver in the `chromedriver` folder in this lab.
  
## Task 2: Create New Collections and Requests in Postman

- Open the Postman application
  - **TIP**: You do not need to create an account. Select the `Skip getting started` option at the bottom.
  - ![example](./images/postmanStart.png)
- Select the `Create new collection` option in the left sidebar, and name it `3155_Selenium_Lab_Your_Name` (e.g., 3155_Selenium_Lab_David_Gary).
  - ![example](./images/postmanCreateCollection.png)

- Click the `New` button in the top left corner of the Postman window.
  - ![example](./images/postmanNew.png)
- Select the `HTTP Request` option.
  - ![example](./images/postmanHTTP.png)
- Enter "https://www.indeed.com/jobs" in the `Enter request URL` field and set it as a `GET` request.
  - ![example](./images/postmanRequestURL.png)
- Add two key value pairs to the "Params" section of the request:
  - `q` with the value `Software Engineer`
  - `l` with the value `Charlotte`
- Click the "Send" button to send the request.
- Preview the response in the `Preview` tab, screenshot this, and save it for submission later in the lab.
  - ![example](./images/postmanResponse.png)
- Import this as Python code using the `requests` library by clicking the `Code` button in the right sidebar and selecting `Python - requests` from the dropdown menu.
  - ![example](./images/postmanCode.png)
- Complete `TODO 2` by copying the code and pasting it to finish the `indeed_request` function of the `requesting.py` file.

## Task 3: Introduction to `requests` and `selenium`

- Complete `TODO 3` by simply running the `requesting.py` file and viewing the response.
- Complete `TODO 4` by simply running the `starter.py` file and viewing the response.

## Task 4: Finding the Information to Scrape

- Open the `search.py` file.
- Complete `TODO 5` in the `scrape_book_titles` function by using the `get` method built into the selenium driver to navigate to the Indeed website.
  - **HINT**: See `starter.py` for an example of how to use the `get` method.
- Complete `TODO 6` by using the correct method to find a group of elements on the page. The documentation for locating elements can be found [here](https://selenium-python.readthedocs.io/locating-elements.html).
  - **HINT**: For an example of how to find the correct element name, see this week's lab introduction video.
- Complete `TODO 7` by looping over the books on each page and using the correct methods to find and storing their **FULL** titles into the `book_titles` list.
  - **HINT**: The `get_attribute` method might be useful here, but you can also use the `text` attribute. See this [documentation link](https://selenium-python.readthedocs.io/api.html) for more information.

## Submission Details

- On Canvas, submit the following:
  - A zip file of the entire `lab7` directory, renamed as your NinerNetID.zip (e.g., dgary9.zip)
    - **TIP:** If you are struggling to remember how to zip your submission, here's an example of how to do it from the terminal on Mac or Linux machines: `zip -r -X dgary9.zip .`
    - **TIP:** For Windows users who want to use their terminal to zip their submission, you can use the `7za` command. Here's an example of how to do it: `7za dgary9.zip .`
    - **NOTE:** In the above examples, `dgary9` is the NinerNetID of the student submitting the assignment and `.` is the directory that contains the files to be zipped, which is the current directory (`lab7`) in this case.
