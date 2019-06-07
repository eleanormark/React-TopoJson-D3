## Challenge Summary

At Amino, we work with a number of different externally-provided datasets in order to build a clear picture of the American healthcare system. Whenever we get a new dataset in, we go through a process of exploratory data analysis to understand what is in the data, and how comprehensive the coverage is.

A cornerstone of many of our products is our data about physicians. One public source of data about physicians comes from the [Physician Compare](https://data.medicare.gov/data/physician-compare) dataset, provided by the Centers for Medicare & Medicaid. 

Imagine for the purposes of this exercise that you are one of the first web developers at Amino, and you have been asked create a geographic visualization that would allow others in the company to understand how the physicians represented in this source are distributed acoss the country, by specialty.

We have provided the basic application for a backend server that has access to a database populated from a subset of this Physician Compare file; your task is to enhance the application to implement a frontend UI running in a browser, a new API endpoint to support it, and tests to exercise your backend code.

If you have any questions about this challenge or run into external issues preventing you from completing it, shoot an email to [coding.challenge@amino.com](mailto:coding.challenge@amino.com).

## Submission Requirements

Create your implementation in a branch called "feature/challenge-solution". When you are done, open a pull request against the `master` branch in your repository, and tag [@NickDunkman](https://github.com/NickDunkman/) in the PR.

In your PR description, please describe at a high level the approach you took, and anything else that you feel would be helpful for us to know as we evaluate your solution.

If you have any questions about this challenge or run into external issues preventing you from completing it, shoot an email to [coding.challenge@amino.com](mailto:coding.challenge@amino.com).

## Application Requirements

The basic application provided has been set up to run in a [Docker](https://www.docker.com/) container, with a Makefile that contains commands to build, test, and run the backend server.

The backend server is written in [Python 3.7](https://docs.python.org/3/), using [Flask](http://flask.pocoo.org/). If you are not very experienced with Python, don't worry, there should be a lot of contextual clues within the application provided that should allow you to get jump-started.

To set up Docker and get the application running, [consult these instructions](./environment.md).

### Existing Backend

The existing backend uses Flask and SQLAlchemy. If you are not familiar with Flask, it is a microframework for Python roughly analagous to Ruby's [Sinatra](http://www.sinatrarb.com/) or Node's [Express](http://expressjs.com/). Data is stored using a [sqlite](https://sqlite.org/about.html) database, accessed using [SQLAlchemy](http://www.sqlalchemy.org/) as an ORM. Both Flask and SQLAlchemy are very thoroughly documented:

- [Flask Documentation](http://flask.pocoo.org/docs/0.11/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/latest/)

The current endpoints implemented in this application are:

**GET /**

Return the HTML / web view for the map. (You should replace this output of this endpoint with your frontend solution.)

**GET /specialties?size=:num**

Returns a list of the top specialties for the toolbar to display.

Parameters:

- *size*: optional, max number of specialties to return in results. (int, >= 0)

HTTP Codes:

- 200 if successful
- 400 if an invalid size parameter

Example Success Output:

```javascript
{
   "specialties": [
      "INTERNAL MEDICINE",
      "EMERGENCY MEDICINE",
      "FAMILY PRACTICE",
      // ... etc.
   ]
}
```

Example Failure Output:

```json
{
   "error": "'size' must be a positive int"
}
```


### New Frontend Requirements

The application frontend has the following requirements:

1. The UI should display a map of the United States, with the default view being a visual summarization of how physicians are geographically distributed across the map, by state.
2. The UI should provide a tool that allows you to narrow down the summary to show information for providers filtered by a particular Primary Specialty.
3. The UI must run in a web browser. Don't stress trying to make it run in all browsers, just test it in the latest version of whatever browser you are most comfortable in, and let us know which you used.

Notes:

- We don't expect you to re-invent the wheel with this -- feel free to use existing open-source visualization or mapping libraries to help here.
- A TopoJSON files for US states, along with a mapping between IDs and two-letter State codes can be found in the `app/data` folder of this repository.

### New Backend Requirements

To support your application, you should implement this additional interface:


**GET /physician-counts?specialty=:specialty_name**

Returns a by-state summary for the count of physicians that match our parameters.

Parameters:

- *specialty*: name of specialty. If this parameter is passed, the counts returned by this endpoint should be restricted to only physicians who belong to this particular specialty. (optional, case-insensitive string)

HTTP Codes:

- 200 if successful
- 400 and an error message if passed a non-existent specialty parameter

Success Output Format:

```javascript
{
   "physicians": [
      {
         "state": "CA",
         "count": 12345
      },
      {
         "state": "NY",
         "count": 12346
      },
      // ... etc.
   ]
}
```

Failure Output Format:

```json
{
   "error": "Specialty 'abc' does not exist"
}
```

Please write tests for this endpoint that get exercised when running `make test`.



## Halp!

If you have difficulty getting things up and running, or any other technical issues that impede your ability to complete this exercise, please email us at [coding.challenge@amino.com](mailto:coding.challenge@amino.com).
