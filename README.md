# Gutenberg Database Clone

Welcome to the Gutenberg Database Clone project! 📚

This project aims to create a clone of the Gutenberg project by utilizing their database dump. Gutenberg, named after the famous inventor of the printing press, is a digital library offering over 60,000 free eBooks, covering a wide range of genres and subjects. By cloning their database, we aim to provide developers and enthusiasts with a locally accessible version of the Gutenberg project for experimentation, analysis, and integration into their own projects.

## Features

- **Database Clone**: Utilize the Gutenberg project's database dump to recreate a local version of their digital library.
- **Offline Access**: Access the vast collection of over 60,000 free eBooks offline for research, analysis, or reading pleasure.
- **Exploration and Analysis**: Analyze the Gutenberg dataset to gain insights into literary trends, popular genres, and authorship.
- **Integration**: Integrate the cloned Gutenberg database into your own applications, projects, or research endeavors.
- **Contributions**: Contribute to the project by enhancing the database clone, improving accessibility, or adding new features.

## Database Model

This project utilizes the Gutenberg database dump, consisting of the following tables:

- **Author**: Contains information about authors of the eBooks.
- **Language**: Stores information about the languages in which the eBooks are available.
- **Bookshelf**: Represents bookshelves containing collections of eBooks.
- **Subject**: Stores subjects or categories of eBooks.
- **Format**: Contains links and media types for each eBook.
- **Book**: Represents individual eBooks and includes Many-to-Many relationships with authors, subjects, bookshelves, and languages.

Additionally, the project utilizes the Django `User` model, which utilizes an abstract table from the Django contrib auth app.

## Getting Started

To prepare the database for use, follow these steps:

1. Clone the repository to your local machine.
2. Run the following commands, This will populate all the necessary tables with data.:
   ```bash
   python3 manage.py migrate
   python3 manage.py populate_db  
   ```
3. To clean the database, run: 
   ```bash
   python3 manage.py clean_db
   ```
python3 manage.py clean_db

This command will truncate all the tables and remove the data.

## Contribution Guidelines
We welcome contributions from developers, researchers, and enthusiasts alike! If you'd like to contribute to the Gutenberg Database Clone project, please follow these guidelines:

- Fork the repository and create a new branch for your contribution.
- Ensure your code follows the project's coding standards and conventions.
- Submit a pull request with a clear description of your changes and their purpose.
- Participate in discussions, code reviews, and issue tracking to help improve the project collaboratively.

## License
This project is licensed under the MIT License, which allows for free use, modification, and distribution of the software.



serializers : how are we handling many to many fields 
filters : how are we filtering data 
views : how are we presenting it to user (throttling, pagination, permissions, order) 
tests: What all things are tested and why 
3rd party libraries we are using and why 
code documentation : what tools are we using for that. 
query optimization and performance 
docker and deployment guide 
N+1 queries problem and its solution 
load testing 
12 factor app 
django best practices that this project follows. 
environment separation 
api documentation 
continuous integration and deployment pipeline. 
latency 
django coding principle and philosophies. 