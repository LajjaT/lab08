# Lab 08 - File Input/Output, Testing

In this lab, we'll learn how to create classes, unit test those classes and their functions, as well as file input and output.

## Getting Started

Be sure that you have accepted the assignment invitation within GitHub Classroom (by clicking on the link provided in the lab assignment on Canvas), before you proceed.  You want to clone your own copy of the repository (not the original, since you can't write to that repository).  The command to do so will look something like this:

```
git clone https://github.com/CSCI1030U/lab08-rana-muniz
```

Be sure to change directory to a place where the rest of your CSCI1030U labs are stored, first, so that this command copies your lab assignment starter code into the proper place.

## Instructions

In this lab, you will write the `lab08.py` files so that it meets the requirements described in the following sections.  This file has no basic code to start, and it will be up to you to write all of the code for this lab.

#### Part 1

The data to be used will come from Toronto's Open Data Portal:

- https://open.toronto.ca/dataset/apartment-building-evaluation/

However, I've modified a version of this file to make it easier to process.  The file can be found in the same directory as this lab, and is called `apartment_building_evaluation.csv`.

The criteria you want to use to search are:

1. Number of stories (column index 2)
2. Number of units (column index 3)
3. Overall score (column index 24)

Write a Python function, called `load_matching_data()`, that loads all of the data from this file, but only keeps a summary for each apartment that matches the criteria.  The function takes the following arguments:

- `min_score` - the minimum score you will allow for the apartment building
- `min_stories` - the minimum number of stories that you want in the building
- `min_units` - the minimum number of units that you want in the building

The function will return a list of dictionaries, one for each apartment building that matches the above criteria.  The resulting dictionaries will include the three fields used to filter the apartment buildings above, plus one more:

4. Address (column index 26)

Each dictionary will look like this:

```python
[
  {'address': '252  VICTORIA ST ', 'score': 95.0, 'num_stories': 37, 'num_units': 337},
  ...
]
```

The following code will allow you to test your `load_matching_data` function:

```python
results = load_matching_data(85, 28, 300)
print(results)
print(len(results))
```

You can include some test code for your function, or you can exclude it when you submit.  The function itself will be all that is tested.

#### Part 2

Write a Python function, called `save_summary`, which takes a list of dictionaries, exactly like the output of the `load_matching_data` function, and writes it to a JSON file called `apartment_summary.json`.

The contents of this file will be exactly like the following:

```python
[
    {'address': '252  VICTORIA ST ', 'score': 95.0, 'num_stories': 37, 'num_units': 337},
    {'address': '320  TWEEDSMUIR AVE ', 'score': 93.0, 'num_stories': 30, 'num_units': 336},
    {'address': '570  BAY ST ', 'score': 100.0, 'num_stories': 29, 'num_units': 463},
    {'address': '77  DAVISVILLE AVE ', 'score': 90.0, 'num_stories': 30, 'num_units': 483},
    {'address': '85-95  THORNCLIFFE PARK DR ', 'score': 93.0, 'num_stories': 43, 'num_units': 500},
    {'address': '561  SHERBOURNE ST ', 'score': 99.0, 'num_stories': 43, 'num_units': 369},
    {'address': '140  ERSKINE AVE ', 'score': 98.0, 'num_stories': 29, 'num_units': 493},
    {'address': '167  CHURCH ST ', 'score': 98.0, 'num_stories': 28, 'num_units': 388},
    {'address': '22  JOHN ST ', 'score': 99.0, 'num_stories': 31, 'num_units': 369},
    {'address': '85-95  THORNCLIFFE PARK DR ', 'score': 94.0, 'num_stories': 43, 'num_units': 496},
    {'address': '45  DUNFIELD AVE ', 'score': 91.0, 'num_stories': 30, 'num_units': 575},
    {'address': '6  FOREST LANEWAY  ', 'score': 91.0, 'num_stories': 29, 'num_units': 406},
    {'address': '118  BALLIOL ST ', 'score': 86.0, 'num_stories': 30, 'num_units': 342},
    {'address': '500  DUPLEX AVE ', 'score': 87.0, 'num_stories': 33, 'num_units': 319},
    {'address': '15  ROEHAMPTON AVE ', 'score': 100.0, 'num_stories': 36, 'num_units': 466}
]
```

Example usage of this code is provided below:

```python
results = load_matching_data(85, 28, 300)
save_summary(results, 'apartment_summary.json')
```

An example of the proper output, which corresponds exactly to what your code should produce for the test code in Code Listing 2, has been also included in this lab folder, with the filename `expected_apartment_summary.json`.

You can include some test code for your function, or you can exclude it when you submit.  The function itself will be all that is tested.

## Verifying Correctness

Run the pre-written tests that verify that your lab assignment code passes, using the following command:

```
pytest
```

Examine the output closely.  There should be hints about what went wrong, if any of the tests fail.  If you are struggling to figure it out, you can always ask for help (see __Getting Help__ for details).


## Getting Help

If your code does not work, there is always a lab instructor present during your lab period for assistance.  Them not having to mark lab assignment submissions means that they should have plenty of time to ensure that you are able to get your lab assignment submission working by the end of the lab period.

_**Note:** The lab instructor is likely to help you figure out what is wrong with your code, rather than tell you how to fix it directly.  The goal is for you to learn how to diagnose and fix your bugs on your own._


## How to Submit

First, ensure that your code passes the tests (see the section __Verifying Correctness__ for details).  If you are certain that your code passes all of the tests, then you can submit your work using the following commands:

```
git add --all
git commit -m "Lab 08 completed code"
git push origin main
```

Once you have submitted your work, you can also double check that your auto-grading was successful by clicking on the `Actions` tab in your repository page on GitHub.  Sometimes, this takes a few minutes to complete, so please be patient.
