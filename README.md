### Instructions

To run, ensure that the PySide6 library is installed, then run **main.py**.  **cell_count.db** is not needed to run the program as it will be created on run.

### Database

I just entered the data into a database using SQLite. I only created one table, organized exactly how the data is presented in the csv. I did this as the simple solution with plans to revisit and it would not scale the best as when there are lots of samples with tons of projects. If I had more time, I may have tried to organize the data a little more by separating into projects, subjects, and samples.

### Code Structure

I wrapped all of my SQLite into a wrapper class **Database** and treated that as the Model. For the View and Controller, I used PySide6 (Qt for python). This keeps decent MVC even though Qt combines the View and Controller. To be honest it got a bit messy in the main file. Each window probably should have gotten its own file to keep better separation, but I was working to get this submitted as soon as possible because I am turning it in later than I should have.

### Note

When adding or removing samples from the database, the table does not automatically update. If you open the melanoma window after adding/removing one then it should show up there. Obviously this isn't the prettiest thing or the easiest to use but those are all things that can be improved upon in the future. All of the functionality is there and working and that is what I was prioritizing since I wanted to resubmit as soon as possible. Any notes or feedback that you have would be greatly appreciated as I am always looking to learn. Thank you for your time and consideration.
