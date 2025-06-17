# Pagination Handling in GitHub API Requests

## Overview

The code implements pagination to efficiently retrieve data from the GitHub API. Pagination is managed using the `per_page` and `page` parameters in the API requests. These parameters allow the user to control the number of items retrieved per request and navigate through the dataset in chunks.

---

## How Pagination Works

1. **`per_page`**:
   - Controls the number of items retrieved in a single request.
   - Example: Setting `per_page=10` retrieves 10 items per request.

2. **`page`**:
   - Specifies the page number to fetch.
   - Example: Setting `page=2` retrieves the second set of items.

3. **Iterative Fetching**:
   - By incrementing the `page` parameter, the user can retrieve all available data in chunks.

---

## Functions with Pagination

### 1. `search_repositories`
- **Description**: Fetches public repositories based on a search query.
- **Pagination Parameters**:
  - `per_page`: Number of repositories per request (default: 10).
  - `page`: Page number to fetch (default: 1).
- **Example URL**:

```
https://api.github.com/search/repositories?q=python&per_page=10&page=1
```

---

### 2. `get_commits`
- **Description**: Retrieves commits from a specific repository.
- **Pagination Parameters**:
  - `per_page`: Number of commits per request (default: 5).
  - `page`: Page number to fetch (default: 1).
- **Example URL**:

```
https://api.github.com/repos/{owner}/{repo}/commits?per_page=5&page=1
```

## Benefits of Pagination

- **Efficiency**: Reduces the amount of data retrieved in a single request, improving performance.
- **Scalability**: Allows handling large datasets by fetching data in manageable chunks.
- **Flexibility**: Enables users to control the size and order of the data retrieved.

---


