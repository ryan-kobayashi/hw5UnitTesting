# hw5UnitTesting

Backend and frontend unit tests are completed using the backend and frontend code
linked [here](https://github.com/LaughingPenguin/mymusiclist).

## Problem 2

To run the unit tests necessary for problem 2, you first must ensure that you have pytest installed. Do this by running, in a terminal,
```
pip3 install pytest
```
Then, still in the terminal, navigate to the `Problem-2` directory and run:
```
pytest unit_testing.py
```
Here is a screenshot of the tests that were provided in problem 1:

<img width="870" alt="Screen Shot 2023-12-07 at 11 50 04 PM" src="https://github.com/ryan-kobayashi/hw5UnitTesting/assets/131481979/3ae1cf80-f201-456e-b088-262ee88cd98c">

## Problem 3

There are several dependencies that are needed to run `test.php`. Install PHPUnit and Guzzle through homebrew and Composer.
1. Install PHPUnit and Composer.
    ```
    brew install phpunit composer
    ```

2. Initialize Composer in the root folder of the backend code, where `index.php`
is located.
    ```
    composer init
    ```
    During the setup process, make sure to define `phpunit/phpunit` in your dev dependecies.
    The specific prompt states, "Would you like to define your dev dependecies (require-dev) interactively? [yes]?"
    Type in "yes".

3. Install Guzzle.
    ```
    composer require guzzlehttp/guzzle
    ```

4. Create a `/test` folder inside your backend root folder. Move `Problem-3/tests/test.php` to
inside of that folder. Configure your backend server to port 8080. Make sure that your local
database is set up according to the instructions provided in the linked GitHub above.

5. Run the unit tests from the backend root folder.
    ```
    ./vendor/bin/phpunit tests/test.php
    ```

## Problem 4

There are several dependecies that are needed to run `signUpView.test.js` and `loginView.test.js`.
1. Install the necessary dependecies in the root project folder.
    ```
    npm install --save-dev jest @testing-library/react @testing-library/jest-dom
    ```
2. Your `package.json` should be updated to include the new dependecies. Add the following code to `package.json` so
that it works properly with axios.
    ```
    "jest": {
        "moduleNameMapper": {
        "axios": "axios/dist/node/axios.cjs"
        }
    }
    ```
3. Move `singUpView.test.js` and `loginView.test.js` into the `\views` folder. The files should be in the same subdirectory of where `signUpView.js` and `loginView.js` are located.
4. Run the unit tests from the frontend root folder.
    ```
    npm run test
    ```
## Problem 5
To see the continuous integration of tests using Github actions, you must navigate to the repository containing the frontend and backend code contained [here](https://github.com/LaughingPenguin/mymusiclist). From here, navigate to the actions tab where you can see our workflow runs. Here is a screenshot of one of our workflow runs:

<img width="1396" alt="Screen Shot 2023-12-07 at 11 10 52 PM" src="https://github.com/ryan-kobayashi/hw5UnitTesting/assets/131481979/df2bb914-d147-479f-9680-a10b83ee0c67">

## Problem 6
Recently, interest in chat bots such as ChatGPT or Bard and generative AI used to create images and code have exploded in popularity. This interest has made its way into tools for developers, such as Postman, which can aid engineers in writing code more efficiently.

Recently, a new feature called Postbot was implemented in Postman, which was described as an "AI assistant for all things API." Users may use Postman to add tests, write documentation, visualize responses, etc.

![Screenshot 2023-12-05 at 8 10 01 PM](https://github.com/ryan-kobayashi/hw5UnitTesting/assets/91140371/e475f053-df00-480c-ba9b-d8e74adf01e9)

For example, I can use Postman to send a GET request to my local backend server. Given an HTTP response, I can have Postman generate unit tests for that request in 2 clicks!

See a small sample of the results for yourself.
```
pm.test("Response status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Response has the required fields", function () {
    const responseData = pm.response.json();
    
    pm.expect(responseData).to.be.an('array');
    
    responseData.forEach(function(review) {
        pm.expect(review).to.have.property('id');
        pm.expect(review).to.have.property('username');
        pm.expect(review).to.have.property('song');
        pm.expect(review).to.have.property('artist');
        pm.expect(review).to.have.property('rating');
    });
});

pm.test("Username is a non-empty string", function () {
    const responseData = pm.response.json();
    
    pm.expect(responseData).to.be.an('array');
    responseData.forEach(function(item) {
        pm.expect(item.username).to.be.a('string').and.to.have.lengthOf.at.least(1, "Username should not be empty");
    });
});
```



## Authors
* Ryan Kobayashi
* Steven Xu

*Work distribution: 50/50*

---

*This site was designed and published as part of the COMP 333 Software Engineering class at Wesleyan University. This is a training exercise.*
