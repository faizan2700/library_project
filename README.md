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

This command will truncate all the tables and remove the data.

## Serializers 
1. This projects make use of serializers as it builds rest based backend of gutenberg project. There is book serializer, which converts all of its fields to json representation including many to many fields, I am using SerializerMethod field that uses class method to get all the author names and other many to many field and convert them to json format. 
2. There is no particular validation is required in this use case. 
3. For ordering fields correctly, meta class fields attribute is set properly. 
4. There are other serializers present in the file that can be used if instead of just object present string (author name, format url, etc.) we want to completely serializer the related object and use the nested serializer for presentation. 
5. tests for serializers will be added in tests directory, as of now there no particularly complicated calulations are happening to include in tests. 

## Filters 
1. We can filter books by multiple gutenberg_ids separated by comma and book objects will be returned if they match any value of the search filter. for example id=1,2,3 
2. we can filter books by multiple languages separated by comma, if book matches any language code it will be returned in the filtered objects. for example language=en,fr
3. We can filter books by multiple Mime type, if book matches any mime type it will be part of filtered query set. 
4. We can filter using multiple, partial and case insensitive author name. Lets say we have author John in the queryset, its book will be returned if we filter books with any criteria like jo, hn or such. Like this we can include multiple values in the filter criteria. 
5. We can filter using multiple, partial and case insensitive title of books. 
6. We can filter using mulitple topics. If topic of book includes substring of search criteria partially and case insensitively it will be part of filtered queryset. Set of topic includes all book shelf names and subject names of the books.   

## Views 
1. In response of API Call, we are passing list of books in response that contains book object with following fields: 
    - title of book 
    - information about author list  
    - language code list 
    - subject name list  
    - bookshelf name list 
    - list of links to download in different formats (MIME Types) 
2. If books are more than 20, in that case 20 book objects will be returned per page. Rest frameworks pagination class is being used for this. 
3. Books are ordered from highest number of downloads to lowest. 
4. Data is returned in JSON Format. 
5. Views also include filter class to filter books according to filter criteria as described above. 

## Test Coverage 
1. Test directory in main app contains all the test cases for following modules. 
    - apis 
    - filters 
    - models 
    - serializers 
    - urls 
2. Tests for apis tests that if apis are giving expected response. 
3. Tests for filters tests if filter classes are working in expected manner, it creates test db and insert some objects in it and runs filter on them and checks if filtered data is correct. 
4. Tests for models checks if we are able to create and delete objects successfully. And also checks if many to many fields and reverse relationship of many to many fields are working correctly. 
5. Currently there are no tests for serializers. 
6. Tests for urls checks if view name is resolved to correct url. 
7. Github action script is added for continuous integration pipeline that runs these tests for every push and pull request. 

## Query Optimization and Performance 
1. This project focuses on optimizing queries to ensure efficient database interactions. The primary optimization strategy involves minimizing heavy queries, particularly when fetching complete querysets of books from the database. To achieve this, the project utilizes prefetching to retrieve Many-to-Many fields along with the main queryset. This approach reduces the need for additional queries when serializing related objects.
2. Django Debug Toolbar is integrated into the project to monitor and analyze the number of queries executed during the processing of specific views. This tool provides valuable insights into query performance, allowing developers to identify and address potential bottlenecks or inefficiencies in the application's database interactions.
3. As the project evolves and scales, periodic performance profiling and optimization efforts may be conducted to identify areas for improvement and ensure continued optimal performance.
4. Consideration may be given to database schema design optimizations, such as denormalization or partitioning, to streamline data access and improve query performance in scenarios with large datasets or complex relationships. 

## API Documentation 
1. API documenation is prepared with Swagger API library. you can visit /swagger endpoints for the same afte running project. 
2. With Swagger UI, developers can test API endpoints in real-time, sending requests and examining responses without the need for external tools.

## Codebase Documentation 
1. Docstring are added in functions and classes for ease of readability and collaboration in this project. 
2. Currently no library is being used for generating documentation automatically, but we can use sphinx for that purpose. 

## Further Improvements 
1. We can use docker to containerize and manage this application. 
2. We can use Github actions to set continuous deployment pipeline in place. That will automatically deploy our application to server. 
3. We can Use third party tools like Open telemetry to get better insights to our database performance and metrics, we will be able to monitor each query that our application is performing on our database. 
4. We can separate environments like development, staging and production separating configurations. 
5. We can use 12 Factor app approach to improve the code quality of this app. 

## Contribution Guidelines
We welcome contributions from developers, researchers, and enthusiasts alike! If you'd like to contribute to the Gutenberg Database Clone project, please follow these guidelines:

- Fork the repository and create a new branch for your contribution.
- Ensure your code follows the project's coding standards and conventions.
- Submit a pull request with a clear description of your changes and their purpose.
- Participate in discussions, code reviews, and issue tracking to help improve the project collaboratively.

## License
This project is licensed under the MIT License, which allows for free use, modification, and distribution of the software.