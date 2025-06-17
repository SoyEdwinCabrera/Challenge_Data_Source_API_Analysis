# GitHub API Documentation

This file provides documentation for the GitHub API endpoints used in the project. It includes details about the `Search Repositories`, `Get Repository Commits`, and `Get Repository Contents` endpoints, along with their parameters and example URLs. Additionally, it outlines the headers required for authentication and explains the API rate limits with and without a token.

## 📚 Overview

First of all, we need to search for appropriate endpoints to get the data we need. In this case, we use **curl** command to explore the results.

```
curl -s https://api.github.com/ | jq
```

![endpoints](../assets/endpoints.png)


## 🔍 Endpoints Used

After exploring the endpoints, we can see that we need to use the following endpoints to get the data we need:

### 1. Search Repositories
- **Endpoint:** `GET /search/repositories`
- **URL Example:**  
  `https://api.github.com/search/repositories?q=python&per_page=10&page=1`
- **Parameters:**
  - `q`: Search keyword(s)
  - `per_page`: Items per page (max 100)
  - `page`: Pagination

---

### 2. Get Repository Commits
- **Endpoint:** `GET /repos/{owner}/{repo}/commits`
- **URL Example:**  
  `https://api.github.com/repos/pandas-dev/pandas/commits?per_page=10&page=1`
- **Parameters:**
  - `per_page`, `page`: For pagination
  - `sha`, `since`, `until`: Optional filters

---

### 3. Get Repository Contents
- **Endpoint:** `GET /repos/{owner}/{repo}/contents/{path}`
- **URL Example:**  
  `https://api.github.com/repos/pandas-dev/pandas/contents/`
- **Parameters:**
  - `path`: Optional path to subfolders or files

---

## ⚙️ Headers Used
```
Authorization: Bearer <MY_ACCESS_TOKEN>
Accept: application/vnd.github+json
X-GitHub-Api-Version: 2022-11-28
```
---

## 📈 Rate Limits

* Without token: 60 req/hour
* With token: 5000 req/hour
* Monitor via headers:
  * X-RateLimit-Remaining
  * X-RateLimit-Reset
